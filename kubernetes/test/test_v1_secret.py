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
from kubernetes.client.models.v1_secret import V1Secret


class TestV1Secret(unittest.TestCase):
    """ V1Secret unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Secret(self):
        """
        Test V1Secret
        """
        model = kubernetes.client.models.v1_secret.V1Secret()


if __name__ == '__main__':
    unittest.main()
