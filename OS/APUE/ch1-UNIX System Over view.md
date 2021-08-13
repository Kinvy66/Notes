# 第一章  UNIX基础知识

## 1. UNIX 体系架构

UNIX系统的体系图

![image-20210811105425252](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811105425252.png)

说明：内核的接口是个一个叫做 `系统调用(system calls)` 软件层，一些常用的库函数是建立在系统调用接口之上的，但是应用层可以调用两者。

