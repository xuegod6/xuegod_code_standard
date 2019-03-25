#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:17
# @Author  : Xuegod Teacher If
# @File    : demo02.py
# @Software: PyCharm
import xlsxwriter
workbook = xlsxwriter.Workbook("demo2.xlsx")

worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('python')
worksheet3 = workbook.add_worksheet("linux")
worksheet4 = workbook.add_worksheet()
workbook.close()