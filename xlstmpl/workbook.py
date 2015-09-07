from __future__ import unicode_literals

import xlrd
import xlwt

from .context import Context
from .parser import Parser


class Workbook(xlwt.Workbook):

    def __init__(self, *args, **kwargs):
        self.template = kwargs.pop('template')
        super(Workbook, self).__init__(*args, **kwargs)

    def render(self, context):
        ctx = Context(context)

        workbook = xlrd.open_workbook(self.template)
        sheet_names = workbook.sheet_names()
        for sheet_name in sheet_names:

            sheet = workbook.sheet_by_name(sheet_name)
            new_sheet = self.add_sheet(sheet_name)

            for rows in range(sheet.nrows):
                row = new_sheet.row(rows)
                for cols in range(sheet.ncols):
                    val = sheet.cell_value(rows, cols)
                    if val:
                        key = Parser.get_value(val)
                        cell_value = ctx.get(key)
                        row.write(cols, cell_value)
