# -*- coding: UTF-8 -*-

import os
import test2
import json

counter = 100
miles = 1000.0
name = "John"
print ("hello")
print name[1:3]
print name[1:]
print name[:3]
print name[0]
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list[1]
print list+tinylist

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple+tinytuple

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
del dict[2]
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']
print tinydict
print tinydict.keys()
print tinydict.values()
print dict
print dict.keys()
print dict.values()

a = 10
b = 20

if a and b:
    print 'tt'
else:
    print 'xx'
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
else:
    print 'count=9'

for letter1 in 'Python':
    print 'zm', letter1

fruits = ['banana', 'apple', 'mango']
for fruit1 in fruits:
    print 'sg', fruit1

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '水果 :', fruits[index]

print '-----------'
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

# 打开一个文件
fo = open("D:\\fofo.txt", "w")
print "文件名: ", fo.name
fo.write( "www.runoob.com!\nVery good site!\n")
# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position
# 关闭打开的文件
fo.close()

fo1 = open("D:\\fofo.txt", "r+")
str = fo1.read()

print "读取的字符串是 : \n", str
position = fo1.seek(0, 0)
str2 = fo1.read()
print "读取的字符串是 : \n", str2
# 关闭打开的文件
fo1.close()




"创建 Employee 类的第一个对象"
emp1 = test2.Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = test2.Employee("Manni", 5000)
emp1.age = 7  # 添加一个 'age' 属性
emp1.displayEmployee()
emp2.displayEmployee()

print emp1.age
print "Total Employee %d" % test2.Employee.empCount

print '判断值是否存在有字典中----------------------'
xx={'name':'dfdf',3:'efef','efef':'ewewe'}
print 'name' in xx.keys()
print 'dfdf' in xx.values()

print '字典转json---------------------------------'
json1 = json.dumps(xx)
print json1

print 'json文件读取--------------------------------'
file1 = open('x1.json','r')
jsontxt = json.load(file1)
print jsontxt

print 'json解析------------------------------------'
# print jsontxt['web']
print jsontxt['translation'][len(jsontxt['translation'])-1]
print jsontxt['basic']['us-phonetic']
print jsontxt['basic']['explains'][0]
print jsontxt['web'][0]['key']
print jsontxt['web'][0]['value'][0]
