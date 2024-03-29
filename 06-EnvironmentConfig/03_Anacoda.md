## 6. Anaconda

### 1. 更新

```shell
$conda update --all  #更新所有的库

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
```



### 2. 虚拟环境创建

```shell
$ conda create -n flask-env python=3.8 #创建flask-env的环境
$ conda activate flask-env	#激活进入环境
$ pip install packge-name	#在环境中安装包
$ conda deactivate 			#退出虚拟环境
$ conda remove --name $your_env_name  $package_name   #删除环境
conda remove --name d2l --all

$conda env create -f environment.yaml
```



### 3. 在Ubumtu中使用Anacoda

- 安装

  ```shell
  # Path是自定义安装路径
  $ bash Anaconda3-2021.11-Linux-x86_64.sh -p [Path] -u 
  ```



- 配置

  ```shell
  #conda不作为默认的终端，即命令行前面不会有base
  $ conda config --set auto_activate_base false
  #在终端中进入conda
  $ conda activate
  #退出终端
  $ conda deactivate
  ```

  

```shell
$ pip install d2l -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```



### 4. 修改安装源

清华源: `~/.condarc`

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

