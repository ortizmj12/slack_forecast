#!/usr/bin/env python

import os
import yaml
import requests
from slackclient import SlackClient

forecast_url = "https://api.forecast.io/forecast/"
forecast_api = os.environ['FORECAST_API']
slackToken = os.environ['SLACK_TOKEN']
sc = SlackClient(slackToken)

def yaml_loader():
    with open("config.yaml", "r") as file_descriptor:
        data = yaml.load(file_descriptor)
        location = data.get('variables')['location']
        channel = data.get('variables')['channel']
        username = data.get('variables')['username']
    return location, channel, username

def get_weather(location):
    response = requests.get(forecast_url + forecast_api + "/" + location)
    json_data = response.json()
    weekSummary = json_data['daily']['summary']
    todaySummary = json_data['daily']['data'][0]['summary']
    todayHigh = json_data['daily']['data'][0]['temperatureMax']
    todayLow = json_data['daily']['data'][0]['temperatureMin']
    weather = "```%s```\n*Today's Weather*\n  Summary: %s\n  High: %s\n  Low: %s" % (weekSummary, todaySummary, todayHigh, todayLow)
    return weather

if __name__ == "__main__":
    location, channel, username = yaml_loader()
    message = get_weather(location)
    sc.api_call("chat.postMessage", channel=channel, text=message, username=username)
