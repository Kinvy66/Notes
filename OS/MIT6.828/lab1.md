# Lab 1： Booting a PC



## 介绍

这个实验分为三部分,第一部分主要熟悉x86汇编，QEMU x86模拟器，PC的开机引导程序。第二部分测试 `lab/boot` 下的boot loader。最后，第三部分深入研究了6.828内核本身的初始模块，名为JOS，它位于内核目录中。



### 软件配置

你在本课程中需要的文件以及随后的实验作业都是使用Git版本控制系统发布的。git的学习可参考 [Git user's manual](http://www.kernel.org/pub/software/scm/git/docs/user-manual.html) 

这个课程的git 仓库地址： https://pdos.csail.mit.edu/6.828/2018/jos.git，使用以下命令将文件克隆到本地。

```shell
$ mkdir ~/.mit6.828
$ cd ~./mit6.828
$ git clone https://pdos.csail.mit.edu/6.828/2018/jos.git lab
$ cd lab
```





## Part 1: PC Bootsrap

第一个练习目的是介绍x86汇编和PC的启动过程，开始使用QEMU和QEMU/GDB 调试。这部分的实验不需要写任何代码，但是需要把下面的全部过一遍并且理解，能够回答出下面的问题。



### Getting Started with x86 assembly

如果你不会x86汇编，你将通过本课程快速熟悉汇编。 [PC Assembly Language Book](https://pdos.csail.mit.edu/6.828/2018/readings/pcasm-book.pdf) 是一本比较好的入门书。不过这本书使用的是NASM汇编，而我们课程使用的是 GNU汇编。NASM使用的是Intel格式而GNU使用的是AT&T格式。语义上两者是一致的，但是语法是不同的。不过两者之间的转换非常简单，在[Brennan's Guide to Inline Assembly](http://www.delorie.com/djgpp/doc/brennan/brennan_att_inline_djgpp.html)中有介绍。

> 练习1：
>
> 熟悉 [the 6.828 reference page](https://pdos.csail.mit.edu/6.828/2018/reference.html)上提供的汇编语言材料。你现在不必阅读它们，但是在阅读和编写 x86 程序集时，您几乎肯定会想要参考这些材料中的一些内容。
>
> 建议阅读[Brennan's Guide to Inline Assembly](http://www.delorie.com/djgpp/doc/brennan/brennan_att_inline_djgpp.html) 的“The Syntax”这章内容。它对我们将在 JOS 中与 GNU 汇编器一起使用的 AT&T 汇编语法进行了很好的（而且非常简短的）描述。



当然，x86 汇编语言编程的权威参考是 Intel 的指令集架构参考，你可以在 [the 6.828 reference page](https://pdos.csail.mit.edu/6.828/2018/reference.html)上找到两种版本：旧的  [80386 Programmer's Reference Manual](https://pdos.csail.mit.edu/6.828/2018/readings/i386/toc.htm)的 HTML 版本，它比最新的手册更短且更易于查找，但描述了我们将在 6.828 中使用的所有 x86 处理器功能；来自英特尔的完整、最新和最好的 IA-32 英特尔架构软件开发人员手册，涵盖了我们在课堂上不需要的最新处理器的所有功能，但您可能有兴趣了解。 [AMD](http://developer.amd.com/resources/developer-guides-manuals/)提供了一套一样（通常更友好）的手册。 保存 Intel/AMD 架构手册以备后用，或在您想要查找特定处理器功能或指令的最终解释时将其用作参考。



### Simulating the x86

我们不是在真实的物理计算机 (PC) 上开发操作系统，而是使用一个模拟完整 PC 的程序--模拟器，为模拟器写的代码在物理机上也是可以运行的。使用模拟器简化了调试。比如你可以设置断点，这在真实的cpu是很难做到的。

6.828课程将使用[QEMU Emulator](http://www.qemu.org/)，这是一个现代且相对快速的模拟器。虽然 QEMU 的内置监视器仅提供有限的调试支持，但 QEMU 可以充当[GNU debugger](http://www.gnu.org/software/gdb/) (GDB) 的远程调试目标，我们将在本实验室中使用它来逐步完成启动过程。

首先，按照上面“软件设置”中的描述，将 Lab 1 文件解压缩到你自己物理机上的目录中，然后在 lab 目录中输入`make`（或在 BSD 系统上为 `gmake`）以构建你将启动的最小 6.828 引导加载程序和内核。

```shell
$ cd lab
$ make
+ as kern/entry.S
+ cc kern/entrypgdir.c
+ cc kern/init.c
+ cc kern/console.c
+ cc kern/monitor.c
+ cc kern/printf.c
+ cc kern/kdebug.c
+ cc lib/printfmt.c
+ cc lib/readline.c
+ cc lib/string.c
+ ld obj/kern/kernel
+ as boot/boot.S
+ cc -Os boot/main.c
+ ld boot/boot
boot block is 380 bytes (max 510)
+ mk obj/kern/kernel.img

```

如果有"undefined reference to `__udivdi3'"这样的错误，你可能没有 32bit gcc编译器，如果使用的是Debian或Ubuntu，尝试安装  gcc-multilib

现在你可以运行 QEMU，使用上面创建的文件 `obj/kern/kernel.img` 作为模拟 PC 的“虚拟硬盘”的内容。 这个硬盘映像包含我们的引导加载程序（`obj/boot/boot`）和我们的内核（`obj/kernel`）

```shell
$ make qemu			# or  make qemu-nox
```

这将使用设置硬盘和直接串行端口输出到终端所需的选项执行 QEMU。 一些文本应该出现在 QEMU 窗口中：

```shell
***
*** Use Ctrl-a x to exit qemu
***
qemu-system-i386 -nographic -drive file=obj/kern/kernel.img,index=0,media=disk,format=raw -serial mon:stdio -gdb tcp::26000 -D qemu.log 
6828 decimal is XXX octal!
entering test_backtrace 5
entering test_backtrace 4
entering test_backtrace 3
entering test_backtrace 2
entering test_backtrace 1
entering test_backtrace 0
leaving test_backtrace 0
leaving test_backtrace 1
leaving test_backtrace 2
leaving test_backtrace 3
leaving test_backtrace 4
leaving test_backtrace 5
Welcome to the JOS kernel monitor!
Type 'help' for a list of commands.
K> 

```

在 "Booting from Hard Disk... "之后的所有内容都是由我们JOS内核打印的；`K>`是由我们包含在内核中的小型监视器或交互式控制程序打印的提示。如果你使用了`make qemu`，这些由内核打印出来的行会同时出现在你运行QEMU的常规shell窗口和QEMU显示窗口。这是因为为了测试和实验评分的目的，我们已经设置了JOS内核，使其控制台输出不仅写入虚拟VGA显示器（如在QEMU窗口中看到的），而且写入模拟PC的虚拟串口，QEMU再输出到自己的标准输出。同样，JOS内核将接受来自键盘和串口的输入，所以你可以在VGA显示窗口或运行QEMU的终端给它下命令。另外，你也可以通过运行`make qemu-nox`来使用串口控制台而不使用虚拟VGA。如果你是通过SSH进入系统，这可能很方便。要退出qemu，输入`Ctrl+a x`。

你只有两个命令可以给内核监视器，`help`和`kerninfo`。



运行的截图：

![image-20210817123716281](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210817123716281.png)







### The PC's Physical Address Space

现在我们将深入了解一下个人电脑如何启动的细节。一台个人电脑的物理地址空间被硬性规定为具有以下一般布局：

```

+------------------+  <- 0xFFFFFFFF (4GB)
|      32-bit      |
|  memory mapped   |
|     devices      |
|                  |
/\/\/\/\/\/\/\/\/\/\

/\/\/\/\/\/\/\/\/\/\
|                  |
|      Unused      |
|                  |
+------------------+  <- depends on amount of RAM
|                  |
|                  |
| Extended Memory  |
|                  |
|                  |
+------------------+  <- 0x00100000 (1MB)
|     BIOS ROM     |
+------------------+  <- 0x000F0000 (960KB)
|  16-bit devices, |
|  expansion ROMs  |
+------------------+  <- 0x000C0000 (768KB)
|   VGA Display    |
+------------------+  <- 0x000A0000 (640KB)
|                  |
|    Low Memory    |
|                  |
+------------------+  <- 0x00000000
```



