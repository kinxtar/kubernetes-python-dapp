# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1HorizontalPodAutoscalerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, max_replicas=None, min_replicas=None, scale_target_ref=None, target_cpu_utilization_percentage=None):
        """
        V1HorizontalPodAutoscalerSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_replicas': 'int',
            'min_replicas': 'int',
            'scale_target_ref': 'V1CrossVersionObjectReference',
            'target_cpu_utilization_percentage': 'int'
        }

        self.attribute_map = {
            'max_replicas': 'maxReplicas',
            'min_replicas': 'minReplicas',
            'scale_target_ref': 'scaleTargetRef',
            'target_cpu_utilization_percentage': 'targetCPUUtilizationPercentage'
        }

        self._max_replicas = max_replicas
        self._min_replicas = min_replicas
        self._scale_target_ref = scale_target_ref
        self._target_cpu_utilization_percentage = target_cpu_utilization_percentage

    @property
    def max_replicas(self):
        """
        Gets the max_replicas of this V1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :return: The max_replicas of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """
        Sets the max_replicas of this V1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :param max_replicas: The max_replicas of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """
        if max_replicas is None:
            raise ValueError("Invalid value for `max_replicas`, must not be `None`")

        self._max_replicas = max_replicas

    @property
    def min_replicas(self):
        """
        Gets the min_replicas of this V1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :return: The min_replicas of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """
        Sets the min_replicas of this V1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :param min_replicas: The min_replicas of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def scale_target_ref(self):
        """
        Gets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.

        :return: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        :rtype: V1CrossVersionObjectReference
        """
        return self._scale_target_ref

    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref):
        """
        Sets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.

        :param scale_target_ref: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        :type: V1CrossVersionObjectReference
        """
        if scale_target_ref is None:
            raise ValueError("Invalid value for `scale_target_ref`, must not be `None`")

        self._scale_target_ref = scale_target_ref

    @property
    def target_cpu_utilization_percentage(self):
        """
        Gets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.

        :return: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._target_cpu_utilization_percentage

    @target_cpu_utilization_percentage.setter
    def target_cpu_utilization_percentage(self, target_cpu_utilization_percentage):
        """
        Sets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.

        :param target_cpu_utilization_percentage: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._target_cpu_utilization_percentage = target_cpu_utilization_percentage

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1HorizontalPodAutoscalerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
