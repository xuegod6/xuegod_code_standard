#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:04
# @Author  : Xuegod Teacher If
# @File    : demo01.py
# @Software: PyCharm

import xlsxwriter

#创建一个ExceL 文档
workbook = xlsxwriter.Workbook("demo.xlsx")
#创建一个工作对象
worksheet = workbook.add_worksheet()
#设定第一列A的快递20像素
worksheet.set_column("A:E",40)
#加粗 ,粗体
bold =workbook.add_format({"bold":True})
#在A1单元格写入‘hello’blod加粗
worksheet.write("A1","hello")
worksheet.write("A2","word",bold)
worksheet.write("B2","中文测试",bold)
worksheet.insert_image("B5","test.jpeg")
workbook.close()
