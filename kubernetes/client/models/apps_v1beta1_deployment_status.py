# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppsV1beta1DeploymentStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, available_replicas=None, collision_count=None, conditions=None, observed_generation=None, ready_replicas=None, replicas=None, unavailable_replicas=None, updated_replicas=None):
        """
        AppsV1beta1DeploymentStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'available_replicas': 'int',
            'collision_count': 'int',
            'conditions': 'list[AppsV1beta1DeploymentCondition]',
            'observed_generation': 'int',
            'ready_replicas': 'int',
            'replicas': 'int',
            'unavailable_replicas': 'int',
            'updated_replicas': 'int'
        }

        self.attribute_map = {
            'available_replicas': 'availableReplicas',
            'collision_count': 'collisionCount',
            'conditions': 'conditions',
            'observed_generation': 'observedGeneration',
            'ready_replicas': 'readyReplicas',
            'replicas': 'replicas',
            'unavailable_replicas': 'unavailableReplicas',
            'updated_replicas': 'updatedReplicas'
        }

        self._available_replicas = available_replicas
        self._collision_count = collision_count
        self._conditions = conditions
        self._observed_generation = observed_generation
        self._ready_replicas = ready_replicas
        self._replicas = replicas
        self._unavailable_replicas = unavailable_replicas
        self._updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """
        Gets the available_replicas of this AppsV1beta1DeploymentStatus.
        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.

        :return: The available_replicas of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """
        Sets the available_replicas of this AppsV1beta1DeploymentStatus.
        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.

        :param available_replicas: The available_replicas of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._available_replicas = available_replicas

    @property
    def collision_count(self):
        """
        Gets the collision_count of this AppsV1beta1DeploymentStatus.
        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.

        :return: The collision_count of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count):
        """
        Sets the collision_count of this AppsV1beta1DeploymentStatus.
        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.

        :param collision_count: The collision_count of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self):
        """
        Gets the conditions of this AppsV1beta1DeploymentStatus.
        Represents the latest available observations of a deployment's current state.

        :return: The conditions of this AppsV1beta1DeploymentStatus.
        :rtype: list[AppsV1beta1DeploymentCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this AppsV1beta1DeploymentStatus.
        Represents the latest available observations of a deployment's current state.

        :param conditions: The conditions of this AppsV1beta1DeploymentStatus.
        :type: list[AppsV1beta1DeploymentCondition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this AppsV1beta1DeploymentStatus.
        The generation observed by the deployment controller.

        :return: The observed_generation of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this AppsV1beta1DeploymentStatus.
        The generation observed by the deployment controller.

        :param observed_generation: The observed_generation of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """
        Gets the ready_replicas of this AppsV1beta1DeploymentStatus.
        Total number of ready pods targeted by this deployment.

        :return: The ready_replicas of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """
        Sets the ready_replicas of this AppsV1beta1DeploymentStatus.
        Total number of ready pods targeted by this deployment.

        :param ready_replicas: The ready_replicas of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """
        Gets the replicas of this AppsV1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment (their labels match the selector).

        :return: The replicas of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this AppsV1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment (their labels match the selector).

        :param replicas: The replicas of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._replicas = replicas

    @property
    def unavailable_replicas(self):
        """
        Gets the unavailable_replicas of this AppsV1beta1DeploymentStatus.
        Total number of unavailable pods targeted by this deployment.

        :return: The unavailable_replicas of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas):
        """
        Sets the unavailable_replicas of this AppsV1beta1DeploymentStatus.
        Total number of unavailable pods targeted by this deployment.

        :param unavailable_replicas: The unavailable_replicas of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._unavailable_replicas = unavailable_replicas

    @property
    def updated_replicas(self):
        """
        Gets the updated_replicas of this AppsV1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment that have the desired template spec.

        :return: The updated_replicas of this AppsV1beta1DeploymentStatus.
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """
        Sets the updated_replicas of this AppsV1beta1DeploymentStatus.
        Total number of non-terminated pods targeted by this deployment that have the desired template spec.

        :param updated_replicas: The updated_replicas of this AppsV1beta1DeploymentStatus.
        :type: int
        """

        self._updated_replicas = updated_replicas

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
        if not isinstance(other, AppsV1beta1DeploymentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
