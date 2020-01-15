#-*-coding:utf-8-*-
# Author:Lu Wei

#1.请使用面向对象实现栈（后进先出）
'''
class  Foo:
    def __init__(self):
        self.list=[]
    def pop(self):
        a=self.list.pop()
        return a
    def push(self,name):
        self.list.append(name)
        return self.list
obj=Foo()
obj.push('luwei1')
obj.push('luwei2')
obj.push('luwei3')
obj.push('luwei4')
v=obj.push('luwei5')
print(v)
print(obj.pop())
print(obj.pop())
print(obj.pop())


#2.请是用面向对象实现队列（先进先出）
class  Foo:
    def __init__(self):
        self.list=[]
    def pop(self):
        a=self.list.pop(0)
        return a
    def push(self,name):
        self.list.append(name)
        return self.list
obj=Foo()
obj.push('luwei1')
obj.push('luwei2')
obj.push('luwei3')
obj.push('luwei4')
v=obj.push('luwei5')
print(v)
print(obj.pop())
print(obj.pop())
print(obj.pop())

#3如何实现一个可迭代对象？
# class Foo:
#     def func(self):
#         yield 1
#         yield 2
#         yield 3
# obj=Foo()
# for  i in obj.func():
#     print(i)
# class Foo:
#     def __iter__(self):
#         return iter([1,2,3,4])
# obj=Foo()
# for  i in obj:
#     print(i)

#4.看代码写结果
class Foo(object):

    def __init__(self):
        self.name = '武沛齐'
        self.age = 100


obj = Foo()
setattr(Foo, 'email', 'wupeiqi@xx.com')

v1 = getattr(obj, 'email')
v2 = getattr(Foo, 'email')

print(v1, v2)#wupeiqi@xx.com wupeiqi@xx.com


#5请补充代码（提：循环的列表过程中如果删除列表元素，会影响后续的循环，推荐：可以尝试从后向前找）


li = ['李杰', '女神', '金鑫', '武沛齐','女神1','女神11','女神111']
name = input('请输入要删除的姓氏：') # 如输入“李”，则删除所有姓李的人。
# 请补充代码
class Foo:

    def pop(self,name):
        l=[]
        self.name=name
        for i in li:
            if i.startswith(self.name):
                l.append(i)
        return set(li).difference(set(l))

        #return li

obj=Foo()
v=obj.pop(name)
print(list(v))


#6.有如下字典，请删除指定数据。
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


info = [User('武沛齐', 19), User('李杰', 73), User('景女神', 16)]

name = input('请输入要删除的用户姓名：')
# 请补充代码将指定用户对象再info列表中删除。

for i in range(len(info),0,-1):#3,2,1
    if info[i-1].name==name:
        info.remove(info[i-1])
    print(info[i-1].name)
print(info)
'''


#7.补充代码实现：校园管理系统。

class User(object):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return self.name


class School(object):
    """学校"""

    def __init__(self):
        # 员工字典，格式为：{"销售部": [用户对象,用户对象,] }
        self.user_dict = {}

    def invite(self, department, user_object):
        """
        招聘，到用户信息之后，将用户按照指定结构添加到 user_dict结构中。
        :param department: 部门名称，字符串类型。
        :param user_object: 用户对象，包含用户信息。
        :return:
        """
        pass

    def dimission(self, username, department=None):
        """
        离职，讲用户在员工字典中移除。
        :param username: 员工姓名
        :param department: 部门名称，如果未指定部门名称，则遍历找到所有员工信息，并将在员工字典中移除。
        :return:
        """
        pass

    def run(self):
        """
        主程序
        :return:
        """
        pass


if __name__ == '__main__':
    obj = School()
    obj.run()

