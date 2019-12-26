"""
This module is used to provide configuration for slam-cli
"""
import requests
import json


class SlamAPIController:
    """
    Class config provide specific installation information
    """
    def __init__(self):
        """
        Define some default value
        """
        self.location = 'http://127.0.0.1:8000'
        self.csrf_token_location = '/csrf'
        self.login_location = '/login'
        self.logout_location = '/logout'
        self.username = 'sinese'
        self.password = 'azerty'
        self.plugins = [
            'domains'
        ]
        self.headers = {
            'accept': 'application/json'
        }
        self.session = requests.Session()

    def login(self):
        """
        This method is used to signin slam-v2 REST api.
        """
        # We must get csrf before doing a post action.
        get_csrf = self.session.get("{}{}".format(self.location, self.csrf_token_location),
                                    headers=self.headers)
        # We put CSRF-Token in header
        self.headers['X-CSRFToken'] = get_csrf.cookies['csrftoken']
        data = {
            'username': self.username,
            'password': self.password
        }
        result = self.session.post("{}{}".format(self.location, self.login_location),
                                   data=data,
                                   headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass

    def get(self, plugin, item=None):
        uri = "{}/{}".format(self.location, plugin)
        if item is not None:
            uri = "{}/{}".format(uri, item)
        result = self.session.get(uri, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def create(self, plugin, item, options):
        uri = "{}/{}/{}".format(self.location, plugin, item)
        result = self.session.post(uri, data=options, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def add(self, plugin, item, value, options):
        uri = "{}/{}/{}/{}".format(self.location, plugin, item, value)
        result = self.session.post(uri, data=options, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def update(self, plugin, item, options):
        uri = "{}/{}/{}".format(self.location, plugin, item)
        print(options)
        result = self.session.put(uri, data=options, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
