import os
import requests
from slackclient import SlackClient

url = "https://api.forecast.io/forecast/"
forecastAPI = os.environ['FORECAST_API']
pdx = "45.5231,-122.6765"
slackToken = os.environ['SLACK_TOKEN']
sc = SlackClient(slackToken)

response = requests.get(url + forecastAPI + "/" + pdx)
json_data = response.json()

weekSummary = json_data['daily']['summary']
todaySummary = json_data['daily']['data'][0]['summary']
todayHigh = json_data['daily']['data'][0]['temperatureMax']
todayLow = json_data['daily']['data'][0]['temperatureMin']
weather = "```%s```\n*Today's Weather*\n  Summary: %s\n  High: %s\n  Low: %s" % (weekSummary, todaySummary, todayHigh, todayLow)

sc.api_call("chat.postMessage", channel="pdx_weather", text=weather, username="slacker")
