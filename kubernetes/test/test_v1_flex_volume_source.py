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
from kubernetes.client.models.v1_flex_volume_source import V1FlexVolumeSource


class TestV1FlexVolumeSource(unittest.TestCase):
    """ V1FlexVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1FlexVolumeSource(self):
        """
        Test V1FlexVolumeSource
        """
        model = kubernetes.client.models.v1_flex_volume_source.V1FlexVolumeSource()


if __name__ == '__main__':
    unittest.main()
