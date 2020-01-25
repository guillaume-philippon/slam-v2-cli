"""
Add hosts plugin specific argument for CLI
"""


def hosts_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    # First of all, we store action value
    subparsers = parser.add_subparsers(help='Action', dest='action')

    # All action value are listed here
    # - list: list all hosts
    # - create: create a new host
    # - update: modify a existing host. All value are not mutable
    # - delete: destroy a host
    # - show: show detail of a specific host
    subparsers.add_parser('list', help='list all hosts')
    create = subparsers.add_parser('create', help='create new hosts')
    update = subparsers.add_parser('update', help='update hosts information')
    delete = subparsers.add_parser('delete', help='delete a hosts')
    show = subparsers.add_parser('show', help='show detail of a host')
    add = subparsers.add_parser('add', help='add a new IP address')

    # To create a hardware, wee need a name and a interface mac address, some optional informations
    # can be provided as
    # - fqdn
    # - interface
    # - network
    # - ip-address
    create.add_argument('fqdn', help='Full Qualified Domain Name of the machine')
    create.add_argument('--interface', dest='hardware',
                        help='MAC address of the hardware interface')
    create.add_argument('--no-ip', action='store_true', help='do not generate a IP from network')
    networks = create.add_mutually_exclusive_group()
    # networks_options = networks.add_argument_group('g1')
    networks.add_argument('--network', help='network where the interface will be bind')
    networks.add_argument('--ip-address', help='force a specific IP address')

    # To update hardware information, we need to have the name of the hardware. The following
    # informations are mutable:
    update.add_argument('fqdn', help='Full Qualified Domain Name of the machine')
    update.add_argument('--interface', dest='hardware',
                        help='MAC address of the hardware interface')
    # update.add_argument('--dhcp',  help='Swap dhcp flag to false')
    dhcp = update.add_mutually_exclusive_group()
    dhcp.add_argument('--dhcp', dest='dhcp', action='store_true', help='Enable DHCP configuration')
    dhcp.add_argument('--no-dhcp', dest='dhcp', action='store_false', help='Disable DHCP configuration')
    networks = update.add_mutually_exclusive_group()
    networks.add_argument('--network', help='network where the interface will be bind')
    networks.add_argument('--ip-address', help='force a specific IP address')

    # To delete a hardware, we just need to have the hardware name
    delete.add_argument('host', help='host name')

    # To add a new interface on a hardware, we need to know the hardware name and
    # interface mac-address. Other informations are optionals
    #  - interface-speed: the speed of the interface
    #  - interface-type: the type of interface
    add.add_argument('host', help='host name')
    # add.add_argument('--interface-mac-address', help='Interface address', required=True)
    add.add_argument('--ip-address', help='IP address', required=True)
    add.add_argument('--fqdn', help='The fqdn of the new IP')
    # add.add_argument('--interface-speed', help='Interface speed')
    # add.add_argument('--interface-type', help='Interface type')

    # To have detail on a specific hardware, we just need the hardware name
    show.add_argument('host', help='host you want to show')

    # To remove a interface, we need to know the hardware and interface mac address
    # remove.add_argument('hardware', help='hardware name')
    # remove.add_argument('--interface-mac-address', help='Interface address', required=True)
