# Ch3  文件 I/O

## 3.1 引言

在UNIX系统中，常用的文件I/O函数有--打开文件，读文件，写文件等。例如：`open`、`read`、`write`、`lseek` 、`close`. 本章描述的函数主要是不带缓冲的I/O.



## 3.2 文件描述符

文件描述符是一个非负整数，对内核来说，所有打开的文件多是通过文件描述符引用的。当打开或创建一个文件时，内核向进程返回的也是一个文件描述符。==在UNIX系统中的shell，标准输入，标准输出，标准错误分别与文件描述符0,1,2相关联。==





## 3.3 函数  <span style = "font-family: Courier New">open</span> 和  <span style = "font-family: Courier New">openat</span>

* 函数原型

  ```c
  #include <fcntl.h>
  
  int open(const char *path, int oflag, ... /* mode_t mode */);
  int openat(int fd, const char *path, int oflag, ... /* mode_t mode */);
  //两函数的返回值：若成功，返回文件描述符；若出错，返回-1
  ```

   最后一个参数写 `...` 表示余下的参数类型和数量是可变的，

  

* 函数参数		

  `path`是打开或创建文件的名字，

  `oflag`参数

  |  oflag参数  |                             说明                             |
  | :---------: | :----------------------------------------------------------: |
  |  O_RDONLY   |                           只读打开                           |
  |  O_WRONLY   |                           只写打开                           |
  |   O_RDWR    |                           读写打开                           |
  |   O_EXEC    |                          只执行打开                          |
  |  O_SEARCH   |                          只搜索打开                          |
  |             | 以上5个常量必须指定一个<br/>，且只能指定一个，下面的是可选参数 |
  |  O_APPEND   |                        以追加的方式写                        |
  |  O_CLOEXEX  |               把FD_CLOEXEC常量设置为文件描述符               |
  |   O_CREAT   | 若文件不存在则创建它，<br />使用此选项是还需要说明参数mode<br />指定新文件的权限 |
  | O_DIRECTORY |                    path引用的不是目则出错                    |
  |   O_EXCL    | 如果指定了O_CREAT，而文件已经存在，则出错<br />用此测试一个文件是否存在，不存在则创建 |
  |  O_NOCTTY   | 如果path引用的是终端设备，<br />则不将该设备分配作为从进程的控制终端 |
  | O_NOFOLLOW  |               path引用的是一个符号链接，则出错               |
  | O_NONBLOCK  | path引用的的是一个FIFO，一个块特殊文件，<br />则打开非阻塞操作 |
  |   O_SYNC    |                使每次write等待物理I/O操作完成                |
  |   O_TRUNC   | 如果文件存在，而且为只写或读-写成功打开<br />则将其长度截断为0 |
  | O_TTY_INIT  |   如果打开一个还未打开的终端设备，设置非标准termios参数值    |
  |   O_DSYNC   |                                                              |
  |   O_RSYNC   |                                                              |

  

  `fd`参数把 <span style = "font-family: Courier New">open</span> 和 <span style = "font-family: Courier New">openat</span> 函数区分开，有三种可能性

  1. path参数指定的绝对路径名，在这种情况下，fd参数被忽略， <span style = "font-family: Courier New">openat</span>函数就相当于<span style = "font-family: Courier New">open</span> 函数
  2. path参数指定的是相对路径名，fd参数指出了相对路径名在文件系统中的开始地址，fd参数是通过打开相对路径名所在的目录来获取。
  3. path参数指定了想到路径名，fd参数具有特殊值AT_FDCWD，在这种情况下，路径名在当前工作目录中获取，<span style = "font-family: Courier New">openat</span>函数在操作上是<span style = "font-family: Courier New">open</span>函数类似。



## 3.4 函数  <span style = "font-family: Courier New">creat</span>

`creat` 函数创建一个新文件

* 函数原型

  ```c
  #include <fcntl.h>
  int creat(const char *path, mode_t mode);
  //返回值：若成功，返回为只写文件打开的文件描述符；若出错，返回-1
  ```

  此函数等效： `open(path, O_WRONLY|O_CREAT|O_TRUNC, mode)`

  <span style = "font-family: Courier New">creat</span>函数的一个不足制之处是他以只写方式打开所创建的文件，所以一般使用<span style = "font-family: Courier New">open</span>替代。



## 3.5 函数  <span style = "font-family: Courier New">close</span>

`close` 函数关闭一个打开的文件

* 函数原型

  ```c
  #include <unistd.h>
  int close(int fd);
  //返回值： 若成功，返回0；若出错，返回-1
  ```



## 3.6 函数  <span style = "font-family: Courier New">lseek</span>

`lseek `函数显示地为一个打开文件设置偏移量

* 函数原型

  ```c
  #include <unnistd.h>
  off_t lseek(int fd, off_t offset, int whence);
  ////返回值： 若成功，返回新的文件偏移量；若出错，返回-1
  ```



* 函数参数

  offset与whence的值有关

  * 若whence是 SEEK_SET，则将该文件的偏移量设置为距文件开始处 offset个字节。
  * 若whence是SEEK_CUR，则将该文化的偏移量设置为其当前值加offset，offset可为正或负。
  * 若whence是SEEK_END，则将该文件的偏移量设置为文件长度加offset，offset可为正或负。



* 实例，用于测对标准输入能否设置偏移量

  ```c
  #include "apue.h"
  int main()
  {
      if (lseek(STDIN_FILENO, 0, SEEK_CUR) == -1)
          printf("cannot seek\n");
      else
          printf("seek ok\n");
      exit(0);
  }
  ```

  测试

  ```shell
  $ ./a.out < /etc/passwd
  seek ok
  $ cat < /etc/passwd | ./a.out
  cannot seek
  $ ./a.out < /var/spool/cron/FIFO
  cannot seek
  ```

  



## 3.7 函数 <span style = "font-family: Courier New">read</span>

`read` 函数从打开文件中读数据

* 函数原型

  ```c
  #include <unistd.h>
  ssize_t read(int fd, void *buf, size_t nbytes);
  // 返回值： 读到的字节数，若已到文件尾，返回0；若出错，返回-1
  ```

  实际读到的字节数可能少于要求读的字节数。造成这种的情况有很多。



## 3.8 函数  <span style = "font-family: Courier New">write</span>

`write` 函数向打开文件写数据 

* 函数原型

  ```c
  #include <unistd.h>
  ssize_t write(int fd, const void *buf, size_t nbytes);
  //返回值： 若成功，返回已写的字节数；若出错，返回-1
  ```

  其返回值通常与参数nbytes的值相同，否则表示出错。



## 3.9 I/O 效率

以下程序使用 read 和 write 函数复制一个文件

```c
#include "apue.h"

#define BUFFSIZE 4096

int main()
{
    int n;
    char buf[BUFFSIZE];
    
    while((n = read(STDIN_FILENO, buf, BUFFSIZE)) > 0)
        if (write(STDOUT_FILENO, buf, n) != n)
            err_sys("write error");
    
    if( n < 0)
        err_sys("read error");
    
    exit(0);
}
```

BUFFSIZE设置不同的值时，CPU的时间

![image-20210812131850591](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210812131850591.png)

这里是文件系统采用了预读的技术，当监测到正在进行顺序读取时，系统会预先读取比需要的更多数据。

这个实例后面还会用到





## 3.10 文件共享

UNIX系统支持在不同进程间共享打开的文件，下面对这种共享介绍

内核使用3种数据结构表示打开文件，它们之间的各系决定了在文件共享方面一个进程对另一个进程可能产生的影响。如下图，是对应的3张表的关系：<a id="fig3-7"></a>

![image-20210812160302225](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210812160302225.png)

1. 每个进程维护着一种表，该表记录了该进程打开的所有文件的描述符，同时还有一个文件指针，指向打开的文件。
2. 内核为所有打开的文件维护着一张文件表，该表记录了文件状态标志，文件偏移量，指向v节点表的指针
3. 每个打开的文件（或设备）都有一个v节点表（v-node)结构，v节点包含了文件类型和对此文件进行各种操作函数的指针。v节点又包含了一个i节点（i-node，索引节点）。

这些表在打开文件是从磁盘读入内存，所有的信息随时都可用。



如果是两个进程打开同一个文件，这些表的关系图如下：<a id="fig3-8"></a>

![image-20210812161610119](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210812161610119.png)

说明：

1. 在每个<span style = "font-family: Courier New">write</span>后，在文件表现中的当前文件偏移量会增加所写入的字节数。如果这导致当前文件偏移量超出了当前文件长度，则将i节点表中的当前文件铲毒设置为当前文件偏移量（也就是文件加长了）。
2. 如果使用 <span style = "font-family: Courier New">O_APPEND</span>（追加方式）标志打开一个文件，文件表中的偏移量首先会被设置为i节点表中的文件长度。
3. 若使用 <span style = "font-family: Courier New">lseek</span>定位为文件的尾端，则文件表中的当前文件偏移被设置为i节点表中的文件长度，==注意，这与用O_APPEND标志打开文件是不同的，比如3.11中两个进程打开一个文件==
4. <span style = "font-family: Courier New">lseek</span>函数只修改文件表中的文件偏移量，不进行I/O操作。

## 3.11 原子操作



### 1. 追加到一个文件

早起的UNIX系统是不支持 <span style = "font-family: Courier New">open</span> 的 <span style = "font-family: Courier New">O_APPEND</span>选项，将数据追加到文件尾端通常是下面这样写的

```c
if(lseek(fd, OL, 2) < 0)		//position to EOF
    err_sys("lseek error");
if (write(fd, buf, 100) != 100)	// and write
    err_sys("write error");
```

对于单个进程，上面的程序可以正常工作

当有A,B两个进程同时操作同一个文件时，则会产生问题

![image-20210812171343608](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210812171343608.png)

A，B进程操作同一个文件，是只有一个v节点表的。参考[图3-8](#fig3-8)

1. A进程将当前文件偏移量定位到文件尾端，A进 程文件表中的当前文件偏移量为1500。
2. 执行进程B，调用<span style = "font-family: Courier New">lseek</span>定位到文件的尾端，B进程文件表中的当前文件偏移量设置为1500，再写入一定数量的数据，使得文件长度增至1600。
3. 再次回到A进程，由于A进程文件表中的当前文件偏移量为1500，所以才1500开始写入数据，这样就会导致A进程写入的数据会覆盖B进程写入的部分或全部的数据。

解决以上问题的方法就是使两个操作成为一个原子操作，==任何多于一个函数调用的操作都不是原子操作==，因为在两个函数调用之间内核可能会临时挂起进程。

UNIX系统为这样的操作提供了一种原子操作方法，即在打开文件 <span style = "font-family: Courier New">open</span>函数设置 <span style = "font-family: Courier New">O_APPEND</span> 选项。

> 一般而言，原子操作指的是由多步组成的一个操作。如果该操作原子地执行，则要执行完所有步骤，要么一步也不执行，不可能只执行所有步骤的一个子集。



### 2. 函数  <span style = "font-family: Courier New">pread</span> 和  <span style = "font-family: Courier New">pwrite</span>

* 函数原型

  ```c
  #include <unistd.h>
  //返回值：读到的字节数，若已到文件尾，返回0；若出错，返回-1
  ssize_t pread(int fd, void *buf, size_t nbytes, off_t offset);
  
  //返回值：若成功，返回已写的字节数；若出错，返回-1
  ssize_t pwrite(int fd, const void *buf, size_t nbytes, off_t offset);
  
  ```

调用 <span style = "font-family: Courier New">pread</span> 相对于调用 <span style = "font-family: Courier New">lseek</span> 后调用 <span style = "font-family: Courier New">read</span> ,但是 <span style = "font-family: Courier New">pread</span> 又与这种顺序调用有下列重要区别。

* 调用 <span style = "font-family: Courier New">pread</span> 时，无法中断其定位和读操作
* 不更新当前文件偏移量

调用 <span style = "font-family: Courier New">pwrite</span> 相对于调用 <span style = "font-family: Courier New">lseek</span> 后调用 <span style = "font-family: Courier New">write</span> 



## 3.12 函数 <span style = "font-family: Courier New">dup</span>  和  <span style = "font-family: Courier New">dup2</span>

这两个函数是用来复制一个车现有的文件描述符

* 函数原型

  ```c
  #include <unistd.h>
  int dup(int fd);
  int dup2(int fd, int fd2);	
  //两函数的返回值：若成功，返回新的文件描述符；若出错，返回-1
  ```

  由  <span style = "font-family: Courier New">dup</span> 返回的新文件描述符一定是当前可用文件描述符中的最小数值。对于  <span style = "font-family: Courier New">dup2</span> ，可以用 fd2 参数指定新的描述符的值。如果fd2 已经打开，则先将其关闭。如若fd等于fd2，则  <span style = "font-family: Courier New">dup2</span> 返回 fd2， 而不关闭它。否则，fd2 的  <span style = "font-family: Courier New">FD_CLOEXEC</span> 文件描述符标志被清除，这样fd2 总进程调用   <span style = "font-family: Courier New">exec</span> 时是打开状态。

执行 `newfd = dup(1);` 后的内核数据结构：

![image-20210813121328289](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210813121328289.png)







## 3.13 函数 <span style = "font-family: Courier New">sync</span> 、<span style = "font-family: Courier New">fsync</span> 和 <span style = "font-family: Courier New">fdatasync</span> 

当我们向文件写入数据时，内核通常先将数据复制到缓冲区中，然后排入队列，晚些时候写入磁盘。通常当内核需要重用缓冲区来 存放其他磁盘块数据是，它会把延迟写数据写入磁盘。

为了保证磁盘实际文件系统与缓冲区中内容的一致性，UNIX系统提供了下面三个函数

* 函数原型

  ```c
  #include <unistd.h>
  int fsync(int fd);
  int fdatasync(int fd);
  						//返回值：若成功，返回0；若出错，返回-1
  void sync(void);
  ```

<span style = "font-family: Courier New">sync</span> 只是将所有修改过的块缓冲区排入写队列，然后返回，它并不等实际写磁盘操作结束。通常系统守护进程 <span style = "font-family: Courier New">update</span> 会每隔30秒调用 <span style = "font-family: Courier New">sync</span> 函数，这保证定期清除内核的块缓冲区。

<span style = "font-family: Courier New">fsync</span> 函数只对指定的文件 fd 起作用，并且等待写磁盘操作结束才返回。

<span style = "font-family: Courier New">fdatasync</span> 函数类似于 <span style = "font-family: Courier New">fsync</span> ,它只影响文件的数据部分，但 <span style = "font-family: Courier New">fsync</span> 还会同步更新文件的属性。



## 3.14 函数 <span style = "font-family: Courier New">fcntl</span> 

<span style = "font-family: Courier New">fcntl</span> 函数可以改变已经打开文件的属性

* 函数原型

  ```c
  #include <fcntl.h>
  int fcntl(int fd, int cmd, ... /* int arg */);
  //返回值：若成功，则依赖于cmd（见下）；若出错，返回-1
  ```

* 函数功能

  1. 复制一个已有的描述符（<span style = "font-family: Courier New">cmd = F_DUPFD 或 F_DUPFD_CLOEXEC</span> ）
  2. 获取/设置文件描述符标志 （<span style = "font-family: Courier New">cmd=F_GETFD 或 F_SETFD</span> ）
  3. 获取/设置文件状态标志 （<span style = "font-family: Courier New">cmd=F_GETFL 或 F_SETFL</span> ）
  4. 获取/设置异步I/O所有权 （<span style = "font-family: Courier New">cmd=F_GETOWN 或 F_SETOWN</span> ）
  5. 获取/设置记录锁 （<span style = "font-family: Courier New">cmd=F_GETLK、F_SETLK 或 F_SETLKW</span> ）

* cmd的选项

  cmd有11个选项值，这里先介绍8种。参照 [图3-7](#fig3-7) 讨论各个表的状态值

  |    cmd参数值    |                        说明                        |
  | :-------------: | :------------------------------------------------: |
  |     F_DUPFD     | 复制文件描述符fd，<br />新文件描述符作为函数值返回 |
  | F_DUPFD_CLOEXEC |                   复制文件描述符                   |
  |       ...       |                        ...                         |



* 实例

  ```c
  #include "apue.h"
  #include <fcntl.h>
  
  int main(int argc, char *argv[])
  {
      int val;
  
      if (argc !=2)
          err_quit("usage: a.out <descriptor#>");
      
      if ((val = fcntl(atoi(argv[1]), F_GETFL, 0)) < 0)
          err_sys("fcntl error for fd %d", atoi(argv[1]));
      
      switch (val & O_ACCMODE)
      {
      case O_RDONLY:
          printf("read only");
          break;
      case O_WRONLY:
          printf("write only");
          break;
      case O_RDWR:
          printf("read write");
          break;
      
      default:
          err_dump("unknown access mode");
          break;
      }
  
      if (val & O_APPEND)
          printf(", append");
      if (val & O_NONBLOCK)
          printf(", nonblocking");
      if (val & O_SYNC)
          printf(", synchronous writes");
      
  #if !defined(_POSIX_C_SOURCE) && defined(O_FSYNC) && (O_FSYNC != O_SYNC)
      if (val & O_FSYNC)
          printf(", synchronous writes");
  #endif
  
      putchar('\n');
      exit(0);
  }
  ```

  对于指定的文件描述符打印文件标志，运行测试

  ![image-20210813175910565](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210813175910565.png)
  
  /home/kinvy/apue/ch1/04-shell.c /home/kinvy/apue/ch3/01_fcntl.c



## 3.15 函数 <span style = "font-family: Courier New">ioctl</span>

<span style = "font-family: Courier New">ioctl</span> 函数是 I/O 操作的杂物箱，在前面提到的函数不能实现的操作通常用 <span style = "font-family: Courier New">ioctl</span> 表示，终端 I/O 是使用 <span style = "font-family: Courier New">iotcl</span> 最多的地方

* 函数原型

  ```c
  #include <unistd.h>			// System V
  #include <sys/ioctl.h>		// BSD and Linux
  int ioctl(int fd, int request, ...);
  							//返回值： 若出错，返回-1；若成功，返回其他值
  ```



## 3.16 <span style = "font-family: Courier New">/dev/fd</span>

UNIX 系统都会提供一个名为 <span style = "font-family: Courier New">/dev/fd</span> 的目录，其目录内是名为 0、1、2等文件。打开文件 <span style = "font-family: Courier New">/dev/fd/n</span> 等效与复制描述符 n （假定描述符n是打开的）。



