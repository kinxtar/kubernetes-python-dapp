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
from kubernetes.client.models.v1_node_spec import V1NodeSpec


class TestV1NodeSpec(unittest.TestCase):
    """ V1NodeSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NodeSpec(self):
        """
        Test V1NodeSpec
        """
        model = kubernetes.client.models.v1_node_spec.V1NodeSpec()


if __name__ == '__main__':
    unittest.main()
