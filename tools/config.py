#!/usr/bin/env python
import yaml
import os
import collections

class ConfigNotFound(Exception):
    pass

class Config(object):
    def __init__(self, ymlfile):
        with open(ymlfile, 'r') as yml:
            configdata = yaml.load(yml)
        forecast_configs = collections.defaultdict(str)
        try:
            forecast_configs.update(configdata['Forecast'])
        except KeyError as e:
            raise ConfigNotFound(e)
        self._location = forecast_configs['location']
        self._forecast_api_url = forecast_configs['url']
        self._forecast_api_token = forecast_configs['forecast_api'] or os.environ['FORECAST_API']
        try:
            assert self._forecast_api_token
        except AssertionError:
            raise ConfigNotFound('Forecast API token required.')
        slack_configs = collections.defaultdict(str)
        try:
            slack_configs.update(configdata['Slack'])
        except KeyError:
            pass # not our fault if they don't use slack
        self._slack_user = slack_configs['username']
        self._slack_channel = slack_configs['channel']
        self._slack_token = slack_configs['api_token']
    def __getitem__(self, key):
        return self.__dict__['_'+key]
    def __setitem__(self, key, item):
        self.__dict__['_'+key] = item
    def __len__(self):
        return len(self.__dict__)
    def __cmp__(self, dict):
        return cmp(self.__dict__, dict)
    def __contains__(self, item):
        return item in self.__dict__
    def __iter__(self):
        return iter(self.__dict__)
    def __unicode__(self):
        return unicode(repr(self.__dict__))
    def __repr__(self):
        return repr(self.__dict__)
    def keys(self):
        return [i.lstrip('_') for i in self.__dict__.keys()]

