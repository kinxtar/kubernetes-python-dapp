# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest


class TestV1beta1CertificateSigningRequest(unittest.TestCase):
    """ V1beta1CertificateSigningRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1CertificateSigningRequest(self):
        """
        Test V1beta1CertificateSigningRequest
        """
        model = kubernetes.client.models.v1beta1_certificate_signing_request.V1beta1CertificateSigningRequest()


if __name__ == '__main__':
    unittest.main()
