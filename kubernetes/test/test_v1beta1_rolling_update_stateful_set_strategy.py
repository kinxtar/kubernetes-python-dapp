# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_rolling_update_stateful_set_strategy import V1beta1RollingUpdateStatefulSetStrategy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1RollingUpdateStatefulSetStrategy(unittest.TestCase):
    """V1beta1RollingUpdateStatefulSetStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1RollingUpdateStatefulSetStrategy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_rolling_update_stateful_set_strategy.V1beta1RollingUpdateStatefulSetStrategy()  # noqa: E501
        if include_optional :
            return V1beta1RollingUpdateStatefulSetStrategy(
                partition = 56
            )
        else :
            return V1beta1RollingUpdateStatefulSetStrategy(
        )

    def testV1beta1RollingUpdateStatefulSetStrategy(self):
        """Test V1beta1RollingUpdateStatefulSetStrategy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
