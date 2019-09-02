## 近期内容梳理





### 制作docker镜像



https://blog.csdn.net/qq_32923745/article/details/80817395





docker search python-3.6-alpine



### alpine

https://blog.csdn.net/bbwangj/article/details/81088231

FROM python:3.6-alpine





\# 309544246384.dkr.ecr.cn-northwest-1.amazonaws.com.cn/python-3.6-alpine:init

RUN apk add python3-psycopg2 libpq-dev 

psycopg2==2.8.3

​    pip install psycopg2 && \

RUN apk add --no-cache update libpq && \

​    apk add --no-cache --virtual temp-apks gcc musl-dev python-dev postgresql-dev && \

​    apk del temp-apks

RUN apk upgrade && apk add --no-cache tzdata



### dockerfile

FROM python:3.6-alpine

RUN apk add gcc python-dev postgresql-dev musl-dev

COPY . .

RUN pip install -r requirements.txt -i  http://pypi.douban.com/simple/ --trusted-host pypi.douban.com



### 开始运行

docker run -ti 57a /bin/sh

### 删除镜像

docker image inspect --format='{{.RepoTags}} {{.Id}} {{.Parent}}' $(docker image ls -q --filter since=XXX) # XXX指镜像ID





1
然后根据根据TAG删除容器

docker rm REPOSITORY:TAG
1
补充
docker none镜像

有效的 none 镜像
Docker文件系统的组成，docker镜像是由很多 layers组成的，每个 layer之间有父子关系，所有的docker文件系统层默认都存储在/var/lib/docker/graph目录下，docker称之为图层数据库。

最后做一个总结< none>:< none> 镜像是一种中间镜像，我们可以使用docker images -a来看到，他们不会造成硬盘空间占用的问题（因为这是镜像的父层，必须存在的），但是会给我们的判断带来迷惑。

无效的 none 镜像

另一种类型的 < none>:< none> 镜像是dangling images ，这种类型会造成磁盘空间占用问题。

像Java和Golang这种编程语言都有一个内存区，这个内存区不会关联任何的代码。这些语言的垃圾回收系统优先回收这块区域的空间，将他返回给堆内存，所以这块内存区对于之后的内存分配是有用的

docker的悬挂(dangling)文件系统与上面的原理类似，他是没有被使用到的并且不会关联任何镜像，因此我们需要一种机制去清理这些悬空镜像。

我们在上文已经提到了有效的< none>镜像，他们是一种中间层，那无效的< none>镜像又是怎么出现的？这些 dangling镜像主要是我们触发 docker build 和 docker pull命令产生的。

使用下面的命令可以清理
docker rmi $(docker images -f “dangling=true” -q)
docker没有自动垃圾回收处理机制，未来可能会有这方面的改进，但是目前我们只能这样手动清理（写个脚本就好）。

### alpine修改镜像源

```bash
sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
```

```bash
sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
```

### 查看docker运行状况

docker inspect NAMES 
#### 查看容器所有状态信息；

docker inspect --format='{{.NetworkSettings.IPAddress}}' ID/NAMES
#### 查看 容器ip 地址

docker inspect --format '{{.Name}} {{.State.Running}}' NAMES

#### 容器运行状态

## docker部署项目

### 在项目下编写dockerfile

```dockerfile
FROM python:3.6-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk upgrade && apk add --no-cache tzdata
RUN apk add mysql-dev python-dev gcc postgresql-dev musl-dev
ENV TZ Asia/Shanghai
COPY  . .
RUN pip install -r requirements.txt -i  http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
EXPOSE 5000
ENV FLASK_CONFIG dev
CMD ["gunicorn", "--config", "gunicorn_config.py", "syncer:app", "--timeout", "7200"]
```

修改后，python-dev可能会覆盖python3

```dockerfile
FROM python:3.6-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk upgrade && apk add --no-cache tzdata
RUN apk add mysql-dev gcc postgresql-dev musl-dev
ENV TZ Asia/Shanghai
COPY  . .
RUN pip install -r requirements.txt -i  http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
EXPOSE 5000
ENV FLASK_CONFIG dev
CMD ["gunicorn", "--config", "gunicorn_config.py", "syncer:app", "--timeout", "7200"]
```



### 构建不包含代码的已装好的环境包

```dockerfile
FROM python:3.6-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk upgrade && apk add --no-cache tzdata
RUN apk add mysql-dev gcc postgresql-dev musl-dev
COPY requirements.txt .
ENV TZ Asia/Shanghai
RUN pip install -r requirements.txt -i  http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

docker run -itd -p 4321:5000 -v /C/Users/LvYangyang/Documents/docker_code/flask_test:/codes --name flask_base 461 /bin/sh

docker run -itd -p 4324:5000 -v /C/Users/LvYangyang/Documents/docker_code/flask_test:/codes --name py3_base 461 /bin/sh

### 注意



usr/local会覆盖python的link，因为/usr/local是很多命令的目录，尽量新建一个目录，而非系统目录

加 -p 4321:5000 可能会出现没有python3

docker run -itd -v /C/Users/LvYangyang/Documents/docker_code/flask_test:/codes --name flask_test6 95a /bin/sh

拉取python3+aphine

使用aphine，添加阿里镜像源

注意，pgsql驱动需要添加一些东西

使用豆瓣源安装python包

docker build命令，指定版本

### 后台启动容器的脚本

docker exec -it b6d python /codes/app.py 

可查看日志，但退出时，会关闭，可以用于调试

docker exec -itd b6d python /codes/app.py 

注意host指定0.0.0.0

### docker运行镜像

docker run -it -p 3000:5000 --name 容器名 镜像id 

如果想要后台运行

docker run -itd -p 3006:5000 --name d_sync 610

### 查找宿主机的ip

ipconfig或ifconfig

以太网适配器 vEthernet (DockerNAT):

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::409a:bea9:b3ed:53dc%15
   IPv4 地址 . . . . . . . . . . . . : 10.0.75.1
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . :

然后访问 10.0.75.1:3000即可

### 对docker进行操作

新开一个终端，docker exec -it 容器id /bin/sh 

注意命令

### 常用docker命令

| 命令                        | 功能 |      |
| --------------------------- | ---- | ---- |
| docker ps -a                |      |      |
| docker start xxx            |      |      |
| docker image ls -a          |      |      |
| docker image rm xxx         |      |      |
| docker image ls -a          |      |      |
| docker container ls -a      |      |      |
| docker container rm xxx     |      |      |
| docker run -it xxx          |      |      |
| docker exec -it xxx /bin/sh |      |      |
| docker stop xxx             |      |      |

可以看到Linux系统只有关联到本地C:\Users这个目录，其他的目录都找不到，那么我们就在这个目录下进行挂载操作

docker run -d -p 8888:8080 -v /c/Users/systemDir:/usr/local/log balance**



### 创建镜像，容器开发，挂载

docker run -dit -p 4321:5000 -v /C/Users/LvYangyang/Documents/docker_code/flask_test:/usr/local --name ft3 95a /bin/sh

## 在docker容器上如何实现代码的版本管理



   之前在一台centos7的虚拟机上部署了docker并运行了三个容器给开发写代码用，写代码肯定会涉及到版本控制管理。

开始建议是开发在容器中写代码，然后通过docker commit的方式将其保存为image，每次回滚的话是通过新的image重新运行一个镜像的方式，

现在开发觉得利用这种方式很麻烦，每次要commit，run，甚至还可以有一些stop，删除的操作。

在网上查询了一些方法在docker容器上实现代码的版本管理，如下：

1.将代码放在虚拟机的操作系统上，也就是放在docker容器的外部，然后通过-v的方式挂载在容器中，这样的话，在容器外部就可以直接使用git或者svn的方式进行代码的版本控制

## 代码是放在docker里好还是外面比较好

### 首答

 对于楼主的问题，我认为首先需要明确的是：Docker到底能够带来什么样的好处，Docker带来轻量级虚拟化容器方面的优势（资源利用率高，创建快捷，环境纯粹）？还是镜像带来的优势（便于部署，记录容器状态，持续集成等）？

将Docker的优势与楼主项目的性质进行综合，如楼主希望决定项目代码的放置位置。

根据我的理解，docker的外部，可以认为是和Docker没有任何关系。而Docker的内部，可以认为有两个维度，第一，Docker容器内部，第二，Docker的镜像image内部。

假如将用户的项目代码完全放在Docker外部，那么在由自身管理项目代码的时候，不可避免会遇到一个问题，如何在项目代码运行前放入Docker容器内部。一旦将项目代码迁入Docker容器内部，则可以直接将环境image与项目代码commit为一个新的image，以此image为模版，进行开发，迭代等。

所以我的观点是，项目代码通过Docker image的形式存储较为合适。  

### 二答

  放不放入docker这个概念优点不对，docker有镜像和容器区分。两者不一样的是放入镜像相当于模板，这会减低镜像的复用性。

我们team现在的做法是，代码不放入镜像，使用volume挂载放入容器。这样我的镜像只需要维护程序运行的环境，不同的项目运行不同的容器挂载不同的代码。我认为这种粒度比较合适。

[@shlallen](http://dockone.io/people/shlallen) 同学的做法会把代码的版本控制和镜像的版本控制耦合在一起。

如果我们是把源码编译后的内容（随不同语言平台而不同）挂载的方式放入容器，不放入镜像，那代码版本控制还可以继续使用git/svn来管理。

而代码checkout 编译 部署的过程业界有很成熟的方案，即使不想用这些工具也完全可以写个脚本搞定。

只有一种是例外的，那就是你使用开发的代码来直接搭建一个完整的服务，不想要对代码再继续修改。那这时候集成到镜像内是合适的。  



