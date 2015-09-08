from xlstmpl import Workbook
import json


template = 'template.xls'
context = 'context.json'


f = open(context, 'r')
data = json.loads(f.read())
f.close()

wb = Workbook(template=template)
wb.render(data)
wb.save('output.xls')
