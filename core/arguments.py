"""
This module provide generic argument construction. It's built to be easy to add new
module
"""
import argparse
from domains.arguments import domains_argparse
from networks.arguments import networks_argparse
from hardware.arguments import hardware_argparse
from hosts.arguments import hosts_argparse
from producer.arguments import producer_argparse


class SlamArgumentsParser:
    """
    SlamArgumentParser is a generic argument parser for SLAM REST API.
    """
    def __init__(self):
        """
        Here we built all parser and subparser.
        """
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='Plugins', dest='plugin', required=True)

        domains = subparsers.add_parser('domains')
        networks = subparsers.add_parser('networks')
        hardware = subparsers.add_parser('hardware')
        hosts = subparsers.add_parser('hosts')
        producer = subparsers.add_parser('producer')

        domains_argparse(domains)
        networks_argparse(networks)
        hardware_argparse(hardware)
        hosts_argparse(hosts)
        producer_argparse(producer)

        args = parser.parse_args()
        self.args = args

    def plugin(self):
        """
        Easy way to retrieve plugin value
        :return:
        """
        return self.args.plugin

    def action(self):
        """
        Easy way to retrieve action value
        :return:
        """
        return self.args.action

    def show(self):
        """
        Easy way to retrieve show value
        :return:
        """
        if self.args.plugin == 'domains':
            return self.args.domain
        return None

    def options(self):
        """
        Easy way to retrieve all arguments store in a dict()
        :return:
        """
        return self.args
