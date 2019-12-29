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
        domains = self.api.list('domains')

        print('domains:')
        for domain in domains:
            print('    - {}: {}'.format(domain['name'], domain['description']))

    def show(self, options):
        """
        Show is the common name for showing information about a particular item in a collection.
        For domain, this is a specific domain w/ all entries associated

        :param self: object itself
        :param options: arguments passed throught CLI
        """
        domain = self.api.list('domains', options.domain)
        print('domain: {}'.format(domain['domain']))
        print('description: {}'.format(domain['description']))
        print('DNS master: {}'.format(domain['master']))
        print('contact: {}'.format(domain['contact']))
        print('entries:')
        for entry in domain['entries']:
            print('  - name: {}'.format(entry['name']))
            print('    description: {}'.format(entry['description']))
