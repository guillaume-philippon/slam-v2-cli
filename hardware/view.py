"""
This module provide a specific class for domain view management
"""


class SlamHardwareView:
    """
    SlamNetworkView provide some ASCII view for domain management
    """
    def __init__(self, api):
        """

        :param self: object itself
        :param api: generic api for SLAM REST Api
        """
        self.api = api
        pass

    def list(self):
        """
        List is the common name for listing all object in a collection.

        :param self: object itself
        """
        print('inventory:')
        networks = self.api.list('hardware')
        for network in networks:
            print('    - {} ({}): {}'.format(network['name'],
                                             network['owner'],
                                             network['description']))

    def show(self, options):
        """
        Show is the common name for showing information about a particular item in a collection.
        For domain, this is a specific network w/ all entries associated

        :param self: object itself
        :param options: arguments passed throught CLI
        """
        network = self.api.list('hardware', options.hardware)
        print('network name: {}'.format(network['name']))
        print('description: {}'.format(network['description']))
        print('contact: {}'.format(network['contact']))
        print('address/prefix: {}/{}'.format(network['address'], network['prefix']))
        print('gateway: {}'.format(network['gateway']))
        print('DNS master: {}'.format(network['dns-master']))
        print('DHCP: {}'.format(network['dhcp']))
        print('VLAN: {}'.format(network['vlan']))
