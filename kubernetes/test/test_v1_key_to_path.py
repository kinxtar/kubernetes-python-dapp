# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_key_to_path import V1KeyToPath


class TestV1KeyToPath(unittest.TestCase):
    """ V1KeyToPath unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1KeyToPath(self):
        """
        Test V1KeyToPath
        """
        model = kubernetes.client.models.v1_key_to_path.V1KeyToPath()


if __name__ == '__main__':
    unittest.main()
