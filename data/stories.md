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

## Story from conversation with 7c4713d6d1a148c0b511bd37a2a9abb7 on October 26th 2020

* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
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
* deny
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Italian"}
    - slot{"budget":"between 300 to 700"}
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Italian"}
    - slot{"budget":"between 300 to 700"}

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

## Story from conversation with 7c4713d6d1a148c0b511bd37a2a9abb7 on October 26th 2020

* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
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
* deny
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Italian"}
    - slot{"budget":"between 300 to 700"}
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Italian"}
    - slot{"budget":"between 300 to 700"}

## New Story

* restaurant_search{"location":"Delhi"}
    - slot{"location":"Delhi"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"more than 700"}
    - slot{"budget":"more than 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye

## New Story

* greet
    - utter_greet
* greet
    - utter_ask_location
* restaurant_search{"location":"Jammu"}
    - slot{"location":"Jammu"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"North Indian"}
    - slot{"cuisine":"North Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"lesser than 300"}
    - slot{"budget":"lesser than 300"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye

## New Story

* restaurant_search{"cuisine":"indian"}
    - slot{"cuisine":"indian"}
    - slot{"cuisine":"indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":false}
    - utter_ask_budget
* restaurant_search{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - slot{"cuisine":"indian"}
    - slot{"budget":"between 300 to 700"}
    - action_verify_location
    - utter_ask_location
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"indian"}
    - slot{"budget":"between 300 to 700"}
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* greet
    - slot{"cuisine":"indian"}
    - slot{"budget":"between 300 to 700"}
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - utter_goodbye

## Story from conversation with 55232b629df14a72942733d032a5b171 on October 26th 2020

* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"lesser than 300"}
    - slot{"budget":"lesser than 300"}
    - slot{"budget":"lesser than 300"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email":"alsd@ldf.com"}
    - slot{"email":"alsd@ldf.com"}
    - slot{"email":"alsd@ldf.com"}
    - action_send_email
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Italian"}
    - slot{"budget":"lesser than 300"}
    - slot{"email":"alsd@ldf.com"}

## New Story

* restaurant_search{"budget":"between 300 to 700","location":"Mumbai"}
    - slot{"budget":"between 300 to 700"}
    - slot{"location":"Mumbai"}
    - slot{"budget":"between 300 to 700"}
    - slot{"location":"Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye

## New Story

* restaurant_search{"location":"Bangalore"}
    - slot{"location":"Bangalore"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
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
* ask_email{"email":"laf@ldf.com"}
    - slot{"email":"laf@ldf.com"}
    - action_send_email
    - utter_goodbye

## New Story

* greet
    - utter_greet
* greet
    - utter_ask_location
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Bangalore"}
    - slot{"location":"Bangalore"}
    - slot{"location":"Bangalore"}
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
* ask_email
    - slot{"location":"Bangalore"}
    - slot{"cuisine":"South Indian"}
    - slot{"budget":"between 300 to 700"}
    - utter_goodbye

## New Story

* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Punjab"}
    - slot{"location":"Punjab"}
    - slot{"location":"Punjab"}
    - action_verify_location
    - slot{"location":"Punjab"}
    - utter_ask_location
* restaurant_search{"location":"Delhi"}
    - slot{"location":"Delhi"}
    - slot{"location":"Delhi"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"North Indian"}
    - slot{"cuisine":"North Indian"}
    - slot{"cuisine":"North Indian"}
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
* ask_email
    - slot{"location":"Punjab"}
    - slot{"location":"Delhi"}
    - slot{"cuisine":"North Indian"}
    - slot{"budget":"more than 700"}
    - utter_goodbye

## New Story

* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* affirm
    - utter_ask_emailid
* ask_email{"email":"lajdf@ldf.com"}
    - slot{"email":"lajdf@ldf.com"}
    - action_send_email
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - utter_ask_budget
* restaurant_search{"budget":"between 300 to 700"}
    - slot{"budget":"between 300 to 700"}
    - action_verify_budget
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
