# coding=utf-8
import const

# java中注解使用 //
# java中使用final关键字
# final int STATIC_VAR=5
# java是编译型语言所以IDE可以实现在编写代码时就提醒错误【编译时就会检查错误】
# 而python是解释型语言，得运行时才会抛出异常
const.STATIC_VAR = 5
print const.STATIC_VAR
#const.STATIC_VAR = 6  # 这一行会抛出异常

# 变量声明与java的区别
# java中声明变量必须声明变量的类型 如 int i=6;
i = 6

# java中变量的类型不能变化【不能把int赋值给String】而python则可以
i = "一二三"

# 通过序列解包(sequence unpacking)可以将多个值的序列解开，让后一一放置到变量的序列中。
# 解包的序列中的元素必须和等号左边变量数量一致。
values = "1", 2, True#生成的是一个元组【后面会介绍】

print values  # output: (1, 2, 3)
print values[0]
x, y, z = values  # output: 1 2 3
bob_Info = {'name': 'Bob', 'email': 'bob@gmail.com'}
key, value = bob_Info.popitem()
print value  # output: Bob
# 通过使用链式赋值(chained assignment)可以将一个值同时赋给多个变量
x = y = z = 1
print x, y, z  # output: 1 1 1
