# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1alpha1_pod_preset import V1alpha1PodPreset


class TestV1alpha1PodPreset(unittest.TestCase):
    """ V1alpha1PodPreset unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1PodPreset(self):
        """
        Test V1alpha1PodPreset
        """
        model = kubernetes.client.models.v1alpha1_pod_preset.V1alpha1PodPreset()


if __name__ == '__main__':
    unittest.main()
