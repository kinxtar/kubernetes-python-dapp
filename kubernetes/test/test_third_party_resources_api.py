# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.third_party_resources_api import ThirdPartyResourcesApi


class TestThirdPartyResourcesApi(unittest.TestCase):
    """ ThirdPartyResourcesApi unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.third_party_resources_api.ThirdPartyResourcesApi()

    def tearDown(self):
        pass

    def test_create_third_party_resource(self):
        """
        Test case for create_third_party_resource

        Create a Resource
        """
        pass

    def test_delete_third_party_resource(self):
        """
        Test case for delete_third_party_resource

        Deletes a specific Resource
        """
        pass

    def test_get_third_party_resource(self):
        """
        Test case for get_third_party_resource

        Gets a specific Resource
        """
        pass

    def test_list_third_party_resource(self):
        """
        Test case for list_third_party_resource

        Gets Resources
        """
        pass

    def test_update_third_party_resource(self):
        """
        Test case for update_third_party_resource

        Update a Resource
        """
        pass


if __name__ == '__main__':
    unittest.main()
