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
from kubernetes.client.models.v1beta1_stateful_set_status import V1beta1StatefulSetStatus


class TestV1beta1StatefulSetStatus(unittest.TestCase):
    """ V1beta1StatefulSetStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1StatefulSetStatus(self):
        """
        Test V1beta1StatefulSetStatus
        """
        model = kubernetes.client.models.v1beta1_stateful_set_status.V1beta1StatefulSetStatus()


if __name__ == '__main__':
    unittest.main()
