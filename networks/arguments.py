"""
Add domains plugin specific argument for CLI
"""


def networks_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    # First of all, we store action value
    subparsers = parser.add_subparsers(help='Action', dest='action')

    # All action value are listed here
    # - list: list all item in networks
    # - create: create a new network
    # - update: modify a existing network. All value are not mutable
    # - delete: destroy a network
    # - show: show detail of a specific network
    subparsers.add_parser('list', help='list all networks')
    create = subparsers.add_parser('create', help='create new network')
    update = subparsers.add_parser('update', help='update network information')
    delete = subparsers.add_parser('delete', help='delete a network')
    show = subparsers.add_parser('show', help='show detail of a specific network')

    # To create a network, we need a network name, a network address and prefix,
    # and optionaly
    #  - description: a description of the network
    #  - gateway: the network gateway
    #  - contact: a contact email for the network
    #  - dns-master: the DNS master of reverse resolution
    #  - dhcp: the DHCP server for the network
    #  - vlan: the VLAN id
    create.add_argument('network', help='network name')
    create.add_argument('--address', help='network address', required=True)
    create.add_argument('--prefix', help='network prefix', required=True)
    create.add_argument('--description', help='a description of the network')
    create.add_argument('--gateway', help='the network gateway address')
    create.add_argument('--contact', help='a contact email for the network')
    create.add_argument('--dns-master', help='DNS master address for reverse DNS')
    create.add_argument('--dhcp', help='DHCP server address')
    create.add_argument('--vlan', help='VLAN id')

    # To delete a network, we just need to know the name
    delete.add_argument('network', help='network name')

    # To update network information, we need the network name and the following value
    # are mutable
    #  - description: a description of the network
    #  - gateway: the network gateway
    #  - contact: a contact email for the network
    #  - dns-master: the DNS master of reverse resolution
    #  - dhcp: the DHCP server for the network
    #  - vlan: the VLAN id
    update.add_argument('network', help='domain name')
    update.add_argument('--description', help='a description of the network')
    update.add_argument('--gateway', help='the network gateway address')
    update.add_argument('--contact', help='a contact email for the network')
    update.add_argument('--dns-master', help='DNS master address for reverse DNS')
    update.add_argument('--dhcp', help='DHCP server address')
    update.add_argument('--vlan', help='VLAN id')

    # To have detail of a specific network, we just need the network name
    show.add_argument('network', help='network you want to show')
