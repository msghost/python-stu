#以下验证了精度问题
""" x = "aaabbbcccddd"
a = 0.1
b = 0.2

#print(id(x),'\n',type(x))
print('{:.200f}'.format(a+b)) """

#验证dir函数的使用
import math as mt
""" print(dir(mt)) """

#验证help的使用
""" print(help(mt.pow)) """

#验证append和extend的区别
""" a = [1,2,3]
b = ['a','b','c']
a.insert(1,b)
print(a)
a.sort()
a = ' '
a.join() """
""" print(id(a),id(b),id(b.apextend(a)))
print(a,b,b.extend(a)) """

#验证数字输出
""" b = int("022")
print(b)

aaa = '232323sdsdsd'
a = {'a':111,'b':222,333:aaa}
print(a[333]) """

#验证and
""" print(4>3 and 5>3) """

#range函数
""" print(range(0,10)) """

#测试for-else示例
""" from math import sqrt

for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

else:
    print("Nothing.") """

#测试打开文件
""" with open(r"c:/test/111.txt") as f:
    for ss in f:
        print(ss) """

#测试写入文件
""" with open(r"c:/test/2.txt","a") as ff:
    ff.write("test") """

#测试类:说明子类的继承关系，后者覆盖前者的同名属性、方法
""" 
class base(object):
    def base(self):
        print("this is base")

class b1(base):
    def b1(self):
        print("this is b1")
    def bb(self):
        print("this is bb-b1")

class b2(base):
    def b2(self):
        print("this is b2")
    def bb(self):
        print("this is bb-b2")

class test(b2,b1):
    pass

m = test()#此处需要先将类分配给一个对象变量再调用，直接调用test.base()会报错
m.bb() """


