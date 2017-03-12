#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import socketserver
import json, types,string
import os, time

import buildDock
import db

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    路由器监听程序
    负责监听设备接入请求，部署应用
    """
    def handle(self):
        data = self.request.recv(1024).decode()
        jdata = json.loads(data)
        print("Receive data from '%r'"% (data))
        print("Receive jdata from '%r'"% (jdata))
        #:设备唯一编码
        rec_equip = jdata[0]['equip']
        #:设备接入请求，判断不同业务
        rec_log = jdata[0]['log']
        #:代码库
        repo = jdata[0]['repo']
        #:镜像名
        imname = jdata[0]['imname']
        #:应用端口
        dcport = jdata[0]['dcport']
        #:应用启动预执行命令
        rec_cmd = jdata[0]['cmd']

        #:设备注册流程
        if rec_log == 'up':
            #:标记用户为接入但未部署应用
            status = 0
            #:接入时间
            timel = str(time.time()).split('.')[0]
            print("new equip:"+rec_equip)
            #:在数据库中注册设备
            sql = "insert into equipdb (equip,status,signintime,dockername) values ('" + rec_equip +"'," + str(status)+","+str(timel)+",'"+imname+"')"
            db.exec(sql)
            #:标记设备登录成功
            log_ans = True
            #:检查本地镜像库是否已经存在该镜像
            if not buildDock.checkim(imname):
                if buildDock.pulldc(imname):
                    flag = buildDock.run(imname,rec_equip,dcport,rec_cmd)
                    if flag[0]:
                        cmd_ans = True
                    else:
                        cmd_ans = False
                else:
                    cmd_ans = False

#以下为使用ftp下载的命令            
#                #:下载镜像
#                if buildDock.download(repo) and log_ans:
#                    #:载入镜像
#                    if buildDock.load(repo):
#                        #:运行镜像
#                        flag = buildDock.run(imname,rec_equip,dcport,rec_cmd)
#                        #:判断运行是否成功
#                        if flag[0]:
#                            cmd_ans = True
#                        else:
#                            cmd_ans = False
#                    else:
#                        cmd_ans = False
#                else:
#                    cmd_ans = False

            else:
                #:检查是否已经创建过应用
                if buildDock.checkdc(rec_equip):
                    #:若存在应用，则启动容器，不创建
                    flag = buildDock.start(rec_equip)
                    #:判断启动结果
                    if flag[0]:
                        cmd_ans = True
                    else:
                        cmd_ans = False

                else:
                    #:创建并启用容器
                    flag = buildDock.run(imname,rec_equip,dcport,rec_cmd)
                    #:判断启动结果
                    if flag[0]:
                        cmd_ans = True
                    else:
                        cmd_ans = False

        #:该请求未完成，暂不使用    
        elif rec_log == 'in':
            status = 1
            timel = 1
            sql = 'update equipdb set status=1 where equip="'+rec_equip+"'"
            db.exec(sql)
            log_ans = True
            if builDock.start(rec_equip) and log_ans:
                cmd_ans = True
            else:
                cmd_ans = False
        else:
            log_ans = False
            cmd_ans = False
 
        cur_thread = threading.current_thread()
        #:构建json消息
        response = [{'equip':rec_equip,'log_ans':log_ans,'cmd_ans':cmd_ans,'port':flag[1]}]

        jresp = json.dumps(response)
        self.request.sendall(jresp.encode())
           
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    #:设置host和port 
    HOST, PORT = "0.0.0.0", 22223
    
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    #:启动多进程监听服务
    server_thread = threading.Thread(target=server.serve_forever)
    #:当主进程中断时退出程序
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:"+ server_thread.name)
    print( " .... waiting for connection")

    #:使用Ctrl + C退出程序
    server.serve_forever()
