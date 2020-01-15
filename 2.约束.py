#-*-coding:utf-8-*-
# Author:Lu Wei
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