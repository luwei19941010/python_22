#-*-coding:utf-8-*-
# Author:Lu Wei
class Foo(object):
    def __init__(self,name):
        self.name=name

obj=Foo('luwei')
v1=getattr(obj,'name')#==obj.name
print(v1)
print(obj.name)
setattr(obj,'name','llll')
if hasattr(obj,'name'):
    print('123')
print(getattr(obj,'name'))
# delattr(obj,'name')
# print(getattr(obj,'name'))