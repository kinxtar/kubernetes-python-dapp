# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.version_info import VersionInfo


class TestVersionInfo(unittest.TestCase):
    """ VersionInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersionInfo(self):
        """
        Test VersionInfo
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = kubernetes.client.models.version_info.VersionInfo()
        pass


if __name__ == '__main__':
    unittest.main()
