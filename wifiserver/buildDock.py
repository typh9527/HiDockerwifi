import subprocess
import os
import db
import configparser

#:从配置信息中读取配置信息
config = configparser.ConfigParser()
config.read('db.ini')
ftphost = config.get("FTP","host")
registry_host = config.get("Registry","host")

def pulldc(imname):
    """
    从私有库拉去镜像
    """
    full_imname = registry_host + '/' + imname
    cmd = "docker pull " + full_imname
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        print("pull from registry success!")
        return True
    else:
        print("pull from registry failed!")
        return False

def checkdc(equip):
    """
    检查是否存在已equip为名字的容器应用
    """
    #:查看全部应用
    cmd = r"docker ps -a | awk '{print $NF}' | sed 1d | sort"
    (status,output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        dockers = output.split('\n')
        #:返回是否存在
        if equip in dockers:
            return True
        else:
            return False
    else:
        print("cmd is not running!")
        return False

def checkim(imname,force=False):
    '''
    检查是否存在该镜像
    '''
    #:force为真强制不检查镜像
    if not force:
        #:获取全部的镜像
        cmd = r"docker images | awk '{print $1}' | sed 1d |sort"
        (status,output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            images = output.split('\n')
            if imname in images:
                print("image exists!")
                return True
            else:
                return False
        else:
            return False
    else:
        print("cmd is not running!")
        return False

def build(repo,imname):
    """
    使用dockerfile构建容器
    """
    repo = '112.74.171.161/' + repo
    if os.path.isdir(repo):
        cmd = "docker build -t "+imname+" "+repo
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            print("build success!")
            return True
        else:
            print("build failed")
            print(output)
            return False

def load(repo):
    '''
    加载镜像
    '''
    #:下载目录
    repo = str(ftphost) + '/' + repo + '.tar'
    #:判断是否存在
    if os.path.isfile(repo):
        cmd = "docker load < " + repo
        (status,output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            print("load success!")
            return True
        else:
            print("load failed!")
            print(output)
            return False

def download(repo):
    """
    从FTP服务器下载镜像
    """
    #:判断是否已经下载过该镜像
    if not os.path.exists(str(ftphost) + '/' + repo + '.tar'):
        cmd = "wget -r --no-passive-ftp ftp://uftp:WyrXa9@" +str(ftphost)+ "/" + repo + '.tar'
        (status, output) = subprocess.getstatusoutput(cmd)
        if status == 0:
            print("download success!")
            return True
        else:
            print("download failed!")
            return False
    else:
        print("download successed before!")
        return True

def run(imname,equip,dcport,rec_cmd):
    """
    启动容器
    """
    #:提取未使用的端口
    sql = "select port from portdb where status=0 limit 1"
    hostport = db.get(sql)
    #:应用启动命令
    cmd = "docker run -it --name " + equip + " -d -p " + str(hostport) + ":" + dcport + " -P --link=mysql_server:webdb " + imname + " " + rec_cmd
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        print("docker is running!")
        #:将端口号标记为占用
        sql = 'update portdb set status=1,equip="'+equip+'"  where port='+str(hostport)
        db.exec(sql)
        #:返回执行结果和端口号
        flag = [True,hostport]
    else:
        print("docker cannot run!")
        flag = [False,hostport]
    return flag

def start(equip):
    """
    启动容器
    """
    cmd = "docker start " + equip
    (status,output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        print("docker is running!")
        sql = 'select port from portdb where equip="'+equip+'"'
        hostport = db.get(sql)
        flag = [True,hostport]
    else:
        print("docker cannot run!")
        flag = [False,None]
    return flag

if __name__ == "__main__":
    print(checkim("resin/armv7hf-debian"))

    #download("joliu/debian")
    #load("joliu/debian")
    #build("joliu","jo/mysqll")

