# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-snapshot
    
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
from kubernetes.client.apis.batch_v2alpha1_api import BatchV2alpha1Api


class TestBatchV2alpha1Api(unittest.TestCase):
    """ BatchV2alpha1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.batch_v2alpha1_api.BatchV2alpha1Api()

    def tearDown(self):
        pass

    def test_create_namespaced_cron_job(self):
        """
        Test case for create_namespaced_cron_job

        
        """
        pass

    def test_create_namespaced_job(self):
        """
        Test case for create_namespaced_job

        
        """
        pass

    def test_create_namespaced_scheduled_job(self):
        """
        Test case for create_namespaced_scheduled_job

        
        """
        pass

    def test_delete_collection_namespaced_cron_job(self):
        """
        Test case for delete_collection_namespaced_cron_job

        
        """
        pass

    def test_delete_collection_namespaced_job(self):
        """
        Test case for delete_collection_namespaced_job

        
        """
        pass

    def test_delete_collection_namespaced_scheduled_job(self):
        """
        Test case for delete_collection_namespaced_scheduled_job

        
        """
        pass

    def test_delete_namespaced_cron_job(self):
        """
        Test case for delete_namespaced_cron_job

        
        """
        pass

    def test_delete_namespaced_job(self):
        """
        Test case for delete_namespaced_job

        
        """
        pass

    def test_delete_namespaced_scheduled_job(self):
        """
        Test case for delete_namespaced_scheduled_job

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_cron_job_for_all_namespaces(self):
        """
        Test case for list_cron_job_for_all_namespaces

        
        """
        pass

    def test_list_job_for_all_namespaces(self):
        """
        Test case for list_job_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_cron_job(self):
        """
        Test case for list_namespaced_cron_job

        
        """
        pass

    def test_list_namespaced_job(self):
        """
        Test case for list_namespaced_job

        
        """
        pass

    def test_list_namespaced_scheduled_job(self):
        """
        Test case for list_namespaced_scheduled_job

        
        """
        pass

    def test_list_scheduled_job_for_all_namespaces(self):
        """
        Test case for list_scheduled_job_for_all_namespaces

        
        """
        pass

    def test_patch_namespaced_cron_job(self):
        """
        Test case for patch_namespaced_cron_job

        
        """
        pass

    def test_patch_namespaced_cron_job_status(self):
        """
        Test case for patch_namespaced_cron_job_status

        
        """
        pass

    def test_patch_namespaced_job(self):
        """
        Test case for patch_namespaced_job

        
        """
        pass

    def test_patch_namespaced_job_status(self):
        """
        Test case for patch_namespaced_job_status

        
        """
        pass

    def test_patch_namespaced_scheduled_job(self):
        """
        Test case for patch_namespaced_scheduled_job

        
        """
        pass

    def test_patch_namespaced_scheduled_job_status(self):
        """
        Test case for patch_namespaced_scheduled_job_status

        
        """
        pass

    def test_read_namespaced_cron_job(self):
        """
        Test case for read_namespaced_cron_job

        
        """
        pass

    def test_read_namespaced_cron_job_status(self):
        """
        Test case for read_namespaced_cron_job_status

        
        """
        pass

    def test_read_namespaced_job(self):
        """
        Test case for read_namespaced_job

        
        """
        pass

    def test_read_namespaced_job_status(self):
        """
        Test case for read_namespaced_job_status

        
        """
        pass

    def test_read_namespaced_scheduled_job(self):
        """
        Test case for read_namespaced_scheduled_job

        
        """
        pass

    def test_read_namespaced_scheduled_job_status(self):
        """
        Test case for read_namespaced_scheduled_job_status

        
        """
        pass

    def test_replace_namespaced_cron_job(self):
        """
        Test case for replace_namespaced_cron_job

        
        """
        pass

    def test_replace_namespaced_cron_job_status(self):
        """
        Test case for replace_namespaced_cron_job_status

        
        """
        pass

    def test_replace_namespaced_job(self):
        """
        Test case for replace_namespaced_job

        
        """
        pass

    def test_replace_namespaced_job_status(self):
        """
        Test case for replace_namespaced_job_status

        
        """
        pass

    def test_replace_namespaced_scheduled_job(self):
        """
        Test case for replace_namespaced_scheduled_job

        
        """
        pass

    def test_replace_namespaced_scheduled_job_status(self):
        """
        Test case for replace_namespaced_scheduled_job_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
