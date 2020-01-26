"""
This module provide a specific class for domain view management
"""


class SlamDomainView:
    """
    SlamDomainView provide some ASCII view for domain management
    """
    def __init__(self, api):
        """

        :param self: object itself
        :param api: generic api for SLAM REST Api
        """
        self.api = api

    def list(self):
        """
        List is the common name for listing all object in a collection. For domain, this is
        all domains supported

        :param self: object itself
        """
        domains = self.api.get('domains')
        try:  # In case the server return a unexpected output
            print('domains:')
            for domain in domains:
                print('    - {}: {} ({} records)'.format(domain['name'], domain['description'],
                                                         domain['entries_count']))
        except KeyError:
            print(domains)

    def show(self, options):
        """
        Show is the common name for showing information about a particular item in a collection.
        For domain, this is a specific domain w/ all entries associated

        :param self: object itself
        :param options: arguments passed throught CLI
        """
        domain = self.api.get('domains', options.domain)
        try:  # In case the server return a unexpected output
            print('       name: {}'.format(domain['name']))
            print('description: {}'.format(domain['description']))
            print(' dns-master: {}'.format(domain['dns_master']))
            print('    contact: {}'.format(domain['contact']))
            print('    records:')
            for entry in domain['entries']:
                if entry['type'] == 'A' or entry['type'] == 'PTR':
                    print('        - {}/{} {}'.format(entry['name'], entry['type'],
                                                      ", ".join([str(x['ip'])
                                                                 for x in entry['addresses']])))
                elif entry['type'] == 'CNAME':
                    print('        - {}/{} {}'.format(entry['name'], entry['type'],
                                                      ", ".join([str(x['name'])
                                                                 for x in entry['entries']])))
                else:
                    print('        - {}/{}'.format(entry['name'], entry['type']))
        except KeyError:
            print(domain)
