# coding=utf-8
# java中List、数组对应的内容
# 列表
students = ["小明", "小华", "小李", "小娟", "小云"]
print students[3]
students[3] = "小月"
print students[3]
# 元组java中没有内置对应的数据结构
studentsArray = ("小明", "小军", "小强", "小武", "小龙")
print studentsArray[1]
# studentsArray[1] = "小云"  # 这行会报错 元组不允许修改
print studentsArray[1]
#java中set接口
a = set("abcnmaaaaggsng")
b = set("cdfm")
print a  # 会自动去重
print b
# 交集
x = a & b
print x
# 并集
y = a | b
print y
# 差集
z = a - b
print z
# 去除重复元素
new = set(a)
print new
# 字典
k = {"姓名": "韦玮", "籍贯": "桂林"}
print k["籍贯"]
# 添加字典里面的项目
k["爱好"] = "音乐"
print k["姓名"]
print k["爱好"]
