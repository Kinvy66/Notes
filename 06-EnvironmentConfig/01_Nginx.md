# Nginx 安装

参考：[How To Install Nginx on Ubuntu 18.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)



## 0. 环境

- 服务器： 腾讯云轻量服务器（CPU: 1核 内存: 2GB)
- 系统： Ubuntu18，软件源默认为腾讯



## 1. 安装

软件源建议使用国内的

- 更新软件包

  ```shell
  $ sudo apt update
  ```



- 安装nginx

  ```shell
  $ sudo apt install ngin



## 2. 防火墙设置

在服务器的控制台中添加下面两个端口（腾讯云的轻服务器是默认打开的）

![image-20211214105332690](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211214105332690.png)



- 查看是否打开

  ```shell
  $ sudo ufw app list
  ```

  正常的应该输出：

  ```shell
  #Output
  Available applications:
    Nginx Full
    Nginx HTTP
    Nginx HTTPS
    OpenSSH
  ```



## 3. 测试Web服务

- 检查Nginx是否运行

  ```shell
  $ systemctl status nginx
  ```

  输出:

  ```shell
  ● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2021-12-14 10:36:42 CST; 22min ago
       Docs: man:nginx(8)
   Main PID: 21412 (nginx)
      Tasks: 2 (limit: 2157)
     CGroup: /system.slice/nginx.service
             ├─21412 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             └─21414 nginx: worker process
  ```

  ==active (running)== 表示Nginx在运行



* 通过浏览器访问

  在浏览器输入服务器的ip地址

  ```shell
  http://your_server_ip
  ```

  安装成功，并且启动Nginx,你输入ip地址后应该出现下面的页面

  ![image-20211214110354360](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211214110354360.png)

## 4. 管理Nginx进程

- 停止Nginx

  ```shell
  $ sudo systemctl stop nginx
  ```



- 启动Nginx

  ```shell
  $ sudo systemctl start nginx
  ```



- 重启Nginx

  ```shell
  $ sudo systemctl restart nginx
  ```



- 修改了Nginx的配置后，可以使用下面的命令重新加载配置，而不需要重启

  ```shell
  $sudo systemctl reload nginx
  ```



- Nginx默认是自动启动的，如果不想让Nginx自启可以使用下面命令关闭自启

  ```shell
  $ sudo systemctl disable nginx
  ```

  关闭自启后，需要再次打开自启，使用

  ```shell
  $ sudo systemctl disable nginx
  ```

  

## 5. 配置Nginx

- 创建静态文件存放目录

  ```shell
  #your_domain 换成自己的项目名称
  $sudo mkdir -p /var/www/your_domain/html
  ```

  > Nginx的静态文件目录默认放在 `/var/www` ，放在其他路径也可以的，只需配置是指定相应的路径
  >
  > 需要将项目打包的静态资源文件放到`/var/www/your_domain/html` 文件夹下



- 更改静态文件的拥有者和群组

  ```shell
  $ sudo chown -R $USER:$USER /var/www/your_domain/html  # -R 表示递归子文件和目录
  ```



- 修改静态文件权限

  ```shell
  $sudo chmod -R 755 /var/www/your_domain
  ```



- 创建配置文件

  ```shell
  $ sudo vim /etc/nginx/sites-available/your_domain  
  ```

  your_damiain的内容：

  ```json
  server {
          listen 80;
          listen [::]:80;
  
          root /var/www/your_domain/html;
          index index.html index.htm index.nginx-debian.html;
  		
  		#写域名或者ip（没有域名的情况）
  		#示例表示可以通过 your_domain.com和www.your_domain 地址访问
          server_name your_domain.com www.your_domain;
  
          location / {
                  try_files $uri $uri/ =404;
          }
  }
  ```

  > 以上配置需要修改的部分：
  >
  > - root ， 改成自己的静态文件的存放路径
  > - server_name， 服务器配置的域名或是ip地址



- 创建软链接

  ```shell
  $sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
  ```

  > Nginx的配置文件 `/etc/nginx/nginx.conf` 会自动包含`/etc/nginx/sites-enabled/*` 
  >
  > 所以要把我们写的配置文件创建一个软链接放到该目录下



- 重启Nginx

  ```shell
  #重启之前先检查配置文件是否有错误
  $ sudo nginx -t
  $ sudo systemctl restart nginx
  ```

  

- 最后在浏览器中输入配置的域名或是ip就可以访问服务器中的静态资源









 





















































