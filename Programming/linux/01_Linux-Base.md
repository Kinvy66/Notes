# Linux基础



## 1.  Linux命令



### 1.1 重定向操作

```shell
echo  helloworld	#在终端输出helloworld
echo helloworld > tmp	#将helloworld写入到temp文件中，会覆盖文件中原有的内容
echo helloworld >> tmp  #以追加的方式添加内容
```



### 1.2  压缩和解压命令 tar

1. **压缩**

   tar只能打包文件，不能够压缩文件。压缩工具：`gzip` `bzip2` ,但是不能打包压缩文件，每个文件都会生成一个单独的压缩包，并且压缩之后不会保留原文件

   > 如果使用 `tar` 完成文件压缩，涉及的的参数如下，在使用过程中没有先后顺序
   
   * `c`: 创建压缩文件
   * `z`: 使用`gzip` 的方式进行文件压缩
   * `j`: 使用`bzip2` 的方式进行文件压缩
   * `v`: 压缩过程中显示压缩信息，可以省略不写
   * `f`: 指定压缩包的名字
   
   > 一般认为 `.tgz` 文件等同于 `.tar.gz` 文件，因此它们的压缩方式是相同的
   
   ```shell
   #语法
   $ tar [参数] [生成的压缩包的名字] [要压缩的文件（文件或目录）]
   
   #备注: 关于生成的压缩包的名字，建议使用标准后缀，方便识别
   #	  -压缩使用gzip方式， 标准后缀格式为： .tar.gz
   #	  -压缩使用bzip2方式，标准后缀格式为： .tar.bz2
   ```
   
   > 举例： 使用 `gzip` 的方式进行文件压缩
   
   ```shell
   $ tar czvf all.tar.gz tmp.txt  temp/  #使用gzip压缩文件
   $ tar cjvf all.tar.bz2 tmp.txt  temp/  #使用把bzip2压缩文件
   
   ```
   
   



2. **解压**

   > 如果使用`tar` 进行文件的解压缩，设计的参数如下，在使用过程中参数没有先后顺序

   * `x`: 释放压缩文件内容
   * `z`: 使用 `gzip` 的方式进行文件解压缩，压缩包后缀为`.tar.gz`
   * `j`: 使用`bzip2` 的方式进行文件解压缩，压缩包后缀为`.tar.bz2`

   * `v`: 解压缩过程中显示解压缩信息
   * `f`: 指定压缩包的名字

   > 使用以上参数是将压缩包解压到当前目录，如果需要解压到指定目录，需要指定参数 `-c`, 一般认为 `.tgz` 文件等同于 `.tar.gz` 文件，解压缩方式是相同的，解压缩的语法格式如下：

   ```shell
   #语法1： 解压到当前目录中
   $ tar [参数] [压缩包名]
   
   #语法2： 解压到指定目录中
   $ tar [参数] [压缩包名] -C [解压目录]
   ```

   > 举例：使用`gzip` 的方式进行文件压缩

   ```shell
   # 将 all.tar.gz 压缩包解压缩到 temp 目录中
   $ tar zxvf all.tar.gz -C temp
   
   ```
   
   > 举例：使用bzip2的方式进行文件解压缩
   
   ```shell
   # 将 part.tar.bz2 中的文件加压缩到 temp 目录中
   $ tar jxvf part.tar.bz2 -C temp
   
   ```



### 1.3 zip

> zip格式的压缩包在Linux中也是常见的，在某些版本中需要安装才能使用

Ubuntu中安装zip

```shell
$ sudo apt install zip		#压缩
$ sudo apt install unzip	#解压缩
```



1. **压缩（.zip）**

   > 使用 `zip` 压缩目录需要注意一点，必须添加参数 `-r` ，这样才能将子目录中的文件一并压缩，如果要压缩的文件中没有哦目录，该参数可以不写
   >
   > 另外使用 `zip` 压缩文件，会自动生产文件后缀`.zip` ，因此就不需要额外指定了

   ```shell
   #语法：
   $ zip [-r] [压缩包名] [要压缩的文件]
   ```

   > 举例

   ```shell
   # 压缩目录 get 和文件 onepiece.txt robin.txt 得到压缩包 all.zip(不需要指定后缀, 自动添加)
   $ zip all onepiece.txt robin.txt get/ -r
   ```

   

2. **解压缩（.zip）**

   > 对应 zip 格式的文件解压缩，必须要使用 unzip 命令，和压缩的时候使用的命令是不一样的。如果压缩包中的文件要解压到指定目录需要指定参数 -d, 默认是解压缩到当前目录中。

   ```shell
   # 语法1: 解压到当前目录中 
   $ unzip 压缩包名
   
   # 语法: 解压到指定目录, 需要添加参数 -d
   $ unzip 压缩包名 -d 解压目录
   
   ```

   > 举例

   ```shell
   
   # 将 all.zip 解压缩到 temp 目录中
   $ unzip all.zip -d temp/
   ```



### 1.4 rar

> `rar` 这种压缩格式在 Linux 中并不常用，这是 Windows 常用的压缩格式，如果想要在 Linux 压缩和解压这种格式的文件需要额外安装对应的工具，不同版本的 Linux 安装方式也是不同的。

Ubuntu安装rar

```shell
sudo apt install rar
```



1. **压缩（.rar）**

   > 使用 `rar` 压缩过程中的注意事项和 `zip` 是一样的，`如果压缩的是目录, 需要指定参 -r`, 如果只压缩文件就不需要添加了。压缩过程中需要使用参数` a (archive)`, 压缩归档的意思。
   >
   > `rar` 工具在生成压缩包的时候也会自动添加后缀，名字为`.rar`, 因此我们只需要指定压缩包的名字

   ```shell
   # 文件压缩, 需要使用参数 a, 压缩包名会自动添加后缀 .rar
   # 如果压缩了目录, 需要加参数 -r
   # 语法: 
   $ rar a 压缩包名 要压缩的文件 [-r]
   
   # 压缩文件 onepiece.txt, robin.txt 和目录 get/ 到要是文件 all.rar 中
   $ rar a all onepiece.txt get/ robin.txt -r 
   ```



2. **解压缩（.rar）**

   >解压缩`.rar `格式的文件的时候，可以使用`rar` 也可以使用 `unrar`, 操作方式是一样的，需要添加参数 `x`, 默认是将压缩包内容释放到当前目录中，如果要释放到指定目录直接指定解压目录名即可，不需要使用任何参数。

   ```shell
   # 解压缩: 需要参数 x
   # 语法: 解压缩到当前目录中
   $ rar/unrar x 压缩包名字
   
   # 语法: 解压缩到指定目录中
   rar/unrar x 压缩包名字 解压目录
   
   ```

   > 举例

   ```shell
   # 将 all.rar 中的文件解压缩到 temp 目录中
   $ rar x all.rar temp/ 
   ```

   



### 1.5  xz

> `.xz` 格式的文件压缩和解压缩都相对比较麻烦，通过一个命令是完不成对应的操作的，需要通过两步操作才行。并且操作过程中需要使用 `tar` 工具进行打包，压缩使用的则是 `xz` 工具。



1. **压缩（.tar.xz）**

   >创建文件的步骤如下，首先 将需要压缩的文件打包 `tar cvf xxx.tar files`, 然后再对打包文件进行压缩 `xz -z xxx.tar`, 这样我们就可以得到一个打包之后的压缩文件了。
   >
   >使用 `xz` 工具压缩文件的时候需要添加参数 `-z`
   
   ```shell
   # 语法:
   # 第一步
   $ tar cvf xxx.tar 要压缩的文件
   # 第二步, 最终得到一个xxx.tar.xz 格式的压缩文件
   $ xz -z xxx.tar
   
   ```
   
   > 举例
   
   ```shell
   # 将文件 onepiece.txt, robin.txt 和目录 get 打包到 all.tar 中
   $ tar cvf all.tar onepiece.txt robin.txt get/
   
   ```



2. **解压缩（.tar.xz）**

   >解压缩的步骤和压缩的步骤相反，需要先解压缩，然后将文件包中的文件释放出来。
   >
   >使用 `xz`工具解压需要使用参数 `-d`。

   ```shell
   # 语法:
   # 第一步： 压缩包解压缩, 得到 xxx.tar
   $ xz -d xxx.tar.xz
   # 第二步: 将 xxx.tar 中的文件释放到当前目录
   $ tar xvf xxx.tar 			
   
   ```

   ```shell
   # 将 all.tar.xz 解压缩, 得到 all.tar
   $ xz -d all.tar.xz 
   
   ```



## 2. vim的使用

### 2.1  vim的模式

在vim中一共有三种模式，分别是 `命令模式` ，`末行模式` ，`编辑模式` ，当我们打开vim之后默认进入的是命令模式

* 命令模式：在该模式下我们可以进行`查看文件内容`，`修改文件` ，`关键的搜索`等操作
* 编辑模式：在该模式下主要对文件内容进行修改和内容添加
* 末行模式：在该模式下可以进行 `执行Linux命令` ，`保存文件` ，`进行行跳转`，`窗口分屏` 等操作

