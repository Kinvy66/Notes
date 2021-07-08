# Issues



## 1. ubuntu 安装gcc,g++

```shell
sudo apt install build-essential 
```



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

   

