import argparse
from domains.arguments import domains_argparse
from networks.arguments import networks_argparse


class SlamArgumentsParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='Plugins', dest='plugin')
        domains = subparsers.add_parser('domains')
        networks = subparsers.add_parser('networks')
        hardware = subparsers.add_parser('hardware')

        domains_argparse(domains)
        networks_argparse(networks)

        args = parser.parse_args()
        self.args = args

    def plugin(self):
        return self.args.plugin

    def action(self):
        return self.args.action

    def show(self):
        if self.args.plugin == 'domains':
            return self.args.domain

    def options(self):
        return self.args
