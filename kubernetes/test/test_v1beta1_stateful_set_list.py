# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_stateful_set_list import V1beta1StatefulSetList


class TestV1beta1StatefulSetList(unittest.TestCase):
    """ V1beta1StatefulSetList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1StatefulSetList(self):
        """
        Test V1beta1StatefulSetList
        """
        model = kubernetes.client.models.v1beta1_stateful_set_list.V1beta1StatefulSetList()


if __name__ == '__main__':
    unittest.main()
