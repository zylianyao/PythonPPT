# coding=utf-8
# 函数使用与返回值
# 函数调用
'''
函数的调用我们已经接触过了多次，要想调用一个函数，
在函数定以后，直接输一遍这个函数名即可，如果要传
递实参到函数里面执行，直接在调用的时候括号里面输
入实参即可。比如一个函数是def func3()：这样定
义的,那么我们调用它直接输入func3(参数)即可。其
中参数可以省略。
'''
def a():
    i = 1
a()
# 函数返回值
'''函数的返回值是通过return语句来实现的'''
# 一个返回值的情况
def test():
    i = 7
    return i
# print test()
# 多个返回值的情况
def test2(i, j):
    k = i * j
    return (i, j, k)
# x=test2(4,5)
# print x
y, z, m = test2(4, 5)
print y