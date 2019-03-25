#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:33
# @Author  : Xuegod Teacher If
# @File    : demo04.py
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook("demo4.xlsx")
worksheet = workbook.add_worksheet()
data = [
[150,152,158,149,155,145,148],
[89, 88,95,93, 98,100, 99],
[201,200,198,175,170,198,195],
]
worksheet.write_row("A1",data[0])
worksheet.write_row("A2",data[1])
worksheet.write_row("A3",data[2])

chart = workbook.add_chart({"type":"column"})

chart.add_series({
    'categories': '=Sheet1!$A$1:$G$1',
    'values': '=Sheet1!$A$1:$G$1',
    'line': {'color': 'black'},
})
chart.set_x_axis({
    'name': '我是横轴',  # 设置 X 轴标题名称
    'name_font': {'size': 14, 'bold': True},  # 设置 X 轴标题字体属性
    'num_font': {'italic': True},  # 设置 X 轴数字字体属性
})


chart.set_size({"width":666,"height":555})
chart.set_title({"name":"业务表"})
chart.set_y_axis({"name":"Mb/s"})
worksheet.insert_chart("A4",chart)
workbook.close()
