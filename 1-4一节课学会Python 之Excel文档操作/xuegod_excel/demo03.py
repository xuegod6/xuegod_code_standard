#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:24
# @Author  : Xuegod Teacher If
# @File    : demo03.py
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook("demo3.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"hello")
worksheet.write(1,0,"world")
worksheet.write(2,2,400)
worksheet.write(3,0,3.14159265358)
worksheet.write(4,0,'=SIN(pi()/4)') #插入公式
worksheet.write(5,0,None)  #不插入数据
worksheet.write(6,0,None)  #不插入数据

worksheet.write_number('A6',2.3) #插入数字类型
worksheet.write_url("A7",'http://www.baidu.com') #插入链接
workbook.close()