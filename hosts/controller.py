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
            'interface': options.interface,
            'network': options.network,
            'ns': ns,
            'domain': domain,
            'ip-address': options.ip_address
        }
        result = self.api.create('hosts', options.fqdn, host)
        if result['status'] == 'done':
            print('Host {} as been created.'.format(result['host']))
        else:
            print('Host {} creation failed with status {}'.format(result['host'],
                                                                  result['status']))

    def delete(self, options):
        """
        Delete a host.

        :return:
        """
        result = self.api.delete('hosts', options.hardware)
        if result['status'] == 'done':
            print('Hosts {} as been deleted')
        else:
            print('Oops..')

