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
from kubernetes.client.models.v1beta1_subject_access_review_spec import V1beta1SubjectAccessReviewSpec


class TestV1beta1SubjectAccessReviewSpec(unittest.TestCase):
    """ V1beta1SubjectAccessReviewSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1SubjectAccessReviewSpec(self):
        """
        Test V1beta1SubjectAccessReviewSpec
        """
        model = kubernetes.client.models.v1beta1_subject_access_review_spec.V1beta1SubjectAccessReviewSpec()


if __name__ == '__main__':
    unittest.main()
