# Foodie Restaurant Bot

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

Zomato apis are used for searching the restaurants. https://developers.zomato.com/documentation#/

### Prerequisites

#### python 3.7.x
#### Rasa 2.0.0 and Rasa X
#### PyCharm 2020.3 (Community Edition) for python development 
#### Rasa_nlu version 2.0.0 (latest) 
#### Rasa_core version 2.0.0

## Built With
* Rasa
* Keras Framework
* Tensorflow
* Slack

- domain file covers all the list  of entities, intents, messages and actions included in the chat bot.
- python version 3.7 and tensorflow 2.3.1 used
- data folder contains the nlu.md and stories.md file as well as Cities-by-Tier.csv.
- zomato api key is applied, search results to be implemented.
- email message is sampled, to be applied in bot for sending messages obtained from zomatoapi.
- Rasa2.0.0 and Rasa X used for interactive stories creation, pycharm, latest used.
- Cities-by-Tier csv file covers the cities for bot to check operated cities.
- Model is trained for tier-1 and tier-2 and few other cities.
- stories file covers the learned messages from model.
- MAC system used ,
- Model is trained on sudfficient data for tier-1 cities.