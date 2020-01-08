"""
This module provide class to control domain data.
"""


class SlamHardwareController:
    """
    SlamDomainController provide CLI wrapper to manage a SLAM domain
    """
    def __init__(self, api):
        """
        :param self: object itself
        :param api: generic api for SLAM REST api
        """
        self.api = api

    def create(self, options):
        """
        Create a new network on SLAM.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        hardware = {
            'name': options.hardware,
            'description': options.description,
            'owner': options.owner,
            'interface_mac_address': options.interface_mac_address,
            'interface_speed': options.interface_speed,
            'interface_type': options.interface_type
        }
        result = self.api.create('hardware', options.hardware, hardware)
        try:
            if result['status'] == 'done':
                print('hardware {} has been created.'.format(result['hardware']))
            else:
                print('hardware {} creation failed with message\n    {}'.format(result['hardware'],
                                                                                result['message']))
        except KeyError:
            print(result)

    def update(self, options):
        """
        Modify a hardware.

        :param self: object itself
        :param options: arguments pass throught CLI
        """
        modification = options.__dict__
        result = self.api.update('hardware', options.hardware, modification)
        if result['status'] == 'done':
            print('Hardware {} has been modified'.format(options.hardware))
        else:
            print('Hardware {} modification failed with status {}'.format(options.hardware,
                                                                          result['status']))

    def delete(self, options):
        """
        Delete a hardware.

        :return:
        """
        result = self.api.delete('hardware', options.hardware)
        try:
            if result['status'] == 'done':
                print('hardware {} has been deleted'.format(result['hardware']))
            else:
                print('{} deletation failed with message\n    {}'.format(result['hardware'],
                                                                         result['message']))
        except KeyError:
            print(result)

    def add(self, options):
        """
        Add a interface in a hardware.

        :param options: information about the new interface
        :return:
        """
        interface = dict()
        interface['interface_mac_address'] = options.interface_mac_address
        if options.interface_type is not None:
            interface['interface_type'] = options.interface_type
        if options.interface_speed is not None:
            interface['interface_speed'] = options.interface_speed
        result = self.api.create('hardware', options.hardware, interface,
                                 field='interfaces/{}'.format(interface['interface_mac_address']))
        try:
            if result['status'] == 'done':
                print('interface {} has been add to {}'.format(options.interface_mac_address,
                                                               options.hardware))
            else:
                print('{} addition failed with message\n    {}'.format(result['status'],
                                                                       result['message']))
        except KeyError:
            print(result)

    def remove(self, options):
        """
        Remove interface from a hardware
        :param options: arguments pass throught CLI
        :return:
        """
        interface = options.interface_mac_address
        result = self.api.delete('hardware', options.hardware,
                                 field='interfaces/{}'.format(interface))
        try:
            if result['status'] == 'done':
                print('Interface {} has been removed'.format(interface))
            else:
                print('Oops')
        except KeyError:
            print(result)