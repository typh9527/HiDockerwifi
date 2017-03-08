FROM resin/armv7hf-debian:latest
    MAINTAINER JoLiu"joliu@s-an.org"
    RUN apt-get update &&\
        apt-get install -y mysql-server
    RUN service mysql start &&\
        mysql -e"grant all privileges on *.* to 'root'@'%' identified by 'letmein';"&&\
        mysql -e"grant all privileges on *.* to 'root'@'localhost' identified by 'letmein';"&&\
        mysql -u root -pletmein -e"show databases;"
    EXPOSE 3306
    CMD ["/usr/bin/mysqld_safe"]

