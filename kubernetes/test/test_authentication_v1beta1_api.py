# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.authentication_v1beta1_api import AuthenticationV1beta1Api


class TestAuthenticationV1beta1Api(unittest.TestCase):
    """ AuthenticationV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.authentication_v1beta1_api.AuthenticationV1beta1Api()

    def tearDown(self):
        pass

    def test_create_token_review(self):
        """
        Test case for create_token_review

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
