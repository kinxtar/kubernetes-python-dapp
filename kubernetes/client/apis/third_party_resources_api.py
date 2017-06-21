# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ThirdPartyResourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_third_party_resource(self, namespace, fqdn, resource, body, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_third_party_resource(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
        else:
            (data) = self.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
            return data

    def create_third_party_resource_with_http_info(self, namespace, fqdn, resource, body, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'fqdn', 'resource', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `create_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `create_third_party_resource`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_third_party_resource(self, body, **kwargs):
        """
        Deletes a specific Resource
        Deletes the specified Resource in the specified namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_resource(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param V1DeleteOptions body: (required)
        :param int grace_period_seconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
        :param bool orphan_dependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.
        :param str propagation_policy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_third_party_resource_with_http_info(body, **kwargs)
        else:
            (data) = self.delete_third_party_resource_with_http_info(body, **kwargs)
            return data

    def delete_third_party_resource_with_http_info(self, body, **kwargs):
        """
        Deletes a specific Resource
        Deletes the specified Resource in the specified namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_resource_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param V1DeleteOptions body: (required)
        :param int grace_period_seconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
        :param bool orphan_dependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.
        :param str propagation_policy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'grace_period_seconds', 'orphan_dependents', 'propagation_policy']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'grace_period_seconds' in params:
            query_params['gracePeriodSeconds'] = params['grace_period_seconds']
        if 'orphan_dependents' in params:
            query_params['orphanDependents'] = params['orphan_dependents']
        if 'propagation_policy' in params:
            query_params['propagationPolicy'] = params['propagation_policy']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_third_party_resource(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_resource(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, **kwargs)
        else:
            (data) = self.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, **kwargs)
            return data

    def get_third_party_resource_with_http_info(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'name', 'fqdn', 'resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_third_party_resource`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `get_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `get_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'name' in params:
            path_params['name'] = params['name']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_third_party_resource(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_third_party_resource(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_third_party_resource_with_http_info(fqdn, resource, **kwargs)
        else:
            (data) = self.list_third_party_resource_with_http_info(fqdn, resource, **kwargs)
            return data

    def list_third_party_resource_with_http_info(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_third_party_resource_with_http_info(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'resource', 'watch']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `list_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `list_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/{resource}'.replace('{format}', 'json')
        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}
        if 'watch' in params:
            query_params['watch'] = params['watch']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_third_party_resource(self, namespace, fqdn, resource, body, **kwargs):
        """
        Update a Resource
        Update the specified third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_resource(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
        else:
            (data) = self.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
            return data

    def update_third_party_resource_with_http_info(self, namespace, fqdn, resource, body, **kwargs):
        """
        Update a Resource
        Update the specified third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'fqdn', 'resource', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `update_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `update_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `update_third_party_resource`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
