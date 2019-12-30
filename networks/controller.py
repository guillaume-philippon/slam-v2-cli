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

    def add(self, options):
        """
        Add a address in a network
        :param options: arguments pass through CLI
        :return:
        """
        if options.ip_address is not None:
            address = options.ip_address
        else:
            address = 'auto'
        result = self.api.create('networks', options.network, dict(), field=address)
        if result['status'] == 'done':
            print('{} has been added'.format(result['address']))
        else:
            print('{} addition failed with message\n    {}'.format(
                result['address'],
                result['message']
            ))

    def remove(self, options):
        """
        Remove a address on a network
        :param options:
        :return:
        """
        result = self.api.delete('networks', options.network, field=options.ip_address)
        if result['status'] == 'done':
            print('{} has been removed'.format(result['address']))
        else:
            print('{} removal failed with message\n    {}'.format(result['address'],
                                                                  result['message']))

    def display(self, options):
        """
        Display all entries in a
        :param options:
        :return:
        """
        feature_uri = '{}'.format(options.address)
        result = self.api.list('networks', options.network, field=feature_uri)
        print('address : {}'.format(result['address']))
        print(' entries:')
        for entry in result['entries']:
            print('        - {}.{} ({})'.format(entry['ns'], entry['domain'], entry['type']))
        pass

    def include(self, options):
        """
        Include a NS entry in a address
        :param options:
        :return:
        """
        if options.type is not None:
            args = {
                'ns_type': options.type
            }
        feature_uri = '{}/{}'.format(options.address, options.fqdn)
        result = self.api.create('networks', options.network, args, field=feature_uri)
        if result['status'] == 'done':
            print('{} has been include'.format(result['entry']))
        else:
            print('{} inclusion failed with message\n    {}'.format(result['entry'],
                                                                    result['message']))

    def exclude(self, options):
        """
        Exclude a NS entry in a address
        :param options:
        :return:
        """
        if options.type is not None:
            args = {
                'ns_type': options.type
            }
        feature_uri = '{}/{}'.format(options.address, options.fqdn)
        result = self.api.delete('networks', options.network, field=feature_uri, options=args)
        if result['status'] == 'done':
            print('{} has been exclude'.format(result['entry']))
        else:
            print('{} exclusion failed with message\n    {}'.format(result['entry'],
                                                                    result['message']))
        pass