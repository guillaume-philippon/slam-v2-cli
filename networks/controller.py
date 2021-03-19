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
            'radius': options.radius,
            'vlan': options.vlan,
            'dns_master': options.dns_master
        }
        result = self.api.create('networks', options.network, network)
        try:
            if result['status'] == 'done':
                print('network {} has been created.'.format(result['network']))
            else:
                print('network {} creation failed with message\n    {}'.format(result['network'],
                                                                               result['message']))
        except KeyError:
            print(result)

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
        if options.radius is not None:
            modification['radius'] = options.radius
        if options.vlan is not None:
            modification['vlan'] = options.vlan
        result = self.api.update('networks', options.network, modification)
        try:
            if result['status'] == 'done':
                print('network {} has been modified'.format(result['network']))
            else:
                print('network {} modification failed with message\n    {}'.format(result['network'],
                                                                                   result['message']))
        except KeyError:
            print(result)

    def delete(self, options):
        """
        Delete a network.

        :param options: arguments pass throught CLI
        :return:
        """
        result = self.api.delete('networks', options.network)
        try:
            if result['status'] == 'done':
                print('network {} has been deleted'.format(result['network']))
            else:
                print('network {} deletation failed with message\n    {}'.format(result['network'],
                                                                                 result['message']))
        except KeyError:
            print(result)

    def add(self, options):
        """
        Add a address in a network
        :param options: arguments pass through CLI
        :return:
        """
        arg = dict()
        if options.ip_address is not None:
            address = options.ip_address
        else:
            address = 'auto'
        if options.default_name is not None:
            fqdn = options.default_name.split('.', 1)
            arg['name'] = fqdn[0]
            arg['domain'] = fqdn[1]
        result = self.api.create('networks', options.network, arg, field=address)
        try:
            if result['status'] == 'done':
                print('{} has been added'.format(result['address']))
            else:
                print('{} addition failed with message\n    {}'.format(
                    result['address'],
                    result['message']
                ))
        except KeyError:
            print(result)

    def remove(self, options):
        """
        Remove a address on a network
        :param options:
        :return:
        """
        result = self.api.delete('networks', options.network, field=options.ip_address)
        try:
            if result['status'] == 'done':
                print('{} has been removed'.format(result['address']))
            else:
                print(result)
                print('{} removal failed with message\n    {}'.format(result['address'],
                                                                      result['message']))
        except KeyError:
            print(result)

    def display(self, options):
        """
        Display all entries in a
        :param options:
        :return:
        """
        feature_uri = '{}'.format(options.address)
        result = self.api.get('networks', options.network, field=feature_uri)
        try:
            print('address : {}'.format(result['ip']))
            print(' records:')
            for record in result['ns_entries']:
                print('        - {}.{} ({})'.format(record['name'], record['domain']['name'],
                                                    record['type']))
        except KeyError:
            print(result)

    def include(self, options):
        """
        Include a NS entry in a address
        :param options:
        :return:
        """
        args = {}
        if options.type is not None:
            args = {
                'ns_type': options.type
            }
        feature_uri = '{}/{}'.format(options.address, options.fqdn)
        result = self.api.create('networks', options.network, args, field=feature_uri)
        try:
            if result['status'] == 'done':
                print('{} has been include'.format(result['entry']))
            else:
                print('{} inclusion failed with message\n    {}'.format(result['entry'],
                                                                        result['message']))
        except KeyError:
            print(result)

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
        try:
            if result['status'] == 'done':
                print('{} has been exclude'.format(result['entry']))
            else:
                print('{} exclusion failed with message\n    {}'.format(result['entry'],
                                                                        result['message']))
        except KeyError:
            print(result)
