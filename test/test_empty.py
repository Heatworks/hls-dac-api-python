# coding: utf-8

"""
    HLS - DAC (Data Acquisition and Control)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2017-01-23T14:55:49Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import hls_dac
from hls_dac.rest import ApiException
from hls_dac.models.empty import Empty


class TestEmpty(unittest.TestCase):
    """ Empty unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmpty(self):
        """
        Test Empty
        """
        model = hls_dac.models.empty.Empty()


if __name__ == '__main__':
    unittest.main()
