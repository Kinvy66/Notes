# Transformer

transformer是一个 seq2seq的模型

![image-20220130094941226](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130094941226.png)



## 一、 Seq2seq

Transformer的整体架构

![image-20220130100326484](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130100326484.png)







## 二、 Encoder

![image-20220130100457424](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130100457424.png)



具体的架构

![image-20220130100752035](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130100752035.png)



==Layer Norm== 对同一个Feature 的不同维度

==Batch Norm== 对不同Feature的同一个维度







## 三、Decoder

### 1. Autoregressive

以语音识别为例，Encoder会将输入的序列信息输出一组向量，这组向量会作为Decoder的输入，同事在加上一个 special token。首先输出第一个字 "机"，再把"机"和 start作为输入，输出"器"；接着把"器" 和start作为输入，输出"学"，反复以上过程。



![image-20220130102534842](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130102534842.png)



### 2. Decoder

![image-20220130102854778](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130102854778.png)

将Decoder的一部分用盖住，会发现Decoder和Encoder是一样的（部分地方有点不同）

![image-20220130102906832](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130102906832.png)



**不同之处Masked Self attention**

Masked Self attention就是再计算的时候只关注输入向量左边的，比如 $b^2$ 的计算，只关注 $a^2$ 和 $a^1$ 的关联程度，依次类推 $b^3$ 的计算，只关注 $a^3$ 和 $a^1,a^2$ 的关联程度，

![image-20220130103431115](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130103431115.png)

> 因为在Decoder中一个一个的计算，在前面的还没有计算出来，是没有后面的输入





### 3. Adding “Stop Token”

输出的长度是不知道，Decoder会一直不停的输出

![image-20220130104226699](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130104226699.png)



为了使Decoder结束输出，会加上一个停止的标志

![image-20220130104441438](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130104441438.png)



## 四、Decoder--Non autoregressive (NAT)

![image-20220130104739298](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130104739298.png)





## 五、Encoder--Decoder

Encoder-Decoder的连接（Cross attention），也就是下图红框中的部分，

![image-20220130105012253](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130105012253.png)

具体实现



![image-20220130105339688](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130105339688.png)



![image-20220130105542092](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220130105542092.png)