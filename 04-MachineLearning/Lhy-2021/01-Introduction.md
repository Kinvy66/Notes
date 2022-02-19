# Introduction



## 一、 什么是机器学习

**机器学习就是寻找一个函数**

![image-20220126103521926](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126103521926.png)



### 机器学习的不同类型

**Regression**： 回归任务

**Classification**：分类任务

![image-20220126103647509](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126103647509.png)

> 除了回归和分类任务，机器学习还有 `Structred Learning` 



## 二、案例

预测Youtube的播放量



### 1. 定义一个带未知参数的函数 （model）

![image-20220126104143417](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126104143417.png)

这里定义的函数是 $y=b+wx_1$ 

$y$ 是预测值 ，$x_1$ 已知的数据（比如前一天或几天的播放数据）， $w, b$ 是未知的参数



### 2. 定义 Loss 

**Loss is a function of parameters** $L(b,w)$

Loss：用来度量一组参数的好坏

![image-20220126104701083](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126104701083.png)

 上面计算的是预测值和实际值的差值

==MAE== : mean absolute error   $e=|y-\hat{y}|$  绝对值误差

==MSE== : mean square error   $e=(y-\hat{y}^2)$ 均方误差

这里定义的loss函数是 ： $Loss: L = \frac{1}{N}\sum_{n}e_n$





### 3. 优化迭代

在这个案例中优化目标是 :
$$
w^*,b^*=arg\ \underset{w,b}{min}\ L
$$
使用==Gradient Descent== （梯度下降）的方法求最优解

#### 求解步骤

1. 随机取一个初始的$w_0$ 
2. 计算 $\frac{\partial L}{\partial w}|_{w=w_0}$   , $w_1 \leftarrow w^0-\eta \frac{\partial L}{\partial w}|_{w=w_0}$ 其中 $\eta$ 是 ==learning rate== （学习率）
3. 重复步骤 2 直到 $w$ 取得最小值 

参数 $b$ 的求解和 $w$ 一样



==hyperparameters== （超参数）需要通过学习得到或是自己设定的一些参数 比如 $\eta$  



![image-20220126111137934](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126111137934.png)



![image-20220126111316284](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126111316284.png)







## 三、 机器学习的步骤



![image-20220126111537212](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126111537212.png)



### 1. step1

在上面的案例中定义的是一个 ==Linear model== （线性模型）实际效果并不是很好，进一步改进
$$
y = b + \sum_{j=1}^{7} w_jx_j
$$
将7天（一周）的数据做一次计算，甚至可以用一个月（28天）的数据

![image-20220126112347891](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126112347891.png)



![image-20220126112623027](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126112623027.png)

复杂的红色线段可以使用 一个常数 + 若干个蓝色的线段组成

对于蓝色曲线的表示，用 ==Sigmoid Function== 近似
$$
y = {\color{red}{c}} \frac{1}{1+e^{-({\color{green}{b}} + {\color{blue}{w}}x_1)}} \\
={\color{red}{c}}\ sigmoid({\color{green}{b}}+{\color{blue}{w}}x_1)
$$
Sigmoid曲线

![butbu-](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126113836520.png)



不同的 $c,b,w$ 曲线的影响

![image-20220126114159734](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126114159734.png)



**使用 sigmoid 定义新的模型**

![image-20220126114422391](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126114422391.png)

矩阵的形式， $i$  no. of sigmoid    $j$  no. of features

![image-20220126114729049](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126114729049.png)



![image-20220126114542375](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126114542375.png)



**整个过程**

![image-20220126115115034](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126115115034.png)

**新模型中的参数**

![image-20220126115259399](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126115259399.png)





### 2. step2 

![image-20220126115410829](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126115410829.png)

Loss 变成了一个关于 $\theta$ 的函数  $L(\theta)$

![image-20220126115859724](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126115859724.png)



### 3. step3

![image-20220126115928804](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126115928804.png)

优化的目标函数
$$
\theta^* = arg\ \underset{\theta}{min}\ L
$$
![image-20220126120035928](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220126120035928.png)



使用上面的计算方式不断的迭代

==Batch==

![image-20220126120420345](C:/Users/Kinvy/AppData/Roaming/Typora/typora-user-images/image-20220126120420345.png)

==epoch==  ==update==







### 4. ReLu

![image-20220126120714948](C:/Users/Kinvy/AppData/Roaming/Typora/typora-user-images/image-20220126120714948.png)

==ReLu==
$$
y = {\color{red}{c}} max\ (0, {\color{green}{b}}+{\color{blue}{w}}x_1)
$$


**Sigmoid** ， **ReLU** 都叫 ==Activation Function== （激活函数），除此之外还有其他的激活函数。