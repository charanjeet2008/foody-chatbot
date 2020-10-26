import json
import pandas as pd

from actions.zomato import zomatopy

config = {"user_key": "be2cfee4af568158abde9eae6c636ca6"}
zomato = zomatopy.initialize_app(config)


def list_restaurants(loc, cuisine, minBudget, maxBudget=10000):
    location_detail = zomato.get_location(loc, 1)
    location_json = json.loads(location_detail)

    lat = location_json["location_suggestions"][0]["latitude"]
    lon = location_json["location_suggestions"][0]["longitude"]
    cuisines_dict = {'american': 1, 'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73,
                     'south indian': 85,
                     'thai': 95}
    try:
        minBudget = int(minBudget)
    except TypeError:
        minBudget =0

    try:
        maxBudget = int(maxBudget)
    except TypeError:
        maxBudget =5000

    list1 = [0, 20, 40, 60, 80]
    d = []
    df = pd.DataFrame()
    for i in list1:
        print(" parameters to request restaurant search :: ", lat, lon, "cuisine :: " + cuisine,
              str(cuisines_dict.get(cuisine)), i)
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), limit=i)
        d1 = json.loads(results)
        d = d1['restaurants']
        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two'],
                             'restaurant_photo': x['restaurant']['featured_image'],
                             'restaurant_url': x['restaurant']['url']} for x in d])
        df = df.append(df1)

    restaurant_df = df[df.budget_for2people.between(minBudget, maxBudget, inclusive=True)]
    restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)

    return restaurant_df


class SearchRestaurants:
    def search_restaurants(self, loc, cuisine, budgetmin, budgetmax):

        print("location ::", loc, " cuisine ::", cuisine, "price ::", budgetmax)

        global restaurants

        restaurants = list_restaurants(loc, cuisine, budgetmin, budgetmax)
        restaurants.drop_duplicates(inplace=True)
        return restaurants

