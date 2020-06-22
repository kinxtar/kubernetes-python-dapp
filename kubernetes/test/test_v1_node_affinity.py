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
from kubernetes.client.models.v1_node_affinity import V1NodeAffinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NodeAffinity(unittest.TestCase):
    """V1NodeAffinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NodeAffinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_node_affinity.V1NodeAffinity()  # noqa: E501
        if include_optional :
            return V1NodeAffinity(
                preferred_during_scheduling_ignored_during_execution = [
                    kubernetes.client.models.v1/preferred_scheduling_term.v1.PreferredSchedulingTerm(
                        preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                            match_expressions = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            match_fields = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', )
                                ], ), 
                        weight = 56, )
                    ], 
                required_during_scheduling_ignored_during_execution = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                    node_selector_terms = [
                        kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                            match_expressions = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            match_fields = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', )
                                ], )
                        ], )
            )
        else :
            return V1NodeAffinity(
        )

    def testV1NodeAffinity(self):
        """Test V1NodeAffinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
