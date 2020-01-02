"""
Add domains plugin specific argument for CLI
"""


def producer_argparse(parser):
    """
    Add subparser to have specific options for domain management

    :param parser: main argument parser
    """
    # First of all, we store action value
    subparsers = parser.add_subparsers(help='Action', dest='action')

    # All action value are listed here
    subparsers.add_parser('commit', help='create DNS/DHCP/Radius file from SLAM database')
    subparsers.add_parser('diff', help='diff of produced file and file currently in production')
    subparsers.add_parser('publish', help='publish the last version of the files')
