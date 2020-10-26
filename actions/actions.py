# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted

from actions.mail.mail_api import send_email
from actions.utils.city_check import check_location
from actions.zomato.search_restaurants import SearchRestaurants


class ActionSearchRestaurant(Action):

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        budget = tracker.get_slot("budget")

        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        global response, restaurants
        zomato = SearchRestaurants()

        if budget == "lesser than 300":
            budgetmin = 0
            budgetmax = 300
        elif budget == "between 300 to 700":
            budgetmin = 300
            budgetmax = 700
        else:
            budgetmin = 700
            budgetmax = 10000

        restaurants = zomato.search_restaurants(location, cuisine, budgetmin, budgetmax)
        restaurants_length = len(restaurants)
        top5 = restaurants.head(5)
        # print(restaurants)
        # top 5 results to display
        if restaurants_length > 0:
            response = 'Showing you top results:' + "\n"
            for index, row in top5.iterrows():
                response = response + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + \
                           row['restaurant_address'] + ' and the average budget for two people ' + str(
                    row['budget_for2people']) + "\n"
        else:
            response = 'No restaurants found in your budge'
        dispatcher.utter_message(str(response))
        return []

        if restaurants_length > 0:
            return [SlotSet("restaurant_exists", True)]

        return [SlotSet("restaurant_exists", False)]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')
        top10 = restaurants.head(10)
        print("got this correct")
        send_email(recipient, top10)
        dispatcher.utter_message(text="Please check you inbox")
        return []


class ActionVerfiyLocation(Action):

    def name(self):
        return 'action_verify_location'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        check = check_location(location)
        if check['location_f'] == "notfound":
            dispatcher.utter_message(text="Please enter valid location")
            return [SlotSet("location_ok", False)]
        if check['location_tier'] == "tier3":
            dispatcher.utter_message(text="We do not operate in that area yet")
            return [SlotSet("location_ok", False)]

        return [SlotSet("location_ok", True)]
        #return [SlotSet('location', check['location']), SlotSet('location_ok', check['location_f']),
         #       SlotSet('location_tier', check['location_tier'])]


class ActionVerfiyCuisine(Action):
    def name(self):
        return 'action_verify_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisines_dict = {'american': 1, 'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73,
                         'south indian': 85,
                         'thai': 95}
        cuisine = tracker.get_slot("cuisine")
        return [SlotSet("cuisine_ok", cuisine.lower() in cuisines_dict)]


class ActionVerfiyBudget(Action):
    def name(self):
        return 'action_verify_budget'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("budget_ok", True)]


class ActionRestarted(Action):
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
