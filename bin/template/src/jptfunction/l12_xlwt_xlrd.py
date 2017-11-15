#!/usr/bin/python
# coding: utf-8
import xlwt, xlrd
##################################################################
## xlwt 写文件
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
##################################################################
## xlrd 读 excel
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
##################################################################
## 总结:
# xlrd － 读取 Excel 文件
# xlwt － 写入 Excel 文件
# xlutils － 操作 Excel 文件的实用工具, 如复制、分割、筛选等
# 尽管这是目前被用得最多的 Excel 库, 我还是很想吐槽为什么这三个包不能放在一个模块里
# 另外它们有个缺陷, 就是只能处理 xls 文件. 如果你想用新版本的 xlsx, 可以考虑 openpyxl 和 xlsxwriter
# 如果只是读写, 用 Pandas
