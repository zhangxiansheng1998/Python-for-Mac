import pymysql

# 终端启动mysql命令 brew services start mysql
connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='ni147258',
    db='mysql',
    charset='utf8')  # 目标主机为本地IP地址，端口3306，账号root，密码mysql，连接的数据库名为test，编码为utf-8

cur = connect.cursor()  # 建立游标，有了游标才能操作数据库[游标类似文件句柄，可以逐条访问数据库执行结果集。pymysql中只能通过游标来执行sql和获取结果]

cur.execute("select * from user where User='root'")  # 查询操作
res1 = cur.fetchall()  # 查询数据库（读）,cur.fetchall()获取结果，fetchall获取所有结果
print(res1)

#cur.execute("update course set name='python' where id=1")
#connect.commit()  # 提交、更改（写）,注意提交用的是connect.commit(),而不是cur.commit（）

#cur.execute("select * from course where id=1")  # 执行查询语句
#res2 = cur.fetchall()
#print(res2)

cur.close()
connect.close()
