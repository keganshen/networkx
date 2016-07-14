#coding=utf-8
'''
#map 函数
def f(x):
    print x[0].upper()+x[1:].lower()

map(f,['adam','LISA','barT'])


#filter 过滤序列
def is_su(n):
    counter=0
    if n >= 2:
        for i in range(n-2):
            if n%(i+1) == 0:
                counter += 1
        return  counter <= 1
    else:
        pass

uncheck = []
for i in range(100000):
    uncheck.append(i)

print len(filter(is_su,uncheck))

'''