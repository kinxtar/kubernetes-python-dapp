# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1alpha1_pod_preset_list import V1alpha1PodPresetList


class TestV1alpha1PodPresetList(unittest.TestCase):
    """ V1alpha1PodPresetList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1PodPresetList(self):
        """
        Test V1alpha1PodPresetList
        """
        model = kubernetes.client.models.v1alpha1_pod_preset_list.V1alpha1PodPresetList()


if __name__ == '__main__':
    unittest.main()
