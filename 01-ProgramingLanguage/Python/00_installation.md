# 环境安装



python的开发环境有比较多的组合方式，这里介绍两种方式。第一种使用python+vscode，这个适合初学者写一些简单的练习代码；第二种是anaconda+pycharm，这种方式适合写一些比较大的工程项目。如果是初学的话建议是用vscode。接下来，具体介绍第一种方式的环境配置，第二的环境配置会在后续的项目实践中在详细介绍。



## 1. 软件下载

* python [下载](https://www.python.org/downloads/)，注意，Python3.9+的版本是不支持win7系统，所以如果你的是win7系统或是写的程序需要在win7的系统运行，建议下载python3.8或是以下的版本

* vscode[官网下载](https://code.visualstudio.com/Download)，选择自己对于的系统版本，本教程是以windows系统为例

  vscode下载通常会比较慢，我们可以把下载 链接替换成国内的源，具体操作如下

  首先，我们点击下载之后，打开下载管理器，复制下载的链接

  ![image-20210930170622168](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930170622168.png)

  将复制的链接粘贴到一个文本中，替换原链接的前面的部分，替换部分为 

  `https://vscode.cdn.azure.cn/` ，图中替换后的下载地址：https://vscode.cdn.azure.cnt/stable/7f6ab5485bbc008386c4386d08766667e155244e/VSCodeUserSetup-x64-1.60.2.exe

  ![image-20210930171136674](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930171136674.png)

  

  将替换后的链接直接粘贴到浏览器的地址栏就可以下载了，下载速度一般可以跑满宽带的。



## 2. 软件安装



### 2.1 python安装

1. 双击python安装包

   ![image-20210930214351814](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930214351814.png)

2. 安装选项，将 `1` 中的两个框都勾选上，然后选择 `2` 

   ![image-20210930214657011](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930214657011.png)



3. 这步的勾选的选项如下，默认是这个的，点击`Next`

   ![image-20210930214835943](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930214835943.png)

   

4. 勾选前几个，安装路径可以自定义路径，建议安装到 `C:\Python`下或是自定义一个其他路径，然后点击`Install`开始安装

   ![image-20210930215606713](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930215606713.png)

5. 开始安装

   ![image-20210930215635422](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930215635422.png)

6. 安装完成，退出

   ![image-20210930215729422](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930215729422.png)

   

7. 测试安装是否成功，按 `win`+ `r` 键，输入 `cmd` 打开命令提示符，输入 `python -V`,如果显示出了安装的python版本则表示安装成功。

   ![image-20210930220052959](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930220052959.png)

   

### 2.2 安装vscode

1. 双击vscode安装包

   ![image-20210930220159175](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930220159175.png)



2. 双击安装文件后可能会出现这个弹窗，不用管他，直接按`确定`

   ![image-20210930222822290](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930222822290.png)

   

3. 同意协议，`下一步`

   ![image-20210930222931098](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930222931098.png)



4. 自定义安装路径，默认的路径太过长，建议安装在 `C:\Program Files\Microsoft VS Code`,选定路径后，`下一步`

   ![image-20210930223458973](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223458973.png)



5. 默认，`下一步`

   ![image-20210930223628746](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223628746.png)

6. 全部勾上，`下一步`

   ![image-20210930223726594](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223726594.png)



7. 开始 `安装`

   ![image-20210930223813641](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223813641.png)

   ![image-20210930223850502](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223850502.png)

8. `完成`安装

   ![image-20210930223924450](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930223924450.png)





### 2.3 配置vscode

vscode安装好了，我们还需要安装一些插件，因为有插件的辅助可以使开发更加的高效和便捷。

开发python需要安装插件有以下几个，其中有几个是美化的插件

* Python
* Code Runner
* Rainbow Brackets
* vscode-icons
* Chinese (Simplified) Language Pack for Visual Studio Code
* Tabnine

 **安装插件的方式**

1. 打开vscode软件，点击左侧的插件安装按钮

   ![image-20210930230547373](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930230547373.png)



2. 在插件安装的搜索框输入插件的名字，然后按回车键查找相应的插件

   ![image-20210930230738724](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930230738724.png)



3. 例如，搜索 `python` ,可以看python相关的插件有下面这些，我们选择自己需要的，点击 `install` 安装

   ![image-20210930231116434](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210930231116434.png)



4. 其他插件的安装和上面列举的一样。



## 3. vscode使用

### 3.1 程序编写

1. 新建一个文件夹，名字可以随意，例如 `code`, 选中该文件夹，右键`通过Code打开`

   ![image-20211001114951771](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001114951771.png)



2. 打开之后，在左侧的空白部分右键，`新建文件`

   ![image-20211001115254836](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001115254836.png)

3. 输入新建文件的名字，名字可以任意，建议不要使用中文，同时文件后缀名一定要是`.py`,例如 `hello.py`

   ![image-20211001115515821](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001115515821.png)



4. 输入文件名后，文件会在右侧自动打开，打开之后我们就可以写代码了，这里输入以下代码，代码的表示什么意思先不深究，到后面会逐句解释的，现在只是学会怎么使用vscode写python的代码

   ```shell
   print("hello python!")
   print("你好")
   ```

   ![image-20211001115917879](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001115917879.png)



### 3.2 程序运行

程序写完后，只需要点击vscode右上角三角形的符号就可以运行了，运行的结果会在下面的输出窗口显示,点了运行的按钮，输出窗口会自动弹出

![image-20211001122544629](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001122544629.png)





### 3.3 问题

在点击运行后，中文输出可能会出现乱码的问题，如下图这样

![image-20211001123334045](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001123334045.png)



**解决方法**

1. 打开设置

   ![image-20211001123523646](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001123523646.png)

   

2. 搜索 `coderun`, 找到 `2` 中的选项，点击 `在setting.json中编辑`

   ![image-20211001123632245](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001123632245.png)



3. 点击之后会打开一个文件，在文件中找到下面框中的这句，把这行换成 `"python": "set PYTHONIOENCODING=utf8 && python -u",`

   ![](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001124000080.png)



4. 替换后，记得保存，然后关闭打开的文件

   ![image-20211001124407223](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001124407223.png)





5. 测试，再次运行代码，可以看到中文不会乱码了

   ![image-20211001124515389](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211001124515389.png)







