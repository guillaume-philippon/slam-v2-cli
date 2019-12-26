class SlamDomainView:
    def __init__(self, api):
        self.api = api
        pass

    def list(self):
        print('-- Domain list --')
        domains = self.api.list('domains')

        for domain in domains:
            print('  - {}: {}'.format(domain['name'], domain['description']))

    def show(self, options):
        domain = self.api.list('domains', options.domain)
        print('domain: {}'.format(domain['domain']))
        print('description: {}'.format(domain['description']))
        print('DNS master: {}'.format(domain['master']))
        print('contact: {}'.format(domain['contact']))
        print('entries:')
        for entry in domain['entries']:
            print('  - name: {}'.format(entry['name']))
            print('    description: {}'.format(entry['description']))
