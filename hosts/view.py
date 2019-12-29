"""
This module provide a specific class for domain view management
"""


class SlamHostView:
    """
    SlamNetworkView provide some ASCII view for domain management
    """
    def __init__(self, api):
        """

        :param self: object itself
        :param api: generic api for SLAM REST Api
        """
        self.api = api

    def list(self):
        """
        List is the common name for listing all object in a collection.

        :param self: object itself
        """
        hosts = self.api.list('hosts')
        print('hosts:')
        for host in hosts:
            print('    - {} ({})'.format(host['name'], host['ip-address']))
