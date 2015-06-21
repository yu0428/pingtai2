#!/usr/bin/env python
__author__ = 'bing'

from confparser import ConfParser
from confparser import ConfException
import unittest


class TestConfParser(unittest.TestCase):

    def test_raise_exception(self):
        """An exception should be raised when html_template doesn't exist or
         when html_template is not a directory.
         """
        confparser = ConfParser()
        with self.assertRaises(ConfException) as excep:
            confparser.read_html_template(configuration_file="./test1_conf.txt")

        with self.assertRaises(ConfException) as excep:
            confparser.read_html_template(configuration_file="./test2_conf.txt")

    def test_html_template(self):
        confparser = ConfParser()
        res = confparser.read_html_template(configuration_file="./test3_conf.txt")
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(res["login_file"], "./html_template/login.html")

    def test_error_file(self):
        confparser = ConfParser()
        res = confparser.read_html_template(configuration_file="./test4_conf.txt")["error_file"]
        self.assertEqual(res, "")
