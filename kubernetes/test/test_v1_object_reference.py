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
from kubernetes.client.models.v1_object_reference import V1ObjectReference


class TestV1ObjectReference(unittest.TestCase):
    """ V1ObjectReference unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ObjectReference(self):
        """
        Test V1ObjectReference
        """
        model = kubernetes.client.models.v1_object_reference.V1ObjectReference()


if __name__ == '__main__':
    unittest.main()
