# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.node_v1alpha1_api import NodeV1alpha1Api


class TestNodeV1alpha1Api(unittest.TestCase):
    """ NodeV1alpha1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.node_v1alpha1_api.NodeV1alpha1Api()

    def tearDown(self):
        pass

    def test_create_runtime_class(self):
        """
        Test case for create_runtime_class

        
        """
        pass

    def test_delete_collection_runtime_class(self):
        """
        Test case for delete_collection_runtime_class

        
        """
        pass

    def test_delete_runtime_class(self):
        """
        Test case for delete_runtime_class

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_runtime_class(self):
        """
        Test case for list_runtime_class

        
        """
        pass

    def test_patch_runtime_class(self):
        """
        Test case for patch_runtime_class

        
        """
        pass

    def test_read_runtime_class(self):
        """
        Test case for read_runtime_class

        
        """
        pass

    def test_replace_runtime_class(self):
        """
        Test case for replace_runtime_class

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
