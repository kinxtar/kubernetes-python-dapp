# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.extensions_v1beta1_deployment_spec import ExtensionsV1beta1DeploymentSpec


class TestExtensionsV1beta1DeploymentSpec(unittest.TestCase):
    """ ExtensionsV1beta1DeploymentSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtensionsV1beta1DeploymentSpec(self):
        """
        Test ExtensionsV1beta1DeploymentSpec
        """
        model = kubernetes.client.models.extensions_v1beta1_deployment_spec.ExtensionsV1beta1DeploymentSpec()


if __name__ == '__main__':
    unittest.main()
