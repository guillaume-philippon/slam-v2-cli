class SlamDomainController:
    def __init__(self, api):
        self.api = api

    def create(self, options):
        domain = {
            'name': options.domain,
            'description': options.description,
            'contact': options.contact,
            'master': options.dns_master
        }
        result = self.api.create('domains', options.domain, domain)
        if result['status'] == 'done':
            print('Domain {} as been created.'.format(result['domain']))
        else:
            print('Domain {} creation failed with status {}'.format(result['domain'],
                                                                    result['status']))

    def add(self, options):
        fqdn = options.fqdn.split('.', 1)
        name = fqdn[0]
        domain = fqdn[1]
        print("{} on domain {}".format(name, domain))
        result = self.api.add('domains', domain, name, {})
