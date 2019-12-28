"""
Add domains plugin specific argument for CLI
"""


def hardware_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    subparsers = parser.add_subparsers(help='Action', dest='action')
    collection = subparsers.add_parser('list', help='list all hardware')
    show = subparsers.add_parser('show', help='show detail of a hardware')
    create = subparsers.add_parser('create', help='create new hardware')
    add = subparsers.add_parser('add', help='Add a new host')
    update = subparsers.add_parser('update', help='Update hardware information')
    # remove = subparsers.add_parser('remove', help='remove a domain')

    show.add_argument('hardware', help='hardware you want to show')

    create.add_argument('hardware', help='hardware name')
    create.add_argument('--description', help='description')
    create.add_argument('--owner', help='owner of the hardware')
    create.add_argument('--interface-address', help='Interface address')
    create.add_argument('--interface-speed', help='Interface speed')
    create.add_argument('--interface-type', help='Interface type')

    # add.add_argument('fqdn', help='Create a new DNS entry')
    #
    # update.add_argument('hardware', help='hardware name')
