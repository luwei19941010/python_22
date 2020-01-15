#-*-coding:utf-8-*-
# Author:Lu Wei
class Foo(object):
	def __iter__(self):
		yield 1 	#返回生成器
		yield 2
		yield 3
obj=Foo()
for item in obj:
    print(item)


