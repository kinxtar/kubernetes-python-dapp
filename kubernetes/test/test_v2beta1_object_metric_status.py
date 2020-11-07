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
from kubernetes.client.models.v2beta1_object_metric_status import V2beta1ObjectMetricStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta1ObjectMetricStatus(unittest.TestCase):
    """V2beta1ObjectMetricStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta1ObjectMetricStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta1_object_metric_status.V2beta1ObjectMetricStatus()  # noqa: E501
        if include_optional :
            return V2beta1ObjectMetricStatus(
                average_value = '0', 
                current_value = '0', 
                metric_name = '0', 
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                target = kubernetes.client.models.v2beta1/cross_version_object_reference.v2beta1.CrossVersionObjectReference(
                    api_version = '0', 
                    kind = '0', 
                    name = '0', )
            )
        else :
            return V2beta1ObjectMetricStatus(
                current_value = '0',
                metric_name = '0',
                target = kubernetes.client.models.v2beta1/cross_version_object_reference.v2beta1.CrossVersionObjectReference(
                    api_version = '0', 
                    kind = '0', 
                    name = '0', ),
        )

    def testV2beta1ObjectMetricStatus(self):
        """Test V2beta1ObjectMetricStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
