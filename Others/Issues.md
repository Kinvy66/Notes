# Issues



## 1. ubuntu 安装初始环境配置

1. 换源 Ubuntu20.04源,  `\etc\apt\sources.list`

   ```shell
   #阿里源
   deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
   deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
   deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
   deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
   deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
   deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
   deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
   deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
   deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
   deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
   
   #中科大源
   deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
   deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
   deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
   deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
   deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
   deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
   deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
   deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
   deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
   deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
   
   #163源
   deb http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
   deb http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
   deb http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
   deb http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
   deb http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
   deb-src http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
   deb-src http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
   deb-src http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
   deb-src http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
   deb-src http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
   
   ```

2. 基础软件安装

   ```shell
   $sudo apt-get update		#更新源
   $sudo apt-get upgrade		#更新软件
   $sudo apt-get install openssh-server	#安装ssh
   $sudo apt install build-essential 		#安装gcc，g++
   ```

3. 其他软件安装

## 2. Debian  tab命令补全

Debian 默认不带命令补全的插件

* 安装补全插件

  ```shell 
  sudo apt-get install bash-completion
  ```

* 在 `/etc/profile` 或 `~/.bash_profile` 添加以下配置

  ```shell
  if [ -f /etc/bash_completion ]; then
  ./etc/bash_completion
  fi
  ```

  



## 3. Unix环境高级编程（第三版）环境配置

系统： wsl2 ubuntu18

1. [下载源码](http://www.apuebook.com/src.3e.tar.gz)

2. 解压文件

   ```shell
   $ tar -zxvf *.tar.gz
   $ cd apue.3e/
   ```

3. make

   ```shell
   $ sudo apt-get install libbsd-dev   #先安装库
   $ make
   ```

4. 将编译的库复制到系统库

   ```shell
   $ sudo cp ./include/apue.h /usr/include/
   $ sudo cp ./lib/libapue.a /usr/local/lib/
   ```

5. 示例

   ```c
   #ls.c
   #include "apue.h"
   #include <dirent.h>
   
   int main(int argc, char *argv[])
   {
       DIR *dp;
       struct dirent *dirp;
   
       if (argc != 2)
       {
           err_quit("usage: ls directory_name");
       }
       if((dp = opendir(argv[1])) == NULL)
           err_sys("can't open %s", argv[1]);
   
       while ((dirp = readdir(dp)) != NULL)
       {
           printf("%s\n",dirp->d_name);
       }
   
       closedir(dp);
   
       exit(0); 
   }
   ```

   ```shell
   gcc ls.c -o ls -lapue	#编译时链接apue库
   ```

   

## 4. Jupyter设置主题

安装主题

```shell
$ pip install jupyterthemes
```

查看可用主题

```shell
$ jt -l
$ jt -r  #恢复默认
```

更换主题，[详细参数设置](https://github.com/dunovank/jupyter-themes)

```shell
jt -t grade3 -f source -fs 12 -cellw 90% -ofs 11 -dfs 11 -T -N
```



