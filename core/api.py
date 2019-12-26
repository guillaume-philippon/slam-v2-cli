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
        self.location = 'http://127.0.0.1:8000'
        self.csrf_token_location = '/'
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
        get_csrf = self.session.get("{}{}".format(self.location, self.csrf_token_location),
                                    headers=self.headers)
        self.headers['X-CSRFToken'] = get_csrf.cookies['csrftoken']
        data = {
            'username': self.username,
            'password': self.password
        }
        print(data)
        self.session.post("{}{}".format(self.location, self.login_location), headers=self.headers)

    def get(self, plugin, item=None):
        uri = "{}/{}".format(self.location, plugin)
        if item is not None:
            uri = "{}/{}".format(uri, item)
        result = self.session.get(uri, headers=self.headers)
        return json.loads(result.text)

    def post(self, plugin, item, options):
        uri = "{}/{}/{}".format(self.location, plugin, item)
        print(uri)
        result = self.session.post(uri, data=options, headers=self.headers)
        print(result.text)
