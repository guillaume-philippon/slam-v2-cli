"""
This module provide a specific class for domain view management
"""


class SlamNetworkView:
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
        networks = self.api.list('networks')
        print('networks:')
        for network in networks:
            print('    - {} ({}/{}): {}'.format(network['network'],
                                                network['address'],
                                                network['prefix'],
                                                network['description']))

    def show(self, options):
        """
        Show is the common name for showing information about a particular item in a collection.
        For domain, this is a specific network w/ all entries associated

        :param self: object itself
        :param options: arguments passed throught CLI
        """
        network = self.api.list('networks', options.network)
        print('  network name: {}'.format(network['network']))
        print('   description: {}'.format(network['description']))
        print('       contact: {}'.format(network['contact']))
        print('address/prefix: {}/{}'.format(network['address'], network['prefix']))
        print('       gateway: {}'.format(network['gateway']))
        print('    DNS master: {}'.format(network['dns_master']))
        print('          DHCP: {}'.format(network['dhcp']))
        print('          VLAN: {}'.format(network['vlan']))
        print('     Addresses:')
        for address in network['addresses']:
            print('             - {} {}'.format(address['ip'], address['fqdn']))
