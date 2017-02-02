#!/usr/bin/python
# coding: utf-8
import xlwt, xlrd
wbk = xlwt.Workbook()             # 写 excel
sheet = wbk.add_sheet('sheet 1')  # sheet 1
sheet.write(0, 0, 'r0,c0')        # 从 0 开始, 先 row 后 column
# sheet.write(0, 0, 'oops')       # 会报错 Exception: Attempt to overwrite cell
sheet.write(0, 1, 'r0,c1')
sheet.write(1, 0, 'r1,c0')
sheet.write(1, 1, 'r1,c1')
sheet2 = wbk.add_sheet('sheet 2', cell_overwrite_ok=True)  # 这样就可以覆盖
sheet2.write(0, 0, 'some text')
sheet2.write(0, 0, 'overwrite')
wbk.save('./l12_xlwt_xlrd.xls')  # 保存
# 读 excel
wb = xlrd.open_workbook('./l12_xlwt_xlrd.xls')
print(wb.sheet_names())     # 检查表单名字
sh1 = wb.sheet_by_index(0)  # 得到表单, 通过索引和名字
sh2 = wb.sheet_by_name(u'sheet 2')
for rownum in range(sh1.nrows):  # 输出每行信息 table.nrows 获取行数
    print(sh1.row_values(rownum))
for colnum in range(sh1.ncols):  # 输出每列信息 table.ncols 获取列数
    print(sh1.col_values(colnum))
first_column = sh1.col_values(0); print(first_column)  # table.row_values(i) 得到列信息
cell_A1 = sh1.cell(0, 1).value; print(cell_A1)  # 得到单元格数值
cell_B2 = sh1.cell(1, 1).value; print(cell_B2)
