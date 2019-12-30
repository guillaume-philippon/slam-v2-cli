"""
This module provide class to control domain data.
"""


class SlamNetworkController:
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
        network = {
            'name': options.network,
            'description': options.description,
            'address': options.address,
            'prefix': options.prefix,
            'gateway': options.gateway,
            'dhcp': options.dhcp,
            'vlan': options.vlan,
            'dns_master': options.dns_master
        }
        result = self.api.create('networks', options.network, network)
        if result['status'] == 'done':
            print('network {} has been created.'.format(result['network']))
        else:
            print('network {} creation failed with message\n    {}'.format(result['network'],
                                                                           result['message']))

    def update(self, options):
        """
        Modify a network.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        modification = {}
        if options.description is not None:
            modification['description'] = options.description
        if options.gateway is not None:
            modification['gateway'] = options.gateway
        if options.contact is not None:
            modification['contact'] = options.contact
        if options.dns_master is not None:
            modification['dns_master'] = options.dns_master
        if options.dhcp is not None:
            modification['dhcp'] = options.dhcp
        if options.vlan is not None:
            modification['vlan'] = options.vlan
        result = self.api.update('networks', options.network, modification)
        if result['status'] == 'done':
            print('network {} has been modified'.format(result['network']))
        else:
            print('network {} modification failed with message\n    {}'.format(result['network'],
                                                                               result['message']))

    def delete(self, options):
        """
        Delete a network.

        :param options: arguments pass throught CLI
        :return:
        """
        result = self.api.delete('networks', options.network)
        if result['status'] == 'done':
            print('network {} has been deleted'.format(result['network']))
        else:
            print('network {} deletation failed with message\n    {}'.format(result['network'],
                                                                             result['message']))
