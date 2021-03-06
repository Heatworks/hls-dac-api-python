# coding: utf-8

"""
    HLS - DAC (Data Acquisition and Control)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2017-01-23T14:55:49Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Datum(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, organization_id=None, device=None, channel=None, occurred=None, value_float=None, value_int=None, value_string=None):
        """
        Datum - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'organization_id': 'str',
            'device': 'str',
            'channel': 'str',
            'occurred': 'float',
            'value_float': 'float',
            'value_int': 'float',
            'value_string': 'str'
        }

        self.attribute_map = {
            'organization_id': 'organizationId',
            'device': 'device',
            'channel': 'channel',
            'occurred': 'occurred',
            'value_float': 'value_float',
            'value_int': 'value_int',
            'value_string': 'value_string'
        }

        self._organization_id = organization_id
        self._device = device
        self._channel = channel
        self._occurred = occurred
        self._value_float = value_float
        self._value_int = value_int
        self._value_string = value_string

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Datum.

        :return: The organization_id of this Datum.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Datum.

        :param organization_id: The organization_id of this Datum.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def device(self):
        """
        Gets the device of this Datum.

        :return: The device of this Datum.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Datum.

        :param device: The device of this Datum.
        :type: str
        """

        self._device = device

    @property
    def channel(self):
        """
        Gets the channel of this Datum.

        :return: The channel of this Datum.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this Datum.

        :param channel: The channel of this Datum.
        :type: str
        """

        self._channel = channel

    @property
    def occurred(self):
        """
        Gets the occurred of this Datum.

        :return: The occurred of this Datum.
        :rtype: float
        """
        return self._occurred

    @occurred.setter
    def occurred(self, occurred):
        """
        Sets the occurred of this Datum.

        :param occurred: The occurred of this Datum.
        :type: float
        """
        if occurred is None:
            raise ValueError("Invalid value for `occurred`, must not be `None`")

        self._occurred = occurred

    @property
    def value_float(self):
        """
        Gets the value_float of this Datum.

        :return: The value_float of this Datum.
        :rtype: float
        """
        return self._value_float

    @value_float.setter
    def value_float(self, value_float):
        """
        Sets the value_float of this Datum.

        :param value_float: The value_float of this Datum.
        :type: float
        """

        self._value_float = value_float

    @property
    def value_int(self):
        """
        Gets the value_int of this Datum.

        :return: The value_int of this Datum.
        :rtype: float
        """
        return self._value_int

    @value_int.setter
    def value_int(self, value_int):
        """
        Sets the value_int of this Datum.

        :param value_int: The value_int of this Datum.
        :type: float
        """

        self._value_int = value_int

    @property
    def value_string(self):
        """
        Gets the value_string of this Datum.

        :return: The value_string of this Datum.
        :rtype: str
        """
        return self._value_string

    @value_string.setter
    def value_string(self, value_string):
        """
        Sets the value_string of this Datum.

        :param value_string: The value_string of this Datum.
        :type: str
        """

        self._value_string = value_string

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
