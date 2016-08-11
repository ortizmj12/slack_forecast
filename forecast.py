#!/usr/bin/env python

import os
import yaml
import requests
import argparse
import tools.config as config
import tools.slack_bot as slack_bot

def get_weather(url, api, location):
    response = requests.get(url + api + "/" + location)
    json_data = response.json()
    weekSummary = json_data['daily']['summary']
    todaySummary = json_data['daily']['data'][0]['summary']
    todayHigh = json_data['daily']['data'][0]['temperatureMax']
    todayLow = json_data['daily']['data'][0]['temperatureMin']
    weather = "```%s```\n*Today's Weather*\n  Summary: %s\n  High: %s\n  Low: %s" % (weekSummary, todaySummary, todayHigh, todayLow)
    return weather

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Check the weather')
    parser.add_argument('config', help='YAML configuration file')
    args = parser.parse_args()
    conf = config.Config(args.config)
    location = conf['location']
    forecast_api_url = conf['forecast_api_url']
    forecast_api_token = conf['forecast_api_token']
    slack_token = conf['slack_token']
    channel = conf['slack_channel']
    username = conf['slack_user']
    bot = slack_bot.Slackbot(slack_token)
    weather = get_weather(forecast_api_url,
                          forecast_api_token,
                          location)
    bot.chat(channel, weather, username)
