# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
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
from kubernetes.client.models.v1beta1_horizontal_pod_autoscaler import V1beta1HorizontalPodAutoscaler


class TestV1beta1HorizontalPodAutoscaler(unittest.TestCase):
    """ V1beta1HorizontalPodAutoscaler unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1HorizontalPodAutoscaler(self):
        """
        Test V1beta1HorizontalPodAutoscaler
        """
        model = kubernetes.client.models.v1beta1_horizontal_pod_autoscaler.V1beta1HorizontalPodAutoscaler()


if __name__ == '__main__':
    unittest.main()
