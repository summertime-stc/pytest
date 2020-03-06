# -*- coding: UTF-8 -*-
import pymysql
import json
import os

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='stc13858449075',
    database='test',
    charset='utf8')

# cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  # 执行完毕返回的结果集以字典集显示


#查询
sql = "select tname,tage from user"
res = cursor.execute(sql)
# print res
# ret1 = cursor.fetchone()  # 取一条
# print ret1
# ret2 = cursor.fetchmany(10)  # 取10条
# print ret2
rows = cursor.fetchall()
print rows
print '1------------'

for result in rows:
    # print result.has_key('tname')
    # print result
    print result.keys()
    print 'tname' in result.keys()
print '2------------'
json1 = json.dumps(rows)
print json1

print '3------------'
a = json.loads(json1)
print a[0]['tname']

print '4------------'


# result2 = [(tname,tage) for tname,tage in rows]
# print result2


# 更新
# sql = "update userinfo set pwd=%s where user=%s;"
# 拼接并执行SQL语句
# cursor.execute(sql, ["july", "july"])
# conn.commit()

# 删除
# sql = "delete from userinfo where user=%s;"
# name = "june"
# 拼接并执行SQL语句
# cursor.execute(sql, [name])
# conn.commit()

#增加
# sql = "insert into userinfo (user, pwd) values (%s, %s);"
# name = 'wuli'
# pwd = '123456789'
# cursor.execute(sql, [name, pwd])
# conn.commit()
# 获取最新的那一条数据的ID
# last_id = cursor.lastrowid
# print("最后一条数据的ID是:", last_id)

cursor.close()
conn.close()