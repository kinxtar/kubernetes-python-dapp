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
from kubernetes.client.models.v1_flocker_volume_source import V1FlockerVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1FlockerVolumeSource(unittest.TestCase):
    """V1FlockerVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1FlockerVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_flocker_volume_source.V1FlockerVolumeSource()  # noqa: E501
        if include_optional :
            return V1FlockerVolumeSource(
                dataset_name = '0', 
                dataset_uuid = '0'
            )
        else :
            return V1FlockerVolumeSource(
        )

    def testV1FlockerVolumeSource(self):
        """Test V1FlockerVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
