"""
Add domains plugin specific argument for CLI
"""


def domains_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    # First of all, we store action value
    subparsers = parser.add_subparsers(help='Action', dest='action')

    # All action value are listed here
    # - list: list all item in domains
    # - create: create a new domain
    # - update: modify a existing domain. All value are not mutable
    # - delete: destroy a domain and all its entries
    # - show: show detail of a specific domain
    # - add: add a new entry on a domain
    # - remove: remove a specific entry in a domain.
    subparsers.add_parser('list', help='list all domains')
    create = subparsers.add_parser('create', help='create new domain')
    update = subparsers.add_parser('update', help='update domain informations')
    delete = subparsers.add_parser('delete', help='delete a domain and all associated entry')
    show = subparsers.add_parser('show', help='show detail of a specific domain')
    add = subparsers.add_parser('add', help='Add new entry in a domain')
    remove = subparsers.add_parser('remove', help='remove a entry in a domain')

    # To create a domain, we need a domain name and optionaly
    # - description: a description of the domain
    # - contact: a contact email for the domain
    # - dns-master: the DNS master of the domain
    create.add_argument('domain', help='domain name')
    create.add_argument('--description', help='a description of the domain')
    create.add_argument('--contact', help='a contact email for the domain')
    create.add_argument('--dns-master', help='DNS master address')

    # To delete a domain, we just need to know the domain we want to delete
    delete.add_argument('domain', help='domain name')

    # To update a domain, we need to know the domain name and the following value are
    # mutable
    # - description: a description of the domain
    # - contact: a contact email for the domain
    # - dns-master: the DNS master of the domain
    update.add_argument('domain', help='domain name')
    update.add_argument('--description', help='description of the domain')
    update.add_argument('--contact', help='contact email for the domain')
    update.add_argument('--dns-master', help='DNS master address')

    # To have detail of a specific domain, we just need to know the name of it
    show.add_argument('domain', help='domain name')

    # To add a new entry of a domain, we need know, the Full Qualified Domain Name (fqdn)
    # of the entry and optionaly
    # - description: a description of the entry
    # - type: the type of entry. The type is a bind type (A, AAAA, CNAME, ...)
    add.add_argument('fqdn', help='Full Qualified Domain Name')
    add.add_argument('--description', help='description of the entry')
    add.add_argument('--type', help='bind type')

    # To remove a specific entry, we need to know which fqdn remove
    remove.add_argument('fqdn', help='Full Qualified Domain Name')
