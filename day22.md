### day22

-  可迭代对象
- 约束+异常
- 反射

#### 内容详细

##### 1.可迭代对象

表象：可以被for循环对象就可以称为是可迭代对象：'xx'，[1，2，3，4]，{2，3，4}

```
class Foo()：
	pass
obj=Foo()
```

思考：如何让一个对象变成一个可迭代对象？

在类中实现__ iter __方法且返回一个迭代器（生成器）

```
class Foo(object):
	def __iter__(self):
		return iter([1,2,3,4])#返回迭代器
obj=Foo()

class Foo(object):
	def __iter__(self):
		yield 1 	#返回生成器
		yield 2
		yield 3
obj=Foo()
```

记住：只要能被for循环就是执行iter方法

##### 2.约束

```
class Interface(object):
    def send(self):
        raise NotImplementedError()

class Base(Interface):
    def send(self):
        pass


class Foo(Interface):
        pass


obj=Foo()
obj1=Base()
obj.send()
obj1.send()
```

##### 3.反射

根据字符串的形式去某个对象中操作他的成员

- getattr(对象,‘字符串')  根据字符串的形式去某个对象中获取对象的成员
- hasattr(对象,‘字符串') 根据字符串的形式去某个对象中判断是否有该成员对象的成员
- setattr(对象，’变量‘，’值‘)根据字符串的形式去某个对象中设置成员
- delattr（对象,‘字符串')根据字符串的形式去某个对象中删除成员

```
class Foo(object):
    def __init__(self,name):
        self.name=name
	def login(self):
		pass
obj=Foo('luwei')
#获取变量
v1=getattr(obj,'name')#==obj.name
print(v1)
print(obj.name)
setattr(obj,'name','llll')#obj.name='llll'
print(getattr(obj,'name'))
if not hasattr(obj,'login')
	return 'no no no '
#获取方法
method_name=getattr(obj,'login')
method_name()
#删除成员
delattr(obj,'name')
```

python一切皆对象，所以以后想要通过字符串的形式操作其内部成员都可以反射的机制实现。



##### 4.特殊模块：importlib

根据字符串形式去导入一个模块。

```
#用字符串的形式导入模块
import importlib

v=importlib.import_module('x.y')#等于from x import y

#用字符串的形式去对象(模块)找到成员。
getattr(v,'func')
```





 