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
    # - add: add a ip address
    # - remove: remove a ip address
    # - display: display all entries in a address
    # - include: include a entry in a address
    # - exclude: exclude a entry in a address
    subparsers.add_parser('list', help='list all networks')
    create = subparsers.add_parser('create', help='create new network')
    update = subparsers.add_parser('update', help='update network information')
    delete = subparsers.add_parser('delete', help='delete a network')
    show = subparsers.add_parser('show', help='show detail of a specific network')
    add = subparsers.add_parser('add', help='add a address on a network')
    remove = subparsers.add_parser('remove', help='remove a address on a network')
    display = subparsers.add_parser('display', help='display NS entries in a address')
    include = subparsers.add_parser('include', help='include a NS entry in a address')
    exclude = subparsers.add_parser('exclude', help='exclude a NS entry in a address')

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

    # To add a new ip we need the network name and the following optionals value
    add.add_argument('network', help='network name')
    add.add_argument('--ip-address', help='IP address')

    # To remove a ip address, we need to now the network and ip address
    remove.add_argument('network', help='network name')
    remove.add_argument('--ip-address', help='IP address', required=True)

    # To include a entry in ip address, we need network, address and a fqdn
    display.add_argument('network', help='network name')
    display.add_argument('address', help='address IP')

    # To include a entry in ip address, we need network, address and a fqdn
    include.add_argument('network', help='network name')
    include.add_argument('address', help='address IP')
    include.add_argument('fqdn', help='Full Qualified Domain Name')
    include.add_argument('--type', help='NS type')

    # To exclude a entry in ip address, we need network, address and a fqdn
    exclude.add_argument('network', help='network name')
    exclude.add_argument('address', help='address IP')
    exclude.add_argument('fqdn', help='Full Qualified Domain Name')
    exclude.add_argument('--type', help='NS type')
