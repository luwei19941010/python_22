#-*-coding:utf-8-*-
# Author:Lu Wei

import os,sys,importlib

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

class Base(object):
    def process(self):
        raise  NotImplementedError()


class CrsfMiddleware(object):
    def process(self):
        print('1233')
        return 'csrf'
