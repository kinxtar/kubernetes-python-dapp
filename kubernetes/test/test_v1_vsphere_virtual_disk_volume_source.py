# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VsphereVirtualDiskVolumeSource(unittest.TestCase):
    """V1VsphereVirtualDiskVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VsphereVirtualDiskVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_vsphere_virtual_disk_volume_source.V1VsphereVirtualDiskVolumeSource()  # noqa: E501
        if include_optional :
            return V1VsphereVirtualDiskVolumeSource(
                fs_type = '0', 
                storage_policy_id = '0', 
                storage_policy_name = '0', 
                volume_path = '0'
            )
        else :
            return V1VsphereVirtualDiskVolumeSource(
                volume_path = '0',
        )

    def testV1VsphereVirtualDiskVolumeSource(self):
        """Test V1VsphereVirtualDiskVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
