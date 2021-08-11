# Generation



## 1. Network as Generator

神经网络作为生成器来用

![image-20210810111136592](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810111136592.png)

> z是从一个分布中采样出来的，例如高斯分布，network同时看想，x和z的输入，输出一个复杂的分布

###  为什么需要输出一个分布

**example1：**

![image-20210810111855751](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810111855751.png)

可能输出两种结果

![image-20210810112030717](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810112030717.png)

解决方式，

![image-20210810112156248](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810112156248.png)





# Generative Adversarial Network（GAN）



## 1. Basic of GAN

举例，Unconditional generation，生成一个二次元人物

![image-20210811095431193](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811095431193.png)

### 1.1 Discrimination

在GAN中，除了Generator外还需要训练一个Discrimination

![image-20210811095555877](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811095555877.png)

> Discrimination也是一个Neural Networks，输入一张图片，输出一个scalar，越大表示生成的图片越像真实的图片



**GAN过程**

![image-20210811100156127](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811100156127.png)

> Generator 和Discriminator共同的迭代进化







## 2. Algorithm

### 2.1 steps

* **step1**

  ![image-20210811100545202](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811100545202.png)

  > 初始化一个G和D，随机从数据集中采样，G生成图片，把图片给D分辨



* **step2**

  ![image-20210811101051543](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811101051543.png)

  > 固定D，update G，使得D输出的数值最大。可以将G,D看做一个网络，这个网络只改变G的部分

* 训练过程

  ![image-20210811101536042](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811101536042.png)

  > G和D是反复的训练，





## 3. Theory behind GAN

###  3.1 目标

![image-20210811102233873](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811102233873.png)

> GAN的目标是生成的数据尽可能的接近真实的训练（测试）数据

![image-20210811102420520](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811102420520.png)

* **问题：怎么计算 $Div$​​​**

  只需要能够从训练数据中采样就可以了。虽然不知道 $P_G, P_{data}$ 的分布，但是可以采样

  ![image-20210811103059701](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811103059701.png)

  

* **靠 Discrimination计算

  ![image-20210811103339541](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811103339541.png)

  > $E_{y\sim P_{data}}$​​ 表示的是从真实数据集采样的数据，等同于下式

  ![image-20210811103851725](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210811103851725.png)

