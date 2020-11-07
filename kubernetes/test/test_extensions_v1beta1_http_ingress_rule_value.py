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
from kubernetes.client.models.extensions_v1beta1_http_ingress_rule_value import ExtensionsV1beta1HTTPIngressRuleValue  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1HTTPIngressRuleValue(unittest.TestCase):
    """ExtensionsV1beta1HTTPIngressRuleValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1HTTPIngressRuleValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_http_ingress_rule_value.ExtensionsV1beta1HTTPIngressRuleValue()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1HTTPIngressRuleValue(
                paths = [
                    kubernetes.client.models.extensions/v1beta1/http_ingress_path.extensions.v1beta1.HTTPIngressPath(
                        backend = kubernetes.client.models.extensions/v1beta1/ingress_backend.extensions.v1beta1.IngressBackend(
                            service_name = '0', 
                            service_port = kubernetes.client.models.service_port.servicePort(), ), 
                        path = '0', )
                    ]
            )
        else :
            return ExtensionsV1beta1HTTPIngressRuleValue(
                paths = [
                    kubernetes.client.models.extensions/v1beta1/http_ingress_path.extensions.v1beta1.HTTPIngressPath(
                        backend = kubernetes.client.models.extensions/v1beta1/ingress_backend.extensions.v1beta1.IngressBackend(
                            service_name = '0', 
                            service_port = kubernetes.client.models.service_port.servicePort(), ), 
                        path = '0', )
                    ],
        )

    def testExtensionsV1beta1HTTPIngressRuleValue(self):
        """Test ExtensionsV1beta1HTTPIngressRuleValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
