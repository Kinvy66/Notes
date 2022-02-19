# CNN

对于张 100\*100\*3 的RGB 图片来说，用==fully connected Network== （全连接网络）处理

![image-20220128102352894](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128102352894.png)

将图片变成一个 1\*(100\*100\*3) 的一维向量，神经元的个数是1000， 则参数 $w$ 的数量是 $100\times100\times3\times1000 = 3\times10^7$ 

参数越多可以增加模型的弹性，但是也会有overfitting的风险

对于图片分类的观察



## 一、对于图片分类的观察



### 1. Observation1

辨别图片的类别，或许可以不用看图片的全部，只需要观察某个局部的信息就可以了

![image-20220128103609276](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128103609276.png)



对于这种方式的一种简化解释

![image-20220128103844563](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128103844563.png)

一个神经元考虑一个 Receptive field，这个Receptive field的大小由自己确定

**经典设定**

![image-20220128104347695](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128104347695.png)







### 2.Observation2

对于不同的图片，他们的相同特征可能出现在不同的位置，对于检测这个特征的神经元不需要在每一个特征区域都存在

![image-20220128104748989](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128104748989.png)

**参数共享**

![image-20220128105203351](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128105203351.png)

上面这两个神经元的参数 $w_i$ 是一样的

**经典的设定**

![image-20220128110431457](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128110431457.png)

==filter== （过滤器，卷积核）





==CNN==

![image-20220128105726750](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128105726750.png)



> Fully Connected Layer，将图片的每个像素多输入到一组神经元中，并且每个像素的是有不同的 $w$ 
>
> Receptive Field，将图片的每个区域输入到一组神经元中，并且每个区域的是有不同的 $w$ 
>
> Convolutional Layer，将图片的每个区域输入到一组神经元中，但是每个区域的 $w$ 是一样的







## 二、 CNN 的另外一种解释

![image-20220128112520778](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128112520778.png)



以一张 6\*6的单通道黑白图片为例，==filter== 就是卷积核（过滤器），假设这里设定为64个卷积核，它的大小是由自己设定的，深度是和原始的图片一样，卷积核中的数值是未知的参数。因为卷积核核的大小是3\*3所以这里能够侦测的范围也是3\*3， ==stride== （步长）设定为1。

**卷积计算过程：**

![image-20220128114444463](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220128114444463.png)

从原始图片起始位置（一般是图片的左上角）取一个卷积核大小的区域（3\*3)，和卷积核进行内积运算得到一个与卷积核大小的矩阵，将该矩阵各个位置的值全部相加，得到一个标量值（如果是一个RGB图片的话，得到的是一个一维向量，深度是3）。接下来将3\*3大小的窗口按给定步长向右移动，进行同样的矩阵计算，直到扫过图片的全部区域，如果移动到图片边界，需要进行==padding==操作。一个filter计算完成，输出的矩阵就是一个==Feature Map== .这里设定的是有64个filter ，所有filter的输出在深度方向叠加，所以最后得到的是一个深度为64的二维矩阵

举例 32\*32\*3 的RGB 图片，卷积核是5\*5\*3（W\*H\*C)，步长是2，卷积核个数是10，paddin设置为0

1. 图片总共有10\*10个5\*5的区域，每一个feature map的大小是10\*10*3
2. 10个卷积核，最后的卷积输出就是10\*10\*3*10





RGB 图片，卷积核为 2\*2\*3, 步长为1，卷积核个数为2

![image-20220130113957486](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130113957486.png)



将对对应通道的卷积核和对应通道的receptive filed 进行卷积运算，将三个通道的值相加就得到第一个feature map的第一个位置的值，扫完一整张图



1. 卷积和的channel与输入特征层的channel相同
2. 输出的特征矩阵channel与卷积核的个数相



卷积后的矩阵尺寸大小计算公式:
$$
N = (W-F+2P)/S +1
$$
输入图片的大小 $W*W$ , Filter大小 $F*F$ ,步长 $S$, padding的像素 $P$





## 三、Observation3 （Pooling）

将一张图片的某些像素去掉，不会影响图片的信息

![image-20220129102040773](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129102040773.png)



### ==Pooling==

==Max Pooling== 对 f eature map进行一个分组（怎么分组是自定义的），下面的是把Feature Map分成2\*2，Max-Pooling操作就是去一个2\*2中最大一个，所以每个Feature Map就成了2\*2

![image-20220129102447616](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129102447616.png)

Pooling主要减少运算量，但是在比较精细的任务上一般不会用pooling，比如围棋



CNN整个架构

![image-20220129102723686](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129102723686.png)























