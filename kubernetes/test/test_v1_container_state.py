# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_container_state import V1ContainerState


class TestV1ContainerState(unittest.TestCase):
    """ V1ContainerState unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ContainerState(self):
        """
        Test V1ContainerState
        """
        model = kubernetes.client.models.v1_container_state.V1ContainerState()


if __name__ == '__main__':
    unittest.main()
