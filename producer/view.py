"""
This module provide a specific class for domain view management
"""


class SlamProducerView:
    """
    SlamNetworkView provide some ASCII view for domain management
    """
    def __init__(self, api):
        """

        :param self: object itself
        :param api: generic api for SLAM REST Api
        """
        self.api = api

    def diff(self):
        """
        List is the common name for listing all object in a collection.

        :param self: object itself
        """
        diff = self.api.get('producer/diff')
        print(diff['data'])
