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
from kubernetes.client.models.v1_affinity import V1Affinity


class TestV1Affinity(unittest.TestCase):
    """ V1Affinity unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Affinity(self):
        """
        Test V1Affinity
        """
        model = kubernetes.client.models.v1_affinity.V1Affinity()


if __name__ == '__main__':
    unittest.main()
