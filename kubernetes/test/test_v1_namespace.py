# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_namespace import V1Namespace


class TestV1Namespace(unittest.TestCase):
    """ V1Namespace unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Namespace(self):
        """
        Test V1Namespace
        """
        model = kubernetes.client.models.v1_namespace.V1Namespace()


if __name__ == '__main__':
    unittest.main()
