# -*- coding: UTF-8 -*-

import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'

conn = cx_Oracle.connect('STC/STC@localhost:1521/orcl')
curs = conn.cursor()
sql = 'select * from user1'
curs.execute(sql)

for result in curs:
    print(result)

curs.close()
conn.close()