import argparse


def domains_argparse(parser):
    # parser.add_argument('test')
    subparsers = parser.add_subparsers(help='Action', dest='action')
    collection = subparsers.add_parser('list', help='list all domains')
    show = subparsers.add_parser('show', help='show detail of spectific domain')
    add = subparsers.add_parser('add', help='add new domain')
    # remove = subparsers.add_parser('remove', help='remove a domain')
    # update = subparsers.add_parser('update', help='update set of value for a domain')
    #
    #
    show.add_argument('domain', help='domain you want to show')
    #
    add.add_argument('domain', help='domain name')
    add.add_argument('--description', help='description of item')
    add.add_argument('--contact', help='contact')
    add.add_argument('--dns-master', help='DNS master address')
    #
    # remove.add_argument('name', help='name of item')
    #
    # update.add_argument('name', help='name of item')