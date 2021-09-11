# 神经网络



## 1. 神经元模型

神经网络中最基本的成分是神经元模型，抽象图如下（M-P神经元模型）

![M-P神经元模型](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210720122911511.png)

在这个模型中，神经元接收到来自 $n$ 个其他神经元传递过来的输入信号，这些输入信号通过带权重的连接进行传递，神经元接收到的总输入值将与神经元的阈值进行比较，通过==激活函数（activation function）==处理以产生神经元的输出。实际中常用 $Sigmoid$ 函数作为激活函数。





## 2. 感知机与多层网络

感知机是由两层神经元组成，如图，输入层接收外接输入信号后传递给输出层，输出层是 M-P神经元，亦称“阈值逻辑单元”。

![image-20210720131003622](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210720131003622.png)

以上这个简单的网络解决的问题有限，一般需要使用多层的神经元，以下是一个常见的网络连接方式，“==多层前馈神经网络==”

![image-20210720131659383](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210720131659383.png)



## 3. 误差你传播算法

==误差逆传播（error BackPropagation，简称BP）== 算法是一个用于神经网络学习的算法，通常所说的 “BP网络”是指用BP算法训练的多层前馈神经网络。

 

