# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.certificates_v1alpha1_api import CertificatesV1alpha1Api


class TestCertificatesV1alpha1Api(unittest.TestCase):
    """ CertificatesV1alpha1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.certificates_v1alpha1_api.CertificatesV1alpha1Api()

    def tearDown(self):
        pass

    def test_create_certificate_signing_request(self):
        """
        Test case for create_certificate_signing_request

        
        """
        pass

    def test_delete_certificate_signing_request(self):
        """
        Test case for delete_certificate_signing_request

        
        """
        pass

    def test_delete_collection_certificate_signing_request(self):
        """
        Test case for delete_collection_certificate_signing_request

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_certificate_signing_request(self):
        """
        Test case for list_certificate_signing_request

        
        """
        pass

    def test_patch_certificate_signing_request(self):
        """
        Test case for patch_certificate_signing_request

        
        """
        pass

    def test_read_certificate_signing_request(self):
        """
        Test case for read_certificate_signing_request

        
        """
        pass

    def test_replace_certificate_signing_request(self):
        """
        Test case for replace_certificate_signing_request

        
        """
        pass

    def test_replace_certificate_signing_request_approval(self):
        """
        Test case for replace_certificate_signing_request_approval

        
        """
        pass

    def test_replace_certificate_signing_request_status(self):
        """
        Test case for replace_certificate_signing_request_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
