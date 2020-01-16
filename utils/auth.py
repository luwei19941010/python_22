#-*-coding:utf-8-*-
# Author:Lu Wei

import os,sys

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

class Base(object):
    def process(self):
        raise  NotImplementedError()


class AuthMiddleware(Base):
    def process(self):
        return 'auth'