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
from kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_spec import V2alpha1HorizontalPodAutoscalerSpec


class TestV2alpha1HorizontalPodAutoscalerSpec(unittest.TestCase):
    """ V2alpha1HorizontalPodAutoscalerSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1HorizontalPodAutoscalerSpec(self):
        """
        Test V2alpha1HorizontalPodAutoscalerSpec
        """
        model = kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_spec.V2alpha1HorizontalPodAutoscalerSpec()


if __name__ == '__main__':
    unittest.main()
