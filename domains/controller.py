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
        entry = dict()
        if options.description is not None:
            entry['description'] = options.description
        if options.type is not None:
            entry['type'] = options.type
        result = self.api.add('domains', domain, name, entry)
        if result['status'] == 'done':
            print('Name resolution {} as been added to domain {}'.format(name, domain))
        else:
            print('Name resolution {}.{} addition has failed with status {}'.format(
                result['name'],
                result['domain'],
                result['status']
            ))

    def update(self, options):
        print(options)
        modification = {}
        if options.contact is not None:
            modification['contact'] = options.contact
        if options.description is not None:
            modification['description'] = options.description
        if options.dns_master is not None:
            modification['master'] = options.dns_master

        result = self.api.update('domains', options.domain, modification)
        print('Domain {} has been modified'.format(options.domain))
