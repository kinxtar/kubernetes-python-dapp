# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.extensions_v1beta1_deployment import ExtensionsV1beta1Deployment


class TestExtensionsV1beta1Deployment(unittest.TestCase):
    """ ExtensionsV1beta1Deployment unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtensionsV1beta1Deployment(self):
        """
        Test ExtensionsV1beta1Deployment
        """
        model = kubernetes.client.models.extensions_v1beta1_deployment.ExtensionsV1beta1Deployment()


if __name__ == '__main__':
    unittest.main()
