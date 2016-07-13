#coding=utf-8

'''
_metaclass_=type # 确定使用新式类
class calculator:

    def count(self,args):
        return 1

calc=calculator() #自定义类型

from random import choice
obj=choice(['hello,world',[1,2,3],calc]) #obj是随机返回的 类型不确定
print type(obj)
print obj.count('a') #方法多态
'''

# human -> male -> boy
# human -> female -> girl
class human(object):
    def __init__(self,name):
        self.name = namewe
    def introduce(self):
        print '%s' " is a human" %(self.name)

class male(human):
    def introduce(self):
        print '%s' " is a man" %(self.name)

class boy(male):
    def introduce(self):
        print '%s' " is a boy" %(self.name)

class female(human):
    def introduce(self):
        print '%s' " is a woman" %(self.name)

class girl(female):
    pass



def who(people):
    people.introduce()
    people.introduce()

who(girl('Kegan'))
