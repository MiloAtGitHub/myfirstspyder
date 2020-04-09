"""
mysql测试
"""
import mysql.connector
from mysql.connector import errorcode


def connect_mysql(host, database, user, password, table):
    """
    这就是所谓的docstring？
    """
    # 连接数据库
    try:
        cnx = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something wrong with your password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
        cursor.execute("show tables")
        table_lists = cursor.fetchall()
        for table_list in table_lists:
            print(table_list)
        query = "select * from %s" % table
        cursor.execute(query)
        curs = cursor.fetchall()
        cursor.close()
        cnx.close()
        return curs


def main():
    """
    打印表
    """
    rows = connect_mysql(host='59.108.67.5', user='root', password='1234', database='cucbm', table='dingqibaosong')
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
