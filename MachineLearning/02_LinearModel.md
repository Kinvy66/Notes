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


