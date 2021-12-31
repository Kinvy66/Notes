# 线性模型



## 1. 基本形式

给定由$d$ 个属性描述的示例 ${\bf{x}}=\{x_1;x_2;\dots;x_d\}$ ,其中$x_i$ 是$\mathcal{x}$ 在第$i$ 个属性上的取值，线性模型

 试图学得一个通过属性的线性组合来进行预测的函数，即
$$
f(x)=w_1x_1+w_2x_2+\dots+w_dx_d+b
$$
一般用向量形式写成
$$
f(x)=\vec{w}^T\vec{x}+b
$$
模型的参数是$\vec{w}$, $b$ 



## 2. 线性回归

给定数据集 $D=\{(x_1,y_1),(x_2,y_2),\dots,(x_m,y_m)\}$ ，其中 $x_i=\{x_{i1};x_{i2};\dots;x_{id}\},y_i\in \mathbb{R}$. 线性回归（linear regression)试图学得一个线性模型以尽可能准确地预测实值输出标记。

**目标**：线性回归试图学得
$$
f(x_i)=wx_i+b,使得 f(x_i)\simeq y_i
$$
**方法**：

如何确定$w,b$ ？关键在于如何衡量$f(x)$与$y$ 之间的差别，这里使用均方误差作为性能度量，让均方误差最小化,即
$$
(w^*,b^*)=\underset{w,b}{arg\ min}\sum_{i=1}^{m}(f(x_i)-y_i)^2\\
=\underset{(w,b)}{arg\ min}\sum_{i=1}^{m}(y_i-wx_i-b)^2
$$

**求解过程：**

计算 $w,b$ 的偏导，使偏导等于0，求出 $w,b$
$$
\frac{\partial E_{(w,b)}}{\partial w} = 2 (w\sum_{i= 1}^{m}x_i^2-\sum_{i=1}^{m}(y_i-b)x_i),\\
\frac{\partial E_{(w,b)}}{\partial b} =2(mb-\sum_{i=1}^{m}(y_i-wx_i))\\
令 \frac{\partial E_{(w,b)}}{\partial w} = 0，\frac{\partial E_{(w,b)}}{\partial b} =0, 得\\
w=\frac {\sum_{i=1}^{m}y_i(x_i-\bar{x})}{\sum_{i=1}^{m}x_i^2-\frac {1}{m}(\sum_{i=1}^mx_i)^2}\\
b=\frac{1}{m}\sum_{i=1}^m(y_i-wx_i)
$$
更一般的形式：
$$
f(\vec x_i) = \vec w^T\vec x_i+b ,使得 f(\vec x_i)\simeq y_i
$$
广义模型，其中 $g(\cdot)$ 是单调可微函数：
$$
y= g^{-1}(\vec w^T\vec x+b)
$$




## 3. 对数几率回归

考虑二分类任务，其输出标记 $y\in \{0,1\}$  ,而线性回归任务模型产生的预测值 $z=\vec w^T\vec x+b$ 是实值，我们需将实值 $z$ 转换为 $0/1$ 值，最理想的是 "单位阶跃函数"
$$
y=
\begin{cases}
0, & z<0\\
0.5, & z=0\\
1, & z>0\\
\end{cases}
$$


![image-20210715175241485](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210715175241485.png)

从上图可看出，单位阶跃函数不连续，因此不能直接用作 $(7)$ 中的 $g^-(\cdot)$ ,于是使用对数几率函数（logistic function）,对数几率函数是一种 ==“Sigmoid函数”==
$$
y=\frac{1}{1+e^{-z}}
$$
==对数几率回归（logistic regression)== 这是一个分类模型:
$$
y=\frac{1}{1+e^{-(\vec w^T\vec x+b)}}
$$

- [ ] $w,b$ 的求取





