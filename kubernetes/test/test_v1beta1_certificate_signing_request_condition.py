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
from kubernetes.client.models.v1beta1_certificate_signing_request_condition import V1beta1CertificateSigningRequestCondition  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1CertificateSigningRequestCondition(unittest.TestCase):
    """V1beta1CertificateSigningRequestCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1CertificateSigningRequestCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_certificate_signing_request_condition.V1beta1CertificateSigningRequestCondition()  # noqa: E501
        if include_optional :
            return V1beta1CertificateSigningRequestCondition(
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                type = '0'
            )
        else :
            return V1beta1CertificateSigningRequestCondition(
                type = '0',
        )

    def testV1beta1CertificateSigningRequestCondition(self):
        """Test V1beta1CertificateSigningRequestCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
