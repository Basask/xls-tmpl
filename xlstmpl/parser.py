from __future__ import unicode_literals

import re


class Parser(object):

    _key_regex = r'{{(.*)}}'

    def __init__(self):
        pass

    @staticmethod
    def get_value(text):
        m = re.search(Parser._key_regex, text)
        return m.group(1)
