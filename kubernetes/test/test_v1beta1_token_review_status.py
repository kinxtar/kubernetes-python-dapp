# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_token_review_status import V1beta1TokenReviewStatus


class TestV1beta1TokenReviewStatus(unittest.TestCase):
    """ V1beta1TokenReviewStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1TokenReviewStatus(self):
        """
        Test V1beta1TokenReviewStatus
        """
        model = kubernetes.client.models.v1beta1_token_review_status.V1beta1TokenReviewStatus()


if __name__ == '__main__':
    unittest.main()
