# 基本概念



[P2-机器学习基本概念](https://www.bilibili.com/video/BV1Wv411h7kN?p=2)

## 1. 机器学习基本概念



### 1.1 什么是机器学习

机器学习就是寻找函数，这个函数可以实现输入一个信号，输出一个我们需要获取的信号，例如：

![image-20210629104414283](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629104421.png)





### 1.2 机器学习的类型

1. 回归（Regression）：输出是一个标量（scalar）
2. 分类（classification）：给一些选项（类别），函数输出一个正确的
3. 结构化学习（Structured Learing）：输出结构化的内容



### 1.3 如何寻找一个函数

以YouTube视频的播放量为例子，预测未来的播放量

1. **写出一个function with unknown parameters**  
   $$
   y = b + wx_1
   $$
   $w, b$ 是未知的参数



2. **define loss**

   loss是一个关于 $w,b$ 的函数 $L(b,w)$, loss是衡量参数好坏的标准
   $$
   L(0.5k,1)\ \ \ \ y=b+wx_1\ \rightarrow \ y = 0.5k+1x_1
   $$
   

   预估的结果和真实的结果的差距：

   ![image-20210629110742418](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629110742.png)

   Loss：
   $$
   Loss: L=\frac{1}{N}\sum_{n}e_n
   $$
   绝对误差和均方差：

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629111230.png" alt="image-20210629111230446" style="zoom:33%;" />

3. **Optimization（优化）**

   目标： $w^*,b^*=\underset{w,b} {arg\ min}\ L$

   方法： Gradient Descent（梯度下降），即求 w和b的偏微分

   步骤：

   ![image-20210629112635645](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629112635.png)

   hyperparameters：超参数，自己设定的参数，其中 $\eta$ (Learing Rate)就是一个超参数

   ==local minimal的问题后续会说明==

   

   ### 1.4 ML的步骤

   ML的步骤：

   

   ![image-20210629114148465](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629114148.png)



## 2. 深度学习基本概念

Liner Model 或许太过简单 ，有时需要复杂的Model。

Linear Model有一些限制，这个叫 **Model Bias** (和 b的 bias不一样)

**示例：**

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629114817.png" alt="image-20210629114817356" style="zoom:50%;" />

红色function = 一个常数 + 一系列蓝色的function



### 2.1 Sigmoid Function

上述的蓝色的function可以近似的function表示，这个function叫 Sigmoid Function

表达式：
$$
y=c\frac{1}{1+e^{-(b+wx_1)}}\\
=c\ sigmoid(b+wx_1)
$$

---



<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629115504.png" alt="image-20210629115504677" style="zoom:50%;" />



对于不同的w,b,c，function的变化：

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629115643.png" alt="image-20210629115643087" style="zoom:50%;" />



### 2.2 一个新的Model

将Linear Model变化一下，使用sigmoid function 来表示
$$
y = b+wx_1 \\
\downarrow \\
y = b+\sum_i c_i\ sigmoid(b_i + w_i x_1)\\
$$

$$
y = b+\sum_j w_j x_j\\
\downarrow \\
y=b+\sum_i c_i\ sigmoid(b_i+\sum_j w_{ij}x_j)
$$

转换为矩阵运算

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629124356.png" alt="image-20210629124356394" style="zoom:50%;" />

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629124520.png" alt="image-20210629124520406" style="zoom:50%;" />

---

函数的未知参数

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629124701.png" alt="image-20210629124701706" style="zoom:50%;" />





### 2.3  回到ML的步骤

1. Step 1: function with unknown
   $$
   y=b+\vec{c}^T\sigma(\vec{b}+\vec{W}\vec{x})
   $$



2. Loss 

   $L(\theta)$ 
   $$
   L = \frac{1}{N}\sum_n e_n
   $$
   

3. Optimization

   目标：$\theta^* = \underset{\theta}{arg\ min}\ L$

   计算步骤：

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629130154.png" alt="image-20210629130154614" style="zoom:50%;" />

   ---

   

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629130219.png" alt="image-20210629130219605" style="zoom:50%;" />

   实际计算Gradient是从所有的训练数据中选取一个Batch计算：

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629131132.png" alt="image-20210629131132225" style="zoom:50%;" />





### 2.4  ReLU（Rectified Linear Unit）

怎么表示下面的这个function

<img src="C:/Users/kinvy/AppData/Roaming/Typora/typora-user-images/image-20210629131526640.png" alt="image-20210629131526640" style="zoom:50%;" />

由图可知用两个ReLU叠加就是第一个，表达式：
$$
Sigmoid \longrightarrow \ ReLU \\
y = b+\sum_ic_i\ sigmoid(b_i+\sum_jw_{ij}x_j)\\
\downarrow\\
y=b+\sum_{2i}c_imax(0,b_i+\sum_jw_{ij}x_j)
$$


**Deep Learning**

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629132432.png" alt="image-20210629132431949" style="zoom:50%;" />

---



# To Learn More



## 1. 深度学习简介

1. **Fully Connect Feedforward Network （全连接前馈网络）**

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629162352.png" alt="image-20210629162352243" style="zoom:50%;" />

   **Deep = Many hidden layers** 



## 2. Backpropagation（反向传播）

Backpropagation 是一种高效的计算梯度的方法



1. Chain Rule（链式法则）

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629163902.png" alt="image-20210629163902437" style="zoom:50%;" />

2. Backpropagation 

   一个简单的实例

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629164049.png" alt="image-20210629164049088" style="zoom:50%;" />



3. Forward Pass

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629164208.png" alt="image-20210629164208516" style="zoom:50%;" />

4. Backward Pass

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629164330.png" alt="image-20210629164330056" style="zoom:50%;" />

