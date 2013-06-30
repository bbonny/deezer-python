""" A client for deezer rest API"""

import json
import requests

from requests_oauthlib import OAuth1
from oauthlib.oauth1 import SIGNATURE_RSA

class Deezer(object):
    DEFAULT_OPTIONS = {
        "server": "https://api.deezer.com",
        "rest_path": "api",
        "rest_api_version": "2.0",
    }

    def __init__(self, options=None):
        """
        """
        self._options = self.DEFAULT_OPTIONS
        self._session = requests.Session()

    def user(self, id=1):
        user = User(self._options, self._session)
        user.find(id)
        return user

    def _get_url(self, path):
        options = self._options
        options.update({'path': path})
        return '{server}/{rest_api_version}/{path}'.format(**options)

    def _get_json(self, path, params=None):
        url = self._get_url(path)
        r = self._session.get(url, params=params)

        r_json = json.loads(r.text)
        return r_json
