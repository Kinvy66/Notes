# Java基础

## 1.  开发环境搭建

1. [JDK](https://www.oracle.com/cn/java/technologies/javase-downloads.html)下载

2. 安装，默认配置，路径可更改

3. 设置环境变量

   ![image-20210618092654482](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210618092701.png)

![image-20210618092718819](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210618092718.png)



## 2. HelloWorld

```java
//单行注释
public class HelloWorld {
    /*
    多行注释
    */
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```



编译运行命令

```bash
javac HelloWorld.java	#编译
java HelloWorld		#运行

```

