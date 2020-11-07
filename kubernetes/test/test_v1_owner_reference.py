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
from kubernetes.client.models.v1_owner_reference import V1OwnerReference  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1OwnerReference(unittest.TestCase):
    """V1OwnerReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1OwnerReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_owner_reference.V1OwnerReference()  # noqa: E501
        if include_optional :
            return V1OwnerReference(
                api_version = '0', 
                block_owner_deletion = True, 
                controller = True, 
                kind = '0', 
                name = '0', 
                uid = '0'
            )
        else :
            return V1OwnerReference(
                api_version = '0',
                kind = '0',
                name = '0',
                uid = '0',
        )

    def testV1OwnerReference(self):
        """Test V1OwnerReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
