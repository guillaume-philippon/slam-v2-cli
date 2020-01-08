"""
This module provide class to control domain data.
"""


class SlamProducerController:
    """
    SlamDomainController provide CLI wrapper to manage a SLAM domain
    """
    def __init__(self, api):
        """
        :param self: object itself
        :param api: generic api for SLAM REST api
        """
        self.api = api

    def commit(self):
        """
        Create a new network on SLAM.

        :param self: object itself
        """
        result = self.api.create('producer/commit', '', '')
        print(result)

    def publish(self):
        """
        Create a new network on SLAM.

        :param self: object itself
        """
        result = self.api.create('producer/publish', '', '')
        print(result)
