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
from kubernetes.client.models.v1_network_policy import V1NetworkPolicy


class TestV1NetworkPolicy(unittest.TestCase):
    """ V1NetworkPolicy unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NetworkPolicy(self):
        """
        Test V1NetworkPolicy
        """
        model = kubernetes.client.models.v1_network_policy.V1NetworkPolicy()


if __name__ == '__main__':
    unittest.main()
