#!/usr/bin/env python3

import logging
import requests
import json
import datetime
import random
logger = logging.getLogger(__name__)



def getOnThisDay(body):
    req_type = body['payload']['type']
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    url = "https://en.wikipedia.org/api/rest_v1/feed/onthisday/{}/{}/{}".format(req_type, month, day)
    r = requests.get(url)
    data = r.json()
    deaths = []
    births = []
    events = []
    holidays = []
    for x in range(0, 3):
        if req_type == 'deaths' or req_type == 'all': deaths.append(get_relevant_keys(random.choice(data['deaths'])))
        if req_type == 'births' or req_type == 'all': births.append(get_relevant_keys(random.choice(data['births'])))
        if req_type == 'events' or req_type == 'all': events.append(get_relevant_keys(random.choice(data['events'])))
        if req_type == 'holidays' or req_type == 'all': holidays.append(get_relevant_keys(random.choice(data['holidays'])))
    response = {
        'deaths': deaths,
        'births': births,
        'events': events,
        'holidays': holidays
    }
    return [response], 200

def get_relevant_keys(dict):
    temp_dict = []
    temp_dict.append(dict['text'])
    for x in dict['pages']:
        print(x)
        temp_dict.append(x['extract'])
    return temp_dict