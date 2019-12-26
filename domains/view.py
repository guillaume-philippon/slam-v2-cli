class SlamDomainView:
    def __init__(self, domains):
        self.domains = domains
        pass

    def display_collection(self):
        print('-- Domain list --')
        for domain in self.domains:
            print('  - {}: {}'.format(domain['name'], domain['description']))

    def display_item(self, domain):
        for item in self.domains:
            if item['name'] == domain:
                print('name: {}'.format(item['name']))
                print('description: {}'.format(item['description']))
                print('DNS master: {}'.format(item['master']))
                print('contact: {}'.format(item['contact']))
