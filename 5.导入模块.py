#-*-coding:utf-8-*-
# Author:Lu Wei

#用字符串的形式导入模块
import importlib

v=importlib.import_module('x.y')#等于from x import y

#用字符串的形式去对象(模块)找到成员。
getattr(v,'func')()
