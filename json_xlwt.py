# coding:utf-8
import json,xlwt

f = open("fx.json","r",encoding='utf-8')
data = f.read()
data_list = json.loads(data)

fx_book = xlwt.Workbook(encoding='utf-8')

fx_sheet=fx_book.add_sheet('fx_sheet')

# 0,0,label='Row 0, Column 0 Value'
fx_sheet.write(0,0,'title')
fx_sheet.write(0,1,'link')
fx_sheet.write(0,2,'av号')

for i in range(len(data_list)):
    fx_sheet.write(i+1,0,data_list[i]['title'])
    fx_sheet.write(i+1,1,data_list[i]['link'])
    fx_sheet.write(i+1,2,data_list[i]['av号'])


fx_book.save('fx.xls')




