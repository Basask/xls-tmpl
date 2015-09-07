from __future__ import unicode_literals


class Context(object):

    def __init__(self, context):
        self.ctx = context

    def get(self, key):
        return unicode(self.ctx.get(key))
