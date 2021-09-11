# 文件和目录

## 4.1 引言

第三章介绍了执行I/O操作的基本函数，主要是普通文件I/O——打开文件，读写文件。本章将描述文件系统的其他特征和文件的性质。



## 4.2 函数 <span style = "font-family: Courier New">stat、fstat、fstatat 和 lstat</span>

这几个函数都是用来获取文件的相关信息的

* 函数原型

  ```c
  #include <sys/stat.h>
  int stat(const char *restrict pathname, struct stat *restrict buf );
  int fstat(int fd, struct stat *buf );
  int lstat(const char *restrict pathname, struct stat *restrict buf );
  int fstatat(int fd, const char *restrict pathname,
              struct stat *restrict buf, int flag);
  //以上四个函数的返回值：若成功：返回0；若出错，返回-1
  ```



* 函数说明

  <span style = "font-family: Courier New">stat</span> 函数返回文件名为 "pathname"的文件的有关信息结构。

  <span style = "font-family: Courier New">fstat</span> 函数返回文件描述符为fd的文件的有关信息。

  <span style = "font-family: Courier New">lstat</span> 函数类似 <span style = "font-family: Courier New">stat</span> ，但是命名的文件是一个符号链接时，<span style = "font-family: Courier New">lstat</span> 返回该符号链接的有关信息。

  <span style = "font-family: Courier New">fstatat</span> 函数为一个相对于当前打开目录的路径名返回文件统计信息。

  

* <span style = "font-family: Courier New">stat</span>结构体

  ```c
  struct stat
  {
      mode_t st_mode;          /* file type & mode (permissions) */
      ino_t st_ino;            /* i-node number (serial number) */
      dev_t st_dev;            /* device number (file system) */
      dev_t st_rdev;           /* device number for special files */
      nlink_t st_nlink;        /* number of links */
      uid_t st_uid;            /* user ID of owner */
      gid_t st_gid;            /* group ID of owner */
      off_t st_size;           /* size in bytes, for regular files */
      struct timespec st_atim; /* time of last access */
      struct timespec st_mtim; /* time of last modification */
      struct timespec st_ctim; /* time of last file status change */
      blksize_t st_blksize;    /* best I/O block size */
      blkcnt_t st_blocks;      /* number of disk blocks allocated */
  };
  ```

  



## 4.3 文件类型

前面介绍了两种不同的文件类型：普通文件和目录。除此之外还有其他的文件类型:

1. 普通文件，最常用的文件类型，这种文件包含某种形式的数据。
2. 目录文件，包含了其他文件的名字以及指向与这些文件有关信息的指针。对一个目录文件具有读权限的任何以进程都可以读该目录的内容，但只有内核可以直接写目录文件。
3. 块特殊文件，提供对设备（如磁盘）带缓冲的访问，每次访问以固定长度为单位进行。
4. 字符特殊文件，提供对设备不带缓冲的访问，每次访问长度可变。系统中的所有设备要么是字符特殊文件，要么是块特殊文件
5. FIFO，用于进程间通信，也称为命名管道
6. 套接字，用于进程间的网络通信
7. 符号链接，指向另一个文件

**<span style = "font-family: Courier New"><sys/stat.h></span> 中的文件类型宏**

|                             宏                             |   文件类型   |
| :--------------------------------------------------------: | :----------: |
| <span style = "font-family: Courier New">S_ISREG()</span>  |   普通文件   |
| <span style = "font-family: Courier New">S_ISDIR()</span>  |   目录文件   |
| <span style = "font-family: Courier New">S_ISCHR()</span>  | 字符特殊文件 |
| <span style = "font-family: Courier New">S_ISBLK()</span>  |  块特殊文件  |
| <span style = "font-family: Courier New">S_ISFIFO()</span> |  管道或FIFO  |
| <span style = "font-family: Courier New">S_ISLNK()</span>  |   符号链接   |
| <span style = "font-family: Courier New">S_ISSOCK()</span> |    套接字    |



**<span style = "font-family: Courier New"><sys/stat.h></span> 中的进程间通信（IPC）宏**

|                              宏                              |  对象的类型  |
| :----------------------------------------------------------: | :----------: |
| <span style = "font-family: Courier New">S_TYPEISMQ()</span> |   消息队列   |
| <span style = "font-family: Courier New">S_TYPEISSEM()</span> |    信号量    |
| <span style = "font-family: Courier New">S_TYPEISSHM()</span> | 共享存储对象 |



* 实例, 打印从命令行输入的参数的文件类型

  ```c
  #include "apue.h"
  int main(int argc, char *argv[])
  {
      int i;
      struct stat buf;
      char *ptr;
      for (i = 1; i < argc; i++)
      {
          printf("%s: ", argv[i]);
          if (lstat(argv[i], &buf) < 0)
          {
              err_ret("lstat error");
              continue;
          }
          if (S_ISREG(buf.st_mode))
              ptr = "regular";
          else if (S_ISDIR(buf.st_mode))
              ptr = "directory";
          else if (S_ISCHR(buf.st_mode))
              ptr = "character special";
          else if (S_ISBLK(buf.st_mode))
              ptr = "block special";
          else if (S_ISFIFO(buf.st_mode))
              ptr = "fifo";
          else if (S_ISLNK(buf.st_mode))
              ptr = "symbolic link";
          else if (S_ISSOCK(buf.st_mode))
              ptr = "socket";
          else
              ptr = "** unknown mode **";
          printf("%s\n", ptr);
      }
      exit(0);
  }
  ```

  测试

  ![image-20210814175840294](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210814175840294.png)



## 4.4 设置用户 ID 和设置组 ID

与一个进程相关联的ID有6个或更多

![image-20210814181650975](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210814181650975.png)



## 4.5 文件访问权限

st_mode 值包含了对文件的访问权限位，前面提到的所有的文化都是有访问权限的。

每个文件有9个访问权限位，可将它们分为3类，图4-6： <a id="fig4-6"></a>

| <span style = "font-family: Courier New">st_mode</span>屏蔽 |   含义   |
| :---------------------------------------------------------: | :------: |
|   <span style = "font-family: Courier New">S_IRUSR</span>   |  用户读  |
|   <span style = "font-family: Courier New">S_IWUSR</span>   |  用户写  |
|   <span style = "font-family: Courier New">S_IXUSR</span>   | 用户执行 |
|   <span style = "font-family: Courier New">S_IRGRP</span>   |   组读   |
|   <span style = "font-family: Courier New">S_IWGRP</span>   |   组写   |
|   <span style = "font-family: Courier New">S_IXGRP</span>   |  组执行  |
|   <span style = "font-family: Courier New">S_IROTH</span>   |  其他读  |
|   <span style = "font-family: Courier New">S_IWOTH</span>   |  其他写  |
|   <span style = "font-family: Courier New">S_IXOTH</span>   | 其他执行 |



## 4.6 新文件和目录的所有权

新文件的用户ID设置为进程的有效用户ID，关于组ID，POSIX.1 允许实现选择下列之一作为新文件的组ID

1. 新文件的组ID可以是进程的有效组ID
2. 新文件的组ID可以是它所目录的组ID



## 4.7 函数 <span style = "font-family: Courier New">access 和 faccessat</span>

这两个函数是按实际用户ID和实际组ID进行访问权限测试

* 函数原型

  ```c
  #include <unistd.h>
  int access(const char *pathname, int mode);
  int faccessat(int fd, const char *pathname, int mode, int flag);
  					//两个函数的返回值：若成功，返回0；若出错，返回-1
  ```

  

* 参数

  当mode为 <span style = "font-family: Courier New">F_OK</span> 表示测试文件是否存在，否则mode为下列常量的按位或
  
  | mode |     说明     |
  | :--: | :----------: |
  | R_OK |  测试读权限  |
  | W_OK |  测试写权限  |
  | X_OK | 测试执行权限 |



<span style = "font-family: Courier New">access 和 faccessat</span> 在下面两种情况是相同的：1）pathname参数为绝对路径，2）fd参数取值为AT_FDCWD而pathname参数为相对路径。

- 实例

  ```c
  #include "apue.h"
  #include <fcntl.h>
  
  int main(int argc, char * argv[])
  {
  	if(argc != 2) {
  		err_quit("usage: a.out <pathname>");
  	}	
  	if(access(argv[1], R_OK) < 0){
  		err_ret("assess error for %s", argv[1]);
  	}
  	else {
  		printf("read access OK\n");
  	}
  	if(open(argv[1], O_RDONLY) < 0) {
  		err_ret("open error for %s", argv[1]);
  	}
  	else {
  		printf("open for reading OK\n");
  	}
  
  	exit(0);
  }
  
  ```

  





## 4.8 函数 <span style = "font-family: Courier New">umask</span>

<span style = "font-family: Courier New">umask</span> 函数为进程设置文件模式创建屏蔽字，并返回之前的值

* 函数原型

  ```c
  #include <sys/stat.h>
  mode_t numask(mode_t cmask);		//返回值：之前的文件模式创建屏蔽字
  ```

* 参数cmask是由[图4-6](#fig4-6) 中列出的9个常量中的若干个按位或构成的





