#MySQL数据库应用
##基于Arm架构的Docker镜像

###使用方法

`docker run --name mysql_server -d -P -p <hostport>:3306 hiwifi/mysql`

###备注

启动容器后需进入容器内，修改`/etc/mysql/my.cnf`注释掉bind-address =127.0.0.1`,否则其他容器无法访问该数据库


