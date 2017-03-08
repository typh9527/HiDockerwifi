import pymysql
import configparser

#:获取配置信息
config = configparser.ConfigParser()
config.read('db.ini')
host = config.get("Settings","host")
port = config.get("Settings","port")
user = config.get("Settings","user")
passwd = config.get("Settings","passwd")
db = config.get("Settings","db")
charset = config.get("Settings","charset")

def exec(sql):
    """
    执行sql命令
    """
    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd,db=db,charset=charset)
    cursor = conn.cursor()
    result =cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get(sql):
    """
    数据库查询命令
    """
    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd,db=db,charset=charset)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result

if __name__ == "__main__":
    print(get_port())


