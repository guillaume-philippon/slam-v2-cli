"""
This module provide class to control domain data.
"""


class SlamHostController:
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
        ns = None
        domain = None
        if options.fqdn is not None:
            fqdn = options.fqdn.split('.', 1)
            ns = fqdn[0]
            domain = fqdn[1]
        host = {
            'interface': options.hardware,
            'network': options.network,
            'ns': ns,
            'domain': domain,
            'ip_address': options.ip_address,
            'no_ip': False
        }
        result = self.api.create('hosts', options.fqdn, host)
        try:
            if result['status'] == 'done':
                print('host {} as been created.'.format(result['name']))
                print(result)
            else:
                print('host {} creation failed with message\n    {}'.format(options.fqdn,
                                                                            result['message']))
        except KeyError:
            print(result)

    def update(self, options):
        """
        Update value of a existing host
        :param options: argument pass through CLI
        :return:
        """
        ns = None
        domain = None
        modification = {}
        if options.fqdn is not None:
            fqdn = options.fqdn.split('.', 1)
            ns = fqdn[0]
            domain = fqdn[1]
        if options.hardware is not None:
            modification['interface'] = options.hardware
        if options.network is not None:
            modification['network'] = options.network
        if options.ip_address is not None:
            modification['ip_address'] = options.ip_address
        result = self.api.update('hosts', options.fqdn, modification)
        try:
            if result['status'] == 'done':
                print('host {} has been updated'.format(result['host']))
            else:
                print('host {} update failed with message\n    {}'.format(result['host'],
                                                                          result['message']))
        except KeyError:
            print(result)

    def delete(self, options):
        """
        Delete a host.

        :return:
        """
        result = self.api.delete('hosts', options.host)
        try:
            if result['status'] == 'done':
                print('host {} as been deleted'.format(result['host']))
            else:
                print('host {} deletation failed with message\n    {}'.format(result['host'],
                                                                              result['message']))
        except KeyError:
            print(result)

    def add(self, options):
        """
        Add a new IP on host
        :param options:
        :return:
        """
        address = dict()
        address['ip_address'] = options.ip_address
        address['fqdn'] = options.fqdn
        result = self.api.create('hosts', options.host, address, field=options.ip_address)
        try:
            if result['status'] == 'done':
                print('address {} has been added'.format(options.ip_address))
            else:
                print('{} addition failed with message\n    {}'.format(result['status'],
                                                                       result['message']))
        except KeyError:
            print(result)
