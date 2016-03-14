# coding=utf-8
# pickle腌制
import pickle

# dumps(object)将对象序列化
lista = ["mingyue", "jishi", "you"]
listb = pickle.dumps(lista)
# print listb

# loads(string)将对象原样恢复，并且对象类型也恢复为原来的格式
listc = pickle.loads(listb)
# print listc

# dump(object,file),将对象存储到文件里面序列化
group1 = ("bajiu", "wen", "qingtian")
# file是python中IO操作的模块 wb 代表写 rb 代表读
f1 = file('1.pk1', 'wb')
pickle.dump(group1, f1, True)
f1.close()

# load(object,file)将dump()存储在文件里面的数据恢复
f2 = file('1.pk1', 'rb')
t = pickle.load(f2)
print t
f2.close()
