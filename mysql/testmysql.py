"""

mysql测试

"""

import mysql.connector
cnx = mysql.connector.connect(
    user = 'root',
    password = '1234',
    host = '59.108.67.5',
    database = 'cucbm'
)
cnx.close()
