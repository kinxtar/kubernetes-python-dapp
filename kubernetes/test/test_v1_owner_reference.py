# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_owner_reference import V1OwnerReference


class TestV1OwnerReference(unittest.TestCase):
    """ V1OwnerReference unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1OwnerReference(self):
        """
        Test V1OwnerReference
        """
        model = kubernetes.client.models.v1_owner_reference.V1OwnerReference()


if __name__ == '__main__':
    unittest.main()
