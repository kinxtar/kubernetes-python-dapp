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
from kubernetes.client.models.v1_endpoints_list import V1EndpointsList


class TestV1EndpointsList(unittest.TestCase):
    """ V1EndpointsList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1EndpointsList(self):
        """
        Test V1EndpointsList
        """
        model = kubernetes.client.models.v1_endpoints_list.V1EndpointsList()


if __name__ == '__main__':
    unittest.main()
