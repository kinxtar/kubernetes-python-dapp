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
from kubernetes.client.models.v1_ceph_fs_volume_source import V1CephFSVolumeSource


class TestV1CephFSVolumeSource(unittest.TestCase):
    """ V1CephFSVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1CephFSVolumeSource(self):
        """
        Test V1CephFSVolumeSource
        """
        model = kubernetes.client.models.v1_ceph_fs_volume_source.V1CephFSVolumeSource()


if __name__ == '__main__':
    unittest.main()
