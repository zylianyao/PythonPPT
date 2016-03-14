# coding=utf-8
#逻辑行与物理行

#以下是3个物理行
print "abc"
print "789"
print "777"

#以下是1个物理行，3个逻辑行
print "abc";print "789";print "777"

#以下是1个逻辑行，3个物理行
print '''逻辑行
一行
物理行
三行！'''
