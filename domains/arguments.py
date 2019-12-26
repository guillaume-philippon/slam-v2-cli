"""
Add domains plugin specific argument for CLI
"""


def domains_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    subparsers = parser.add_subparsers(help='Action', dest='action')
    collection = subparsers.add_parser('list', help='list all domains')
    show = subparsers.add_parser('show', help='show detail of a domain')
    create = subparsers.add_parser('create', help='create new domain')
    add = subparsers.add_parser('add', help='Add new fqdn in a domain')
    update = subparsers.add_parser('update', help='Update domain information')
    # remove = subparsers.add_parser('remove', help='remove a domain')

    show.add_argument('domain', help='domain you want to show')

    create.add_argument('domain', help='domain name')
    create.add_argument('--description', help='description of item')
    create.add_argument('--contact', help='contact')
    create.add_argument('--dns-master', help='DNS master address')

    add.add_argument('fqdn', help='Create a new DNS entry')
    add.add_argument('--description', help='description of item')
    add.add_argument('--type', help='DNS type')

    update.add_argument('domain', help='domain name')
    update.add_argument('--description', help='description of item')
    update.add_argument('--contact', help='contact')
    update.add_argument('--dns-master', help='DNS master address')
