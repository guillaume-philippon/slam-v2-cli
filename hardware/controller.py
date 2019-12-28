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
            'interface-mac-address': options.interface_mac_address,
            'interface-speed': options.interface_speed,
            'interface-type': options.interface_type
        }
        result = self.api.create('hardware', options.hardware, hardware)
        if result['status'] == 'done':
            print('Hardware {} as been created.'.format(result['hardware']))
        else:
            print('Hardware {} creation failed with status {}'.format(result['hardware'],
                                                                      result['status']))

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
        if result['status'] == 'done':
            print('Hardware {} as been deleted')
        else:
            print('Oops..')

    def add(self, options):
        """
        Add a interface in a hardware.

        :param options: information about the new interface
        :return:
        """
        interface = dict()
        interface['interface-mac-address'] = options.interface_mac_address
        if options.interface_type is not None:
            interface['interface-type'] = options.interface_type
        if options.interface_speed is not None:
            interface['interface-speed'] = options.interface_speed
        result = self.api.create('hardware', options.hardware, interface,
                                 field='interfaces/{}'.format(interface['interface-mac-address']))
        if result['status'] == 'done':
            print('Interface {} as been add to {}'.format(options.interface_mac_address,
                                                          options.hardware))
        else:
            print('Interface addition failed with status {}'.format(result['status']))

    def remove(self, options):
        """
        Remove interface from a hardware
        :param options: arguments pass throught CLI
        :return:
        """
        interface = options.interface_mac_address
        result = self.api.delete('hardware', options.hardware,
                                 field='interfaces/{}'.format(interface))
        if result['status'] == 'done':
            print('Interface {} has been removed'.format(interface))
        else:
            print('Oops')
