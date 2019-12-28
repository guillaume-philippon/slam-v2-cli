"""
Add domains plugin specific argument for CLI
"""


def hardware_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    subparsers = parser.add_subparsers(help='Action', dest='action')
    subparsers.add_parser('list', help='list all hardware')
    show = subparsers.add_parser('show', help='show detail of a hardware')
    create = subparsers.add_parser('create', help='create new hardware')
    add = subparsers.add_parser('add', help='Add a new host')
    update = subparsers.add_parser('update', help='Update hardware information')
    delete = subparsers.add_parser('delete', help='remove a hardware')
    remove = subparsers.add_parser('remove', help='delete a interface a hardware')

    show.add_argument('hardware', help='hardware you want to show')

    create.add_argument('hardware', help='hardware name')
    create.add_argument('--description', help='description')
    create.add_argument('--owner', help='owner of the hardware')
    create.add_argument('--interface-mac-address', help='Interface address')
    create.add_argument('--interface-speed', help='Interface speed')
    create.add_argument('--interface-type', help='Interface type')

    update.add_argument('hardware', help='hardware name')
    update.add_argument('--description', help='description')
    update.add_argument('--owner', help='owner of the hardware')

    add.add_argument('hardware', help='hardware name')
    add.add_argument('--interface-mac-address', help='Interface address')
    add.add_argument('--interface-speed', help='Interface speed')
    add.add_argument('--interface-type', help='Interface type')

    delete.add_argument('hardware', help='hardware name')

    remove.add_argument('hardware', help='hardware name')
    remove.add_argument('--interface-mac-address', help='Interface address')
