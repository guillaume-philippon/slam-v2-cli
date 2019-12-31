"""
This module provide a specific class for domain view management
"""


class SlamHostView:
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
        hosts = self.api.list('hosts')
        print('hosts:')
        for host in hosts:
            print('    - {} ()'.format(host['name']))

    def show(self, options):
        """
        Show is a common name for showing information about a particular item in collection.

        :param options: arguments passed througth CLI
        :return:
        """
        host = self.api.list('hosts', options.host)
        print(host)
        print('host: {}'.format(host['host']))
        try:
            print('interface: {}'.format(host['interface']))
        except KeyError:
            pass
        print('main dns entry: {}'.format(host['dns-entry']))
        print('network:')
        try:
            print('    - name: {}'.format(host['network']['name']))
            if host['network']['addresses'] is not None:
                for address in host['addresses']:
                    print('      ip: {}'.format(address))
        except KeyError:
            pass
