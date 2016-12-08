# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.3
    
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
from kubernetes.client.apis.extensions_v1beta1_api import ExtensionsV1beta1Api


class TestExtensionsV1beta1Api(unittest.TestCase):
    """ ExtensionsV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.extensions_v1beta1_api.ExtensionsV1beta1Api()

    def tearDown(self):
        pass

    def test_create_namespaced_daemon_set(self):
        """
        Test case for create_namespaced_daemon_set

        
        """
        pass

    def test_create_namespaced_deployment(self):
        """
        Test case for create_namespaced_deployment

        
        """
        pass

    def test_create_namespaced_deployment_rollback_rollback(self):
        """
        Test case for create_namespaced_deployment_rollback_rollback

        
        """
        pass

    def test_create_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for create_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_create_namespaced_ingress(self):
        """
        Test case for create_namespaced_ingress

        
        """
        pass

    def test_create_namespaced_job(self):
        """
        Test case for create_namespaced_job

        
        """
        pass

    def test_create_namespaced_network_policy(self):
        """
        Test case for create_namespaced_network_policy

        
        """
        pass

    def test_create_namespaced_replica_set(self):
        """
        Test case for create_namespaced_replica_set

        
        """
        pass

    def test_create_third_party_resource(self):
        """
        Test case for create_third_party_resource

        
        """
        pass

    def test_delete_collection_namespaced_daemon_set(self):
        """
        Test case for delete_collection_namespaced_daemon_set

        
        """
        pass

    def test_delete_collection_namespaced_deployment(self):
        """
        Test case for delete_collection_namespaced_deployment

        
        """
        pass

    def test_delete_collection_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for delete_collection_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_delete_collection_namespaced_ingress(self):
        """
        Test case for delete_collection_namespaced_ingress

        
        """
        pass

    def test_delete_collection_namespaced_job(self):
        """
        Test case for delete_collection_namespaced_job

        
        """
        pass

    def test_delete_collection_namespaced_network_policy(self):
        """
        Test case for delete_collection_namespaced_network_policy

        
        """
        pass

    def test_delete_collection_namespaced_replica_set(self):
        """
        Test case for delete_collection_namespaced_replica_set

        
        """
        pass

    def test_delete_collection_third_party_resource(self):
        """
        Test case for delete_collection_third_party_resource

        
        """
        pass

    def test_delete_namespaced_daemon_set(self):
        """
        Test case for delete_namespaced_daemon_set

        
        """
        pass

    def test_delete_namespaced_deployment(self):
        """
        Test case for delete_namespaced_deployment

        
        """
        pass

    def test_delete_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for delete_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_delete_namespaced_ingress(self):
        """
        Test case for delete_namespaced_ingress

        
        """
        pass

    def test_delete_namespaced_job(self):
        """
        Test case for delete_namespaced_job

        
        """
        pass

    def test_delete_namespaced_network_policy(self):
        """
        Test case for delete_namespaced_network_policy

        
        """
        pass

    def test_delete_namespaced_replica_set(self):
        """
        Test case for delete_namespaced_replica_set

        
        """
        pass

    def test_delete_third_party_resource(self):
        """
        Test case for delete_third_party_resource

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_daemon_set_for_all_namespaces(self):
        """
        Test case for list_daemon_set_for_all_namespaces

        
        """
        pass

    def test_list_deployment_for_all_namespaces(self):
        """
        Test case for list_deployment_for_all_namespaces

        
        """
        pass

    def test_list_horizontal_pod_autoscaler_for_all_namespaces(self):
        """
        Test case for list_horizontal_pod_autoscaler_for_all_namespaces

        
        """
        pass

    def test_list_ingress_for_all_namespaces(self):
        """
        Test case for list_ingress_for_all_namespaces

        
        """
        pass

    def test_list_job_for_all_namespaces(self):
        """
        Test case for list_job_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_daemon_set(self):
        """
        Test case for list_namespaced_daemon_set

        
        """
        pass

    def test_list_namespaced_deployment(self):
        """
        Test case for list_namespaced_deployment

        
        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for list_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_list_namespaced_ingress(self):
        """
        Test case for list_namespaced_ingress

        
        """
        pass

    def test_list_namespaced_job(self):
        """
        Test case for list_namespaced_job

        
        """
        pass

    def test_list_namespaced_network_policy(self):
        """
        Test case for list_namespaced_network_policy

        
        """
        pass

    def test_list_namespaced_replica_set(self):
        """
        Test case for list_namespaced_replica_set

        
        """
        pass

    def test_list_network_policy_for_all_namespaces(self):
        """
        Test case for list_network_policy_for_all_namespaces

        
        """
        pass

    def test_list_replica_set_for_all_namespaces(self):
        """
        Test case for list_replica_set_for_all_namespaces

        
        """
        pass

    def test_list_third_party_resource(self):
        """
        Test case for list_third_party_resource

        
        """
        pass

    def test_patch_namespaced_daemon_set(self):
        """
        Test case for patch_namespaced_daemon_set

        
        """
        pass

    def test_patch_namespaced_daemon_set_status(self):
        """
        Test case for patch_namespaced_daemon_set_status

        
        """
        pass

    def test_patch_namespaced_deployment(self):
        """
        Test case for patch_namespaced_deployment

        
        """
        pass

    def test_patch_namespaced_deployment_status(self):
        """
        Test case for patch_namespaced_deployment_status

        
        """
        pass

    def test_patch_namespaced_deployments_scale(self):
        """
        Test case for patch_namespaced_deployments_scale

        
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_patch_namespaced_ingress(self):
        """
        Test case for patch_namespaced_ingress

        
        """
        pass

    def test_patch_namespaced_ingress_status(self):
        """
        Test case for patch_namespaced_ingress_status

        
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

    def test_patch_namespaced_network_policy(self):
        """
        Test case for patch_namespaced_network_policy

        
        """
        pass

    def test_patch_namespaced_replica_set(self):
        """
        Test case for patch_namespaced_replica_set

        
        """
        pass

    def test_patch_namespaced_replica_set_status(self):
        """
        Test case for patch_namespaced_replica_set_status

        
        """
        pass

    def test_patch_namespaced_replicasets_scale(self):
        """
        Test case for patch_namespaced_replicasets_scale

        
        """
        pass

    def test_patch_namespaced_replicationcontrollers_scale(self):
        """
        Test case for patch_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_patch_third_party_resource(self):
        """
        Test case for patch_third_party_resource

        
        """
        pass

    def test_read_namespaced_daemon_set(self):
        """
        Test case for read_namespaced_daemon_set

        
        """
        pass

    def test_read_namespaced_daemon_set_status(self):
        """
        Test case for read_namespaced_daemon_set_status

        
        """
        pass

    def test_read_namespaced_deployment(self):
        """
        Test case for read_namespaced_deployment

        
        """
        pass

    def test_read_namespaced_deployment_status(self):
        """
        Test case for read_namespaced_deployment_status

        
        """
        pass

    def test_read_namespaced_deployments_scale(self):
        """
        Test case for read_namespaced_deployments_scale

        
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_read_namespaced_ingress(self):
        """
        Test case for read_namespaced_ingress

        
        """
        pass

    def test_read_namespaced_ingress_status(self):
        """
        Test case for read_namespaced_ingress_status

        
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

    def test_read_namespaced_network_policy(self):
        """
        Test case for read_namespaced_network_policy

        
        """
        pass

    def test_read_namespaced_replica_set(self):
        """
        Test case for read_namespaced_replica_set

        
        """
        pass

    def test_read_namespaced_replica_set_status(self):
        """
        Test case for read_namespaced_replica_set_status

        
        """
        pass

    def test_read_namespaced_replicasets_scale(self):
        """
        Test case for read_namespaced_replicasets_scale

        
        """
        pass

    def test_read_namespaced_replicationcontrollers_scale(self):
        """
        Test case for read_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_read_third_party_resource(self):
        """
        Test case for read_third_party_resource

        
        """
        pass

    def test_replace_namespaced_daemon_set(self):
        """
        Test case for replace_namespaced_daemon_set

        
        """
        pass

    def test_replace_namespaced_daemon_set_status(self):
        """
        Test case for replace_namespaced_daemon_set_status

        
        """
        pass

    def test_replace_namespaced_deployment(self):
        """
        Test case for replace_namespaced_deployment

        
        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """
        Test case for replace_namespaced_deployment_status

        
        """
        pass

    def test_replace_namespaced_deployments_scale(self):
        """
        Test case for replace_namespaced_deployments_scale

        
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_replace_namespaced_ingress(self):
        """
        Test case for replace_namespaced_ingress

        
        """
        pass

    def test_replace_namespaced_ingress_status(self):
        """
        Test case for replace_namespaced_ingress_status

        
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

    def test_replace_namespaced_network_policy(self):
        """
        Test case for replace_namespaced_network_policy

        
        """
        pass

    def test_replace_namespaced_replica_set(self):
        """
        Test case for replace_namespaced_replica_set

        
        """
        pass

    def test_replace_namespaced_replica_set_status(self):
        """
        Test case for replace_namespaced_replica_set_status

        
        """
        pass

    def test_replace_namespaced_replicasets_scale(self):
        """
        Test case for replace_namespaced_replicasets_scale

        
        """
        pass

    def test_replace_namespaced_replicationcontrollers_scale(self):
        """
        Test case for replace_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_replace_third_party_resource(self):
        """
        Test case for replace_third_party_resource

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
