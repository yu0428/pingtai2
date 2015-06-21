#!/usr/bin/env python
__author__ = 'bing'

import os
import ConfigParser


class ConfException(Exception):
    pass


class ConfParser:
    """Define methods to read configuration information from conf.txt file."""
    def __init__(self):
        pass

    def read_html_template(self, configuration_file="./conf.txt", section="html_template"):
        """Read html template configuration information and return a dictionary object.
        :param configuration_file: the confiruation file to read from.
        :param section: section of html template configuration.
        :return: a dictionary of html template parameters.
        An ConfException will raised if can not find the corresponding section.
        """
        htmls = self.read_section(configuration_file, section)

        if "template_dir" in htmls and htmls["template_dir"]:
            template_dir = htmls["template_dir"]

            if not os.path.isdir(template_dir):
                raise ConfException("{0} is not a directory in {1} file".
                                    format(template_dir, configuration_file))

            htmls.pop("template_dir")

            if "/" != template_dir[-1:]:
                template_dir += "/"

            for key in htmls:
                if htmls[key] is not None and "" != htmls[key]:
                    htmls[key] = template_dir + htmls[key]
            return htmls

    def read_section(self, configuration_file="./conf.txt", section=""):
        """Read section from configuration_file, return an dictionary object."""
        parser = ConfigParser.ConfigParser()
        parser.read(configuration_file)

        sec = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                sec[item[0]] = item[1]
        else:
            raise ConfException("{0} not found in the {1} file".format(section, configuration_file))
        return sec