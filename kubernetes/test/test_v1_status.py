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
from kubernetes.client.models.v1_status import V1Status


class TestV1Status(unittest.TestCase):
    """ V1Status unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Status(self):
        """
        Test V1Status
        """
        model = kubernetes.client.models.v1_status.V1Status()


if __name__ == '__main__':
    unittest.main()
