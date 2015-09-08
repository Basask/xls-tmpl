from xlstmpl import Workbook
import json


template = 'template.xls'
context = 'context.json'


f = open(context, 'r')
data = f.read()
j_data = json.loads(data)
f.close()

print j_data

wb = Workbook(template=template)
wb.render(j_data)

wb.save('output.xls')

