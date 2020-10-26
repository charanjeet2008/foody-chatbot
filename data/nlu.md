## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:restaurant_search
- I am hungry
- I want to have lunch
- I want to have dinner
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- restaurants in budget [lesser than 300](budget)
- restaurants with budget [between 300 to 700](budget) for two people
- restaurants with budget [between 300-700]{"entity": "budget", "value": "between 300 to 700"} for two people
- show me restaurants where the budget for two people is [more than 700](budget)
- show me restaurants where the budget for two people is [>700]{"entity": "budget", "value": "more than 700"}
- [>700]{"entity": "budget", "value": "more than 700"}
- [>700]{"entity": "budget", "value": "more than 700"} budget range
- [<300]{"entity": "budget", "value": "lesser than 300"}
- [<300]{"entity": "budget", "value": "lesser than 300"} budget range
- [300-700]{"entity": "budget", "value": "between 300 to 700"}
- [300-700]{"entity": "budget", "value": "between 300 to 700"} budget range
- [more than 700](budget)
- [lesser than 300](budget)
- [between 300 to 700](budget)
- Rs. [300](email) to [700](email)

## intent:ask_email
- can u mail me the information to [abc@abc.com](email)?
- can u mail to [test@tes.com](email)?
- can u mail me at [test-123.456@dom.123.co.in](email)?
- email address - [test.some@gmail.co.in](email). Mail this list.
- email me at [email-123@domina.com](email)
- mail me [emial@domain.io](email)
- my email address [email.123-abc@domain.123.com](email)
- please mail me the list to [123-email@domain.co.in](email)
- please send me the list to [123@domain.net](email)
- please send this to [email.123@123.456.com](email)
- send this to [abc-email@abc.com](email)
- send to [abc_123-email@abc123.com](email)
- this is my email address - [email-abc_123@abc.com.edu](email). send me an email.
- [email1_34-ret@host-name.123.com](email)

## synonym:Delhi
- New Delhi

## synonym:between 300 to 700
- between 300-700
- 300-700

## synonym:chinese
- chines
- Chinese

## synonym:lesser than 300
- <300

## synonym:more than 700
- >700

## regex:email
- ([\w\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)
