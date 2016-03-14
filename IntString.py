# coding=utf-8
# 变量
# java 中基本类型是值传递，赋值时并不会新建对象
# java 中 String 和 python String一样时不可变的
i = 100
print id(i)  # 通过Python id 函数可以查看基本PyObject标识的变更方式
print i
i = 101
print id(i)
print i
# 复数  java中没有此类型
num = -8.222 - 1.34j
print num.real  # num.real	该复数的实数部分
print num.imag  # num.imag	该复数的虚数部分
print num.conjugate()  # num.conjugat()	返回该复数的共轭算数
# 字符串
# java中字符串只可使用双引号声明
# 单引号
c1 = '2ght'
print id(c1)
print c1
# 下面的语句在java中需要使用转义
c2 = 'It is a "dog"!'
print c2
# 双引号
c1 = "2ght11"
print id(c1)
print c1
c2 = "It's a dog!"
print c2
# java要实现该代码较为复杂且可读性较差
c1 = '''三引号
声明的字符串
会保留换行
    也会保留缩进'''
print c1
c2 = """三引号
双引号也可以
声明的字符串
会保留换行
    也会保留缩进"""
print c2
# 字符串拼接
str = "one" + "123" + "456"
print str
# str="one"+"123"+
#     "456"这种写法是错误的
# \用于代码换行时的拼接
# java中没有编译时会自动将物理行转换为逻辑行所以使用+即可并无此特性
one = "第一次" \
      "第二次"
print one
# 子字符串
# 索引运算符从0开始索引
# 切片运算符[a:b]是指从第a下标开始到第b-1下标。同样第一位的下标为0.
str = '0123456789'
print "str[7] %s" % str[7]
print "str[0:3] %s" % str[0:3]  # 截取第一位到第三位的字符
print "str[:] %s" % str[:]  # 截取字符串的全部字符 java中不支持默认值，所以没有该对应的方法
print "str[6:] %s" % str[6:]  # 截取第七个字符到结尾
print "str[:-3] %s" % str[:-3]  # 截取开始到倒数
print "str[-1] %s" % str[-1]  # 截取倒数第一个字符
print "str[::-1] %s" % str[::-1]  # 倒序 java中反转字符需要自行编写方法实现
print "str[-3:-1] %s" % str[-3:-1]  # 截取倒数第三位与倒数第一位之前的字符
print "str[-3:] %s" % str[-3:]  # 截取倒数第三位到结尾
print "str[:-5] %s" % str[:-5]  # 逆序截取
print "str[:-5:-3] %s" % str[:-5:-3]  # 逆序截取
# 去空格及特殊符号
# strip(rm)删除s字符串中开头、结尾处，位于 rm删除序列的字符，默认为空格。
# lstrip(rm)删除s字符串中开头处，位于 rm删除序列的字符
# rstrip(rm)删除s字符串中结尾处，位于 rm删除序列的字符
s = " 12313 "
print s
print s.strip()#对应java.trim()单java中不可传参
s = ",12313,"
print s
print s.lstrip(",")#java API没有对应方法
print s.rstrip(",")#java API没有对应方法
# str -- 分隔符，默认为空格。
# num -- 分割次数。
str = "#Line1-abcdef #Line2-abc #Line4-abcd";
print str.split()#java中有对应方法只是没有默认参数
print str.split(' ', 1)
# 字符串的重复
str = "字符串的重复\n" * 20#java中不支持此特性需要循环实现
print str
# 转义符
print 'It\'s a dog!'
print "hello boy\nhello boy"
# 自然字符串
print "hello boy\nhello boy"
print r"hello boy\nhello boy"  # java中则是\\n来实现
# 其他API可以自行查询
