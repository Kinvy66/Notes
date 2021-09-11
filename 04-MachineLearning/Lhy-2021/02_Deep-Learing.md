# 深度学习和神经网络训练



## 1. 机器学习任务攻略



1. 一般的流程：

   

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629165202.png" alt="image-20210629165202341" style="zoom: 33%;" />

2. **Model Bias**

   设计的Model的太过于简单，以至于没有包含到loss最小的，如图所示：

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629165828.png" alt="image-20210629165828063" style="zoom:50%;" />

   解决方法：重新设计Model，使其弹性更大





3. **Optimization Issue**

   loss比较大并不是一定是Model Bais导致的，有可能是**Optimization Issue**，最小的loss包含在内，但是没法找到

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629170331.png" alt="image-20210629170331321" style="zoom:50%;" />

   

4. **判断是 Model Bias 还是 Optimization Issue**

   如果说一个简单的和复杂的网络，在训练数据上，复杂的网络loss反而更高，这就是Optimization Issue

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629170850.png" alt="image-20210629170850803" style="zoom:50%;" />

5. **Overfitting**

   在训练数据上loss小，在测试数据loss大，就是Overfitting

   举个很简单的例子：如果一个网络就是针对训练数据生成的，那么在测试数据的loss就会很大

   

6. 交叉验证的方法

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629172301.png" alt="image-20210629172301744" style="zoom: 33%;" />







## 2. 局部最小值（Local minima）与 鞍点（saddle point）

gradient为0的点统称为critical point，在critical point的时候需要判断是local minima 还是saddle point，因为local minima是不能继续减小的，而saddle point还是可以继续减小

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210703171610.png" alt="image-20210703171603560" style="zoom: 33%;" />





**Tayler Series Approximation （泰勒级数逼近）**



* **判断critical point是那种情况**

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210703171921.png" alt="image-20210703171921244" style="zoom: 50%;" />

以上是二次型理论

[Hessian matrix - Wikipedia](https://en.wikipedia.org/wiki/Hessian_matrix)



## 3.  batch（批次）和momentum（动量）

### 3.1  Batch 

在计算梯度时，不是将所有的数据都用来计算，而是把数据分为多个Batch

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210703174103.png" alt="image-20210703174103562" style="zoom:50%;" />

Shuffle 洗牌

以上的优化方法叫做==**BGD**== ，其中 $\eta$​​​ 是学习率，是一个超参数

### 3.2  momentum

#### 3.2.1 （Vanilla）Gradient Descent--一般的梯度下降

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210703182414.png" alt="image-20210703182414789" style="zoom:50%;" />

==SGD== （随机梯度下降）



#### 3.2.2  Gradient Descent + Momentum  ==SGDM==

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210703182600.png" alt="image-20210703182559894" style="zoom:50%;" />

SGDM是会考虑到之前的Gradient

## 4. 自动学习率调整（Learning Rate） 

### 4.1 ==Adagrad== 自适应梯度调整**

![image-20210808091302614](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808091302614.png)

$\theta_i^t$​ 表示的是第 $i$​ 个参数的第 $t$​ 次迭代，learning rate 由 $\eta \rightarrow \frac{\eta}{\sigma_i^t}$​ , $\sigma_i^t$​  使用均方根计算

纠正： 
$$
\sigma_i^t = \sqrt{\frac{1}{t+1} \sum_{i = 0}^t (g_i^t)^2} \\
\sigma_i^t = \sqrt{\frac{1}{t+1} \sum_{t = 0}^t (g_i^t)^2}
$$

> $g_i^t=\nabla L(\theta_t)$ 表示loss function的梯度​​





### 4.2 ==RMSProp==  动态调整

![image-20210808094648432](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808094648432.png)



与Adagrad相比，RMSProp的方法是 $\sigma$ 的计算不同，RMSProp中的 $\alpha$ 是超参数，表示前一个梯度的权重

RMSProp的说明

![image-20210808095109879](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808095109879.png)

### 4.3  ==Adam==： RMSProp  +  Momentum

![image-20210808095212656](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808095212656.png)





### 4.4  Learning Rate Scheduling

使 learning rate $\eta$ 与时间有关，即 $\eta^t$​​ ​,有两种方式：1）Learning Rate Decay  2）Warm Up

![image-20210808095701447](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808095701447.png)



## Summary of Optimization

一些常用的优化方法

* SGD
* SGD with momentum（SGDM）
* Adagrad
* RMSProp
* Adam

![image-20210808100447143](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808100447143.png)







## 5. Classification

### 5.1 回归和分类

![image-20210808102013505](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808102013505.png)

**Soft-max：**
$$
y_i^{'}=\frac{exp(y_i)}{\sum_jexp(y_i)}
$$
![image-20210808102207895](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808102207895.png)

softmax会使相差比较大的值相差更大，小的值更小（趋于0）

> Q&A：对于二分类问题，使用Sigmoid，这和使用二分类softmax是一样的，即本质是一样的。



### 5.2 Loss of Classification

几种常用的loss function， 均方误差，交叉熵

![image-20210808103147418](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808103147418.png)



> 在分类问题常使用Cross-entropy，最小交叉熵等于最大似然





## 6. Batch Normalization

归一化的目标不同维的输入的特征值都在一定的范围，如图

![image-20210808112300864](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808112300864.png)



**Feature Normalization**

![image-20210808112523844](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808112523844.png)



$m_i$ 平均数，$\sigma_i$ 标准差

