# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_env_var import V1EnvVar


class TestV1EnvVar(unittest.TestCase):
    """ V1EnvVar unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1EnvVar(self):
        """
        Test V1EnvVar
        """
        model = kubernetes.client.models.v1_env_var.V1EnvVar()


if __name__ == '__main__':
    unittest.main()
