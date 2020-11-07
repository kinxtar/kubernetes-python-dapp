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
from kubernetes.client.models.v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NetworkPolicyIngressRule(unittest.TestCase):
    """V1NetworkPolicyIngressRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NetworkPolicyIngressRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_network_policy_ingress_rule.V1NetworkPolicyIngressRule()  # noqa: E501
        if include_optional :
            return V1NetworkPolicyIngressRule(
                _from = [
                    kubernetes.client.models.v1/network_policy_peer.v1.NetworkPolicyPeer(
                        ip_block = kubernetes.client.models.v1/ip_block.v1.IPBlock(
                            cidr = '0', 
                            except = [
                                '0'
                                ], ), 
                        namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                        pod_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), )
                    ], 
                ports = [
                    kubernetes.client.models.v1/network_policy_port.v1.NetworkPolicyPort(
                        port = kubernetes.client.models.port.port(), 
                        protocol = '0', )
                    ]
            )
        else :
            return V1NetworkPolicyIngressRule(
        )

    def testV1NetworkPolicyIngressRule(self):
        """Test V1NetworkPolicyIngressRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
