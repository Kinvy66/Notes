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

  

