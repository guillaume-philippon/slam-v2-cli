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
        networks = self.api.get('networks')
        try:
            print('networks:')
            for network in networks:
                print('    - {} ({}/{}): {}'.format(network['name'],
                                                    network['address'],
                                                    network['prefix'],
                                                    network['description']))
        except KeyError:
            print(network)

    def show(self, options):
        """
        Show is the common name for showing information about a particular item in a collection.
        For domain, this is a specific network w/ all entries associated

        :param self: object itself
        :param options: arguments passed throught CLI
        """
        network = self.api.get('networks', options.network)
        try:
            print('          name: {}'.format(network['name']))
            print('address/prefix: {}/{}'.format(network['address'], network['prefix']))
            print('       verions: {}'.format(network['version']))
            print('   description: {}'.format(network['description']))
            print('       gateway: {}'.format(network['gateway']))
            print('       contact: {}'.format(network['contact']))
            print('    DNS master: {}'.format(network['dns_master']))
            print('          DHCP: {}'.format(network['dhcp']))
            print('        Radius: {}'.format(network['radius']))
            print('          VLAN: {}'.format(network['vlan']))
            print('     Addresses: {}/{}'.format(network['used_addresses'],
                                                 network['total']))
            for address in network['addresses']:
                print('             - {}'.format(address['ip']))
                for entry in address['ns_entries']:
                    print('                 {}.{} ({})'.format(entry['name'],
                                                               entry['domain']['name'],
                                                               entry['type']))
        except KeyError:
            print(network)
