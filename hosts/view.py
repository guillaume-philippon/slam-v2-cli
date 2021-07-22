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
        try:
            print('hosts:')
            for host in hosts:
                print('    - {}'.format(host['name']))
        except KeyError:
            print(hosts)

    def show(self, options):
        """
        Show is a common name for showing information about a particular item in collection.

        :param options: arguments passed througth CLI
        :return:
        """
        host = self.api.get('hosts', options.host)
        try:
            print('         name: {}'.format(host['name']))
            print('         dhcp: {}'.format(host['dhcp']))
            print('creation date: {}'.format(host['creation_date']))
            try:
                print('     hardware:')
                print('           - name: {}'.format(host['interface']['hardware']['name']))
                print('             mac: {}'.format(host['interface']['mac_address']))
            except KeyError:
                print('-- debug information --')
                print(host)
                print('-- debug information --')
            print('      network: ({})'.format(host['network']['name']))
            try:
                if host['addresses'] is not None:
                    for address in host['addresses']:
                        print('            - {}'.format(address['ip']))
            except KeyError:
                pass
        except KeyError:
            print(host)
