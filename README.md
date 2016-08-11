# slack_forecast

A Slack bot that sends weather reports!

I use [The Dark Sky Forecast API](https://developer.forecast.io/) for the weather data.
Also use Slack's [python-slackclient](https://github.com/slackhq/python-slackclient) for sending the messages.


## Setup
- Clone the repo
    - `git clone https://github.com/ortizmj12/slack_forecast.git` or
    - `git clone git@github.com:ortizmj12/slack_forecast.git`
- `cd` into the repo directory and create a new virtualenv
    - `virtualenv venv`
- Install the dependencies
    - `pip install -r requirements`
- Set the **FORECAST_API** and **SLACK_TOKEN** environment variables with the appropriate values
    - `export FORECAST_API=<your_API_here>`
    - `export SLACK_TOKEN=<your_token_here>`
- Set the variables in **config.yaml**
    - Latitude/longitude of the location you want to get weather reports for
    - Channel you want the messages sent to
    - Name of the Slack bot user you're using
- Activate the virtualenv
    - `source venv/bin/activate`
- Send the weather to Slack
    - `python forecast.py`


## Cron job it
I created a cron job to automagically send the weather messages every morning. Maybe not the best way to do it, but I created a bash file to run the script. Why?
1. Because I have environment variables set, I needed to source my .bashrc
2. Because I did this in a virtualenv, I needed to use that virtual environment's python executable

Here's the syntax of the bash script:
```
#!/bin/bash

source /home/user/.bashrc
cd /home/user/git/slack_forecast/
/home/user/git/slack_forecast/venv/bin/python /home/user/git/slack_forecast/forecast.py
```
