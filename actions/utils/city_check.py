import json
import pandas as pd

from actions.zomato import zomatopy

global tier1_cities
global tier2_cities
city_df = pd.read_csv("actions/utils/Cities-by-Tier.csv")
tier1_cities_df = city_df.loc[city_df['Tier'] == 'Tier-I']
tier2_cities_df = city_df.loc[city_df['Tier'] == 'Tier-II']
tier1_cities = tier1_cities_df['City'].tolist()
tier2_cities = tier2_cities_df['City'].tolist()
tier1_cities = [x.lower() for x in tier1_cities]
tier2_cities = [x.lower() for x in tier2_cities]


def check_location(loc):
    config = {"user_key": "be2cfee4af568158abde9eae6c636ca6"}
    zomato = zomatopy.initialize_app(config)
    location_detail = zomato.get_location(loc, 1)
    location_json = json.loads(location_detail)
    location_results = len(location_json['location_suggestions'])

    if location_results == 0:
        return {'location_f': 'notfound', 'location_new': None}
    elif tier1_cities.__contains__(loc.lower()):
        return {'location_f': 'found', 'location_tier': 'tier1', 'location': loc}
    elif tier2_cities.__contains__(loc.lower()):
        return {'location_f': 'found', 'location_tier': 'tier1', 'location': loc}
    else:
        return {'location_f': 'notfound', 'location_tier': 'tier3', 'location': loc}
