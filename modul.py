# coding=utf-8
# 分别直接执行这个模块与导入这个模块，看一下结果
print __name__
if __name__ == "__main__":
    print "This is main"
else:
    print "This is not main"
