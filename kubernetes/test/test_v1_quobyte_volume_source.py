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
from kubernetes.client.models.v1_quobyte_volume_source import V1QuobyteVolumeSource


class TestV1QuobyteVolumeSource(unittest.TestCase):
    """ V1QuobyteVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1QuobyteVolumeSource(self):
        """
        Test V1QuobyteVolumeSource
        """
        model = kubernetes.client.models.v1_quobyte_volume_source.V1QuobyteVolumeSource()


if __name__ == '__main__':
    unittest.main()
