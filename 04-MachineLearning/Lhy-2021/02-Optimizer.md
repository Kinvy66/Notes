# Optimizer



![image-20220127093252087](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127093252087.png)

## 一、训练失败的原因

常见的训练失败的原因：梯度为零，梯度为零的情况可能是local minima （局部最小点）或是saddle point （鞍点）。

![image-20220127095902215](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127095902215.png)

我们需要判别式局部最小点还是鞍点，因为局部最小点是没有能够继续走下去的路了，而鞍点还是有路可走的。

**判断方法**

1. 要泰勒级数近似 loss 
   $$
   L(\theta) \approx L(\theta^{'})+(\theta-\theta^{'}{\color{green}{g}})+\frac{1}{2}
   (\theta-\theta^{'})^T{\color{red}{H}}(\theta-\theta^{'})
   $$
   $g$ 是一阶导（梯度），$H$ 是二阶导（Hessian)

2. $H$ 是正定矩阵：Local minima； $H$ 是负定矩阵：Local maxima； $H$ 是半正定矩阵：Saddle point



> 在实际的model训练并不会计算 $H$ ，因为计算量比较大。实际的解决方式的增加维度，比如在我二维空间的局部最小点在三维空间或是更高维度的空间可能是一个鞍点，那么就可以继续计算下去







## 二、 梯度下降的方法

之前的梯度下降的方法叫 ==(Vanilla) Gradient Descent==

==Batch Gradient Descent== ,  ==Gradient Descent + Momentum==



### 1. Batch

将训练数据分成若干个Batch，每个batch计算后都会update一次参数，所有batch计算完成就是一个epoch. 

通常的训练是有多个epoch，为了使每个epoch中的batch数据不一样，一般会在训练完一个epoch后进行shuffle操作

![image-20220127103819226](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127103819226.png)

**Small Batch v.s . Large Batch**

![image-20220127104214042](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127104214042.png)



> large batch : 冷却时间长，伤害高
>
> small batch: 冷却时间短，伤害低
>
> 实际技能冷却时间还是取决于GPU

batch size的大小通常根据所使用的GPU的（内存？核心数？）大小来选择的





**对于使用batch结果会更好的可能解释**

![image-20220127105010205](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127105010205.png)





### 2. Momentum

用物理世界对Momentum的解释，当计算到局部最小点时，因为有动量的存在，能够越过局部最小的

![image-20220127110720671](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127110720671.png)



==(Vanilla) Gradient Descent==

![image-20220127110840582](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127110840582.png)



==Gradient Descent + Momentum== （共轭梯度优化方法）

![image-20220127110909804](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127110909804.png)







## 三、 自适应学习率

训练卡住不一定是 梯度为零或是局部最小点

![image-20220127111526826](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127111526826.png)





自适应学习率，在不同的地方设置不同的学习率

![image-20220127112114089](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127112114089.png)



### 1.Root Mean Square



**对于 $\sigma$ 的计算** ==Root Mean Square== （均方根）， 被用在 ==Adagrad== 的方法中

![image-20220127112345505](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127112345505.png)

 



### 2. RMSProp

![image-20220127112740577](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127112740577.png)



==Adam==

![image-20220127112842337](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127112842337.png)



![image-20220127113657460](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127113657460.png)



## 四、分类

将分类作为回归问题

### 1. 使用Class as one hot vector

![image-20220127115000336](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127115000336.png)



输出多个值

![image-20220127115053676](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127115053676.png)

#### ==Soft-max==

![image-20220127115247044](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127115247044.png)

![image-20220127115257885](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127115257885.png)



#### ==Cross entropy== 

![image-20220127115357844](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220127115357844.png)