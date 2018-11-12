import xlrd
import re


file_path = './file.xlsx'
excel = xlrd.open_workbook(file_path)
sheet = excel.sheet_by_name('Sheet1')

nr = sheet.nrows
ans = dict()
for i in range(1, nr):
    mv = sheet.cell(i, 0).value
    l = sheet.cell(i, 2).value.split('，')
    for i in l:
        if i in ans:
            ans[i].add(mv)
        else:
            ans[i] = {mv}

# print(ans)
for k in ans.items():
    print(k)