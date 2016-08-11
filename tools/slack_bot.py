#!/usr/bin/env python
import slackclient

class Slackbot(object):
    def __init__(self, api_token):
        self._client = slackclient.SlackClient(api_token)
    def chat(self, channel, message, username):
        self._client.api_call('chat.postMessage',
                              channel=channel,
                              text=message,
                              username=username)

