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
from kubernetes.client.models.v1alpha1_limited_priority_level_configuration import V1alpha1LimitedPriorityLevelConfiguration  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1LimitedPriorityLevelConfiguration(unittest.TestCase):
    """V1alpha1LimitedPriorityLevelConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1LimitedPriorityLevelConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_limited_priority_level_configuration.V1alpha1LimitedPriorityLevelConfiguration()  # noqa: E501
        if include_optional :
            return V1alpha1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares = 56, 
                limit_response = kubernetes.client.models.v1alpha1/limit_response.v1alpha1.LimitResponse(
                    queuing = kubernetes.client.models.v1alpha1/queuing_configuration.v1alpha1.QueuingConfiguration(
                        hand_size = 56, 
                        queue_length_limit = 56, 
                        queues = 56, ), 
                    type = '0', )
            )
        else :
            return V1alpha1LimitedPriorityLevelConfiguration(
        )

    def testV1alpha1LimitedPriorityLevelConfiguration(self):
        """Test V1alpha1LimitedPriorityLevelConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
