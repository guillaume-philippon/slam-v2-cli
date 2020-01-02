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
        hosts = self.api.get('hosts')
        print(hosts)
        print('hosts:')
        for host in hosts:
            print('    - {}'.format(host['name']))

    def show(self, options):
        """
        Show is a common name for showing information about a particular item in collection.

        :param options: arguments passed througth CLI
        :return:
        """
        host = self.api.get('hosts', options.host)
        print('    host: {}'.format(host['name']))
        try:
            print('hardware:')
            print('        - name: {}'.format(host['hardware']['name']))
            print('           mac: {}'.format(host['hardware']['interface']))
        except KeyError:
            pass
        print(' network:')
        try:
            print('        - main: {}'.format(host['network']['name']))
            print('        - addresses:')
            if host['addresses'] is not None:
                for address in host['addresses']:
                    print('            ip: {}'.format(address['ip']))
        except KeyError:
            pass
