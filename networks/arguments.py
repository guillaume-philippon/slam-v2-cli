"""
Add domains plugin specific argument for CLI
"""


def networks_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    subparsers = parser.add_subparsers(help='Action', dest='action')
    collection = subparsers.add_parser('list', help='list all networks')
    show = subparsers.add_parser('show', help='show detail of a network')
    create = subparsers.add_parser('create', help='create new network')
    add = subparsers.add_parser('add', help='Add a new host')
    update = subparsers.add_parser('update', help='Update network information')
    # remove = subparsers.add_parser('remove', help='remove a domain')

    show.add_argument('network', help='network you want to show')

    create.add_argument('network', help='network name')
    create.add_argument('--description', help='description')
    create.add_argument('--address', help='network address')
    create.add_argument('--prefix', help='network prefix')
    create.add_argument('--gateway', help='network gateway address')
    create.add_argument('--contact', help='contact')
    create.add_argument('--dns-master', help='DNS master address')
    create.add_argument('--dhcp', help='DHCP server address')
    create.add_argument('--vlan', help='VLAN id')

    add.add_argument('fqdn', help='Create a new DNS entry')

    update.add_argument('network', help='domain name')
    update.add_argument('--description', help='description')
    update.add_argument('--gateway', help='network gateway address')
    update.add_argument('--contact', help='contact')
    update.add_argument('--dns-master', help='DNS master address')
    update.add_argument('--dhcp', help='DHCP server address')
    update.add_argument('--vlan', help='VLAN id')
