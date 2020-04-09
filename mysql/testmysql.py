"""

mysql测试

"""

import mysql.connector
from mysql.connector import errorcode

# 连接数据库
try:
    cnx = mysql.connector.connect(
        user='root',
        password='1234',
        host='59.108.67.5',
        database='cucbm'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something wrong with your password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
else:
    query = "select * from dingqibaosong"
    cursor = cnx.cursor()
    cursor.execute(query)
    for cur in cursor:
        print(cur)

    cursor.close()
    cnx.close()
# print(cursor)


