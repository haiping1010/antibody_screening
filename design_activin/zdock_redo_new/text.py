#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "w")
print "文件名为: ", fo.name
str = "菜鸟教程"
fo.write( str )

# 关闭文件
fo.close()
