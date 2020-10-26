## happy path
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget":"lesser than 300"}
    - slot{"budget": "lesser than 300"}
    - action_verify_budget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exists": true}    
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye
        - action_restart

## Story from conversation with 80bad71a6cb6499c8e15cbf14d0b7965 on October 26th 2020

* greet
    - utter_greet
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email":"kjl@ljd.com"}
    - slot{"email":"kjl@ljd.com"}
    - slot{"email":"kjl@ljd.com"}
    - action_send_email
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - slot{"budget":"between 300 to 700"}
    - slot{"email":"kjl@ljd.com"}

## Story from conversation with 468c74b3fb4c452eae8c6789c87e556a on October 26th 2020

* greet
    - utter_greet
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email":"charanjeet2008@gmail.com"}
    - slot{"email":"charanjeet2008@gmail.com"}
    - slot{"email":"charanjeet2008@gmail.com"}
    - action_send_email
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - slot{"budget":"more than 700"}
    - slot{"email":"charanjeet2008@gmail.com"}

## New Story

* restaurant_search{"cuisine":"italian","budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - slot{"cuisine":"italian"}
    - slot{"budget":"more than 700"}
    - slot{"cuisine":"italian"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"cuisine":"italian","location":"Bangalore","budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - slot{"cuisine":"italian"}
    - slot{"location":"Bangalore"}
    - action_search_restaurants

## New Story

* restaurant_search{"cuisine":"Italian","location":"Bangalore","budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - slot{"cuisine":"Italian"}
    - slot{"location":"Bangalore"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email":"pallavimaya1170@gmail.com"}
    - slot{"email":"pallavimaya1170@gmail.com"}
    - action_send_email
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"bangalore"}
    - slot{"location":"bangalore"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"lesser than 300"}
    - slot{"budget":"lesser than 300"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
