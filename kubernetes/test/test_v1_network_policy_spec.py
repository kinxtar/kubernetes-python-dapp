# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_network_policy_spec import V1NetworkPolicySpec


class TestV1NetworkPolicySpec(unittest.TestCase):
    """ V1NetworkPolicySpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NetworkPolicySpec(self):
        """
        Test V1NetworkPolicySpec
        """
        model = kubernetes.client.models.v1_network_policy_spec.V1NetworkPolicySpec()


if __name__ == '__main__':
    unittest.main()
