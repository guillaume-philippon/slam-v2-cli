"""
This module provide class to control domain data.
"""
from ipaddress import ip_address
import re

class SlamProducerController:
    """
    SlamDomainController provide CLI wrapper to manage a SLAM domain
    """
    def __init__(self, api):
        """
        :param self: object itself
        :param api: generic api for SLAM REST api
        """
        self.api = api

    def commit(self):
        """
        Create a new network on SLAM.

        :param self: object itself
        """
        result = self.api.create('producer/commit', '', '')
        print(result['data'])

    def publish(self):
        """
        Create a new network on SLAM.

        :param self: object itself
        """
        result = self.api.create('producer/publish', '', '')
        print(result['data'])

    def import_from_file(self, options):
        """
        Import data from bind9 file. To simplify our code, we assume that all IPv6 machine have
        IPv4 associated w/.

        :return:
        """
        source = open(options.filename, 'r')
        hostname_regex = r'([a-zA-Z0-9\-]*)'
        fullname_regex = r'((([a-zA-Z0-9\-]*).)*)'
        ipv4_regex = r'(([0-9]{1,3}\.){3}[0-9]{1,3})'
        ipv6_regex = r'(([0-9a-f]*:)*[0-9a-f]+)'
        interface_regex = r'(([0-9A-Za-z]{2}:){5}[0-9A-Za-z]{2})'

        ipv4_record_regex = hostname_regex + r'[\s\t]+IN[\s\t]+A[\s\t]+' + ipv4_regex
        ipv6_record_regex = hostname_regex + r'[\s\t]+IN[\s\t]+AAAA[\s\t]+' + ipv6_regex
        cname_record_regex = hostname_regex + r'[\s\t]+IN[\s\t]+CNAME[\s\t]+' + fullname_regex
        dhcp_regex = r'host[\s\t]+' + hostname_regex + '[\s\t]+\{[\s\t]+.*' + interface_regex + '.*'
        ipv6_result = ''
        ipv4_result = ''
        cname_result = ''
        dhcp_result = ''
        for line in source.readlines():
            if line[0] != ';':  # If it's not a comment
                is_ipv4_line = re.match(ipv4_record_regex, line)
                is_ipv6_line = re.match(ipv6_record_regex, line)
                is_cname_line = re.match(cname_record_regex, line)
                is_dhcp_line = re.match(dhcp_regex, line)
                # print(line)
                if is_ipv4_line:  # let's do the work w/ IPv4
                    ipv4_result += 'slam hosts create {}.{} --ip-address {}\n'.format(
                        is_ipv4_line.group(1),
                        options.domain,
                        is_ipv4_line.group(2))
                if is_ipv6_line:  # let's do the work w/ IPv6
                    ipv6_result += 'slam hosts add {}.{} --ip-address {}\n'.format(
                        is_ipv6_line.group(1),
                        options.domain,
                        is_ipv6_line.group(2))
                if is_cname_line:  # let's do the work w/ CNAME
                    cname_result += 'slam domains add {}.{} --type CNAME' \
                                    ' --reference {}\n'.format(is_cname_line.group(1),
                                                               options.domain,
                                                               is_cname_line.group(2)[:-1])
                if is_dhcp_line:  # let's do the work for DHCP
                    dhcp_result += 'slam hosts update {}.{} --interface {} --dhcp\n'.format(
                        is_dhcp_line.group(1),
                        options.domain,
                        is_dhcp_line.group(2).upper())
        print(ipv4_result)
        print(ipv6_result)
        print(cname_result)
        print(dhcp_result)
        source.close()
