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
from kubernetes.client.models.v1beta1_stateful_set import V1beta1StatefulSet


class TestV1beta1StatefulSet(unittest.TestCase):
    """ V1beta1StatefulSet unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1StatefulSet(self):
        """
        Test V1beta1StatefulSet
        """
        model = kubernetes.client.models.v1beta1_stateful_set.V1beta1StatefulSet()


if __name__ == '__main__':
    unittest.main()
