# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1alpha1_external_admission_hook_configuration import V1alpha1ExternalAdmissionHookConfiguration


class TestV1alpha1ExternalAdmissionHookConfiguration(unittest.TestCase):
    """ V1alpha1ExternalAdmissionHookConfiguration unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1ExternalAdmissionHookConfiguration(self):
        """
        Test V1alpha1ExternalAdmissionHookConfiguration
        """
        model = kubernetes.client.models.v1alpha1_external_admission_hook_configuration.V1alpha1ExternalAdmissionHookConfiguration()


if __name__ == '__main__':
    unittest.main()
