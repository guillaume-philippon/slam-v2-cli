"""
This module provide class to control domain data.
"""


class SlamHardwareController:
    """
    SlamDomainController provide CLI wrapper to manage a SLAM domain
    """
    def __init__(self, api):
        """
        :param self: object itself
        :param api: generic api for SLAM REST api
        """
        self.api = api

    def create(self, options):
        """
        Create a new network on SLAM.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        hardware = {
            'name': options.hardware,
            'description': options.description,
            'owner': options.owner,
            'interface-mac-address': options.interface_mac_address,
            'interface-speed': options.interface_speed,
            'interface-type': options.interface_type
        }
        result = self.api.create('hardware', options.hardware, hardware)
        if result['status'] == 'done':
            print('Hardware {} as been created.'.format(result['hardware']))
        else:
            print('Hardware {} creation failed with status {}'.format(result['hardware'],
                                                                      result['status']))

    def update(self, options):
        """
        Modify a network.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        modification = {}
        if options.contact is not None:
            modification['contact'] = options.contact
        if options.description is not None:
            modification['description'] = options.description
        if options.dns_master is not None:
            modification['dns-master'] = options.dns_master
        if options.gateway is not None:
            modification['gateway'] = options.gateway
        if options.dhcp is not None:
            modification['dhcp'] = options.dhcp
        if options.vlan is not None:
            modification['vlan'] = options.vlan
        result = self.api.update('networks', options.network, modification)
        if result['status'] == 'done':
            print('Network {} has been modified'.format(options.network))
        else:
            print('Network {} modification failed with status {}'.format(options.network,
                                                                         result['status']))
