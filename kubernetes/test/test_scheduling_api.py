# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.scheduling_api import SchedulingApi


class TestSchedulingApi(unittest.TestCase):
    """ SchedulingApi unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.scheduling_api.SchedulingApi()

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """
        Test case for get_api_group

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
