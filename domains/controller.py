import argparse

from core.api import SlamAPIController


class SlamDomainController:
    def __init__(self, api):
        self.api = api

    def add(self, options):
        print('Add')
        domain = {
            'name': options.domain,
            'description': options.description,
            'contact': options.contact,
            'master': options.dns_master
        }
        self.api.post('domains', options.domain, domain)
