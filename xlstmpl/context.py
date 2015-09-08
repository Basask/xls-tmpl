from __future__ import unicode_literals


class Context(object):

    def __init__(self, context):
        self.ctx = context

    def get(self, key):
        parts = key.split('.')
        result = None
        if len(parts):
            result = self.ctx.get(parts.pop(0))
            for part in parts:
                result = result.get(part)
        else:
            result = self.ctx.get(key)

        return unicode(result)
