"""
This module provide class to control domain data.
"""


class SlamDomainController:
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
        Create a new domain on SLAM. By default, we only need domain name and DNS master entry

        :param self: object itself
        :param options: arguments pass through CLI
        """
        domain = {
            'name': options.domain,
            'description': options.description,
            'contact': options.contact,
            'dns_master': options.dns_master
        }
        result = self.api.create('domains', options.domain, domain)
        if result['status'] == 'done':
            print('domain {} has been created.'.format(result['name']))
        else:
            print('domain {} creation failed with message:\n    {}'.format(result['domain'],
                                                                           result['message']))

    def update(self, options):
        """
        Modify a domain. This allow to change contact email, description and dns-master

        :param self: object itself
        :param options: arguments pass through CLI
        """
        modification = {}
        if options.contact is not None:
            modification['contact'] = options.contact
        if options.description is not None:
            modification['description'] = options.description
        if options.dns_master is not None:
            modification['dns_master'] = options.dns_master
        result = self.api.update('domains', options.domain, modification)
        if result['status'] == 'done':
            print('domain {} has been updated'.format(options.domain))
        else:
            print('domain {} update failed with message:\n    {}'.format(options.domain,
                                                                         result['message']))

    def delete(self, options):
        """
        Delete a domain on SLAM.

        :param options: arguments pass through CLI
        :return:
        """
        result = self.api.delete('domains', options.domain)
        if result['status'] == 'done':
            print('domain {} has been deleted'.format(options.domain))
        else:
            print('domain {} deletation has failed with message:\n    {}'.format(options.domain,
                                                                                 result['message']))

    def add(self, options):
        """
        Add a new entry into a domain. A entry is a fqdn (ie www.example.com)

        :param self: object itself
        :param options: arguments pass through CLI
        """
        fqdn = options.fqdn.split('.', 1)
        ns = fqdn[0]
        domain = fqdn[1]
        entry = dict()
        args = dict()
        if options.reference is not None:
            alias = options.reference.split('.', 1)
            alias_ns = alias[0]
            alias_domain = alias[1]
            entry['sub_entry_name'] = alias_ns
            entry['sub_entry_domain'] = alias_domain
            entry['sub_entry_type.'] = 'A'
        if options.type is not None:
            entry['ns_type'] = options.type
        if options.description is not None:
            entry['description'] = options.description
        print(entry)
        result = self.api.create('domains', domain, entry, field=ns)
        if result['status'] == 'done':
            print('{} has been added'.format(result['entry']))
        else:
            print('{} addition has failed with message\n    {}'.format(
                result['entry'],
                result['message']
            ))

    def remove(self, options):
        """
        Remove a specific entry into a domain. The entry is represented by it s fqdn

        :param options: argument pass throught CLI
        :return:
        """
        fqdn = options.fqdn.split('.', 1)
        ns = fqdn[0]
        domain = fqdn[1]
        args = dict()
        if options.type is not None:
            args['type'] = options.type
        result = self.api.delete('domains', domain, field=ns, options=args)
        if result['status'] == 'done':
            print('{} as been removed from domain {}'.format(ns, domain))
        else:
            print('{} removal failed with message\n    {}'.format(ns, result['message']))
