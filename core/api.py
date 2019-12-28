"""
This module is used to provide configuration for slam-cli. To make this module generic as possible
we use the following nomenclature
 - collection: a list of item (per example a inventory, a list of domain, ...)
 - item: a specific element into a collection (per example a explicit hardware, a domain, ...)
 - plugin: the python module we want to use
"""
import json
import requests


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

    def list(self, plugin, item=None):
        """
        A standard way to retrieve all element into a collection. item can be use to have a sublevel
        in case of item in collection is itself a collection.

        :param plugin: the plugin we want to use (domains, networks, hardware, ...)
        :param item: a specific element (domain, network, hardware, ...)
        :return:
        """
        uri = "{}/{}".format(self.location, plugin)
        if item is not None:
            uri = "{}/{}".format(uri, item)
        print(uri)
        result = self.session.get(uri, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def create(self, plugin, item, options, field=None):
        """
        This method provide a standard way to create a new item in a collection. field can be use
        to have a sublevel in case of item is in collection is itself a collection.

        :param plugin: the plugin we want to use
        :param item: the element we want to create
        :param options: some additional data needed to create the item
        :param field: act on a specific field of the item.
        :return:
        """
        uri = "{}/{}/{}".format(self.location, plugin, item)
        if field is not None:
            uri = "{}/{}".format(uri, field)
        print(uri)
        result = self.session.post(uri, data=options, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def update(self, plugin, item, options):
        """
        This method provide a standard way to update fields on a item.

        :param plugin: the plugin we want to use
        :param item: the element we want to update
        :param options: a list of field to update
        :return:
        """
        uri = "{}/{}/{}".format(self.location, plugin, item)
        print(uri)
        result = self.session.put(uri, data=options, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)

    def delete(self, plugin, item, field=None):
        """
        This method provide a standard way to delete a item on a collection. Field can be
        used as a sub-level if item's collection is a collection itself

        :param plugin: the plugin we want to use
        :param item: the element we want to remove
        :param field: the field we want to remove
        :return:
        """
        uri = "{}/{}/{}".format(self.location, plugin, item)
        if field is not None:
            uri = "{}/{}".format(uri, field)
        print(uri)
        result = self.session.delete(uri, headers=self.headers)
        try:
            self.headers['X-CSRFToken'] = result.cookies['csrftoken']
        except KeyError:
            pass
        return json.loads(result.text)
