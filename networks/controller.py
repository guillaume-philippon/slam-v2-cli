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
            print('Network {} as been created.'.format(result['network']))
        else:
            print('Network {} creation failed with status {}'.format(result['network'],
                                                                     result['status']))

    def update(self, options):
        """
        Modify a network.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        modification = options.__dict__
        result = self.api.update('networks', options.network, modification)
        if result['status'] == 'done':
            print('Network {} has been modified'.format(options.network))
        else:
            print('Network {} modification failed with status {}'.format(options.network,
                                                                         result['status']))

    def delete(self, options):
        """
        Delete a network.

        :param options: arguments pass throught CLI
        :return:
        """
        result = self.api.delete('networks', options.network)
        if result['status'] == 'done':
            print('network {} has been deleted'.format(options.network))
        else:
            print('Oops')
