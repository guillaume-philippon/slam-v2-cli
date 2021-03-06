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

    def list(self):
        """
        List is the common name for listing all object in a collection.

        :param self: object itself
        """
        networks = self.api.get('hardware')
        try:
            print('inventory:')
            for network in networks:
                print('    - {} ({}): {}'.format(network['name'],
                                                 network['owner'],
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
        hardware = self.api.get('hardware', options.hardware)
        try:
            print('         name: {}'.format(hardware['name']))
            print('  description: {}'.format(hardware['description']))
            print('        owner: {}'.format(hardware['owner']))
            print('       vendor: {}'.format(hardware['vendor']))
            print('        model: {}'.format(hardware['model']))
            print('serial number: {}'.format(hardware['serial_number']))
            print('    inventory: {}'.format(hardware['inventory']))
            print('  buying date: {}'.format(hardware['buying_date']))
            print('     warranty: {}'.format(hardware['warranty']))
            print('   interfaces:')
            for interface in hardware['interfaces']:
                print('        - mac-address: {}'.format(interface['mac_address']))
        except KeyError:
            print(hardware)
