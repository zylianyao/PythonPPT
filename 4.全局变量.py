# coding=utf-8
# 全局变量与局部变量


# 作用域
def func():
    i = 8


# print i
# print j
j = 9


# print j


# 局部变量
def func2(a):
    i = 7
    print i


i = 9


# func2(i)
# print i


# 全局变量
def func3():
    global i
    i = 7
    # print i


# i=9
func3()
i = 9
print i
