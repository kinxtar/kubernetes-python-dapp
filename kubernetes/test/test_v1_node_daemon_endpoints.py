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
from kubernetes.client.models.v1_node_daemon_endpoints import V1NodeDaemonEndpoints  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NodeDaemonEndpoints(unittest.TestCase):
    """V1NodeDaemonEndpoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NodeDaemonEndpoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_node_daemon_endpoints.V1NodeDaemonEndpoints()  # noqa: E501
        if include_optional :
            return V1NodeDaemonEndpoints(
                kubelet_endpoint = kubernetes.client.models.v1/daemon_endpoint.v1.DaemonEndpoint(
                    port = 56, )
            )
        else :
            return V1NodeDaemonEndpoints(
        )

    def testV1NodeDaemonEndpoints(self):
        """Test V1NodeDaemonEndpoints"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
