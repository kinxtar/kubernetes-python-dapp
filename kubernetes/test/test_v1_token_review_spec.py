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
from kubernetes.client.models.v1_token_review_spec import V1TokenReviewSpec


class TestV1TokenReviewSpec(unittest.TestCase):
    """ V1TokenReviewSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1TokenReviewSpec(self):
        """
        Test V1TokenReviewSpec
        """
        model = kubernetes.client.models.v1_token_review_spec.V1TokenReviewSpec()


if __name__ == '__main__':
    unittest.main()
