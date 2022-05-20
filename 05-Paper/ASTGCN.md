## Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting

基于注意力的时空图卷积网络用于交通流预测





### Abstract

模型由三个独立的部分组成，分别是对短期（几个小时），一天的，一个星期的数据建模。每个部分包含两个主要的部分： 1. 使用注意力机制获取动态的时空交通数据数据的关联性； 2. 使用图卷积处理空间数据，标准卷积处理时间数据



### Introduction

贡献：

1. 提出了一种时空注意力机制用来学习动态时空交通数据的关联性

2. 时空卷积模型，图卷积处理处理空间特征，标准卷积处理时间的依赖关系

3. 用实验验证模型的可行行



### Preliminaries

#### Traffic Networks

准备工作，定义一个无向图 $G=(V,E,\mathbb{A})$ ,  $V$ 是节点的集合， $E$ 是连边的集合， $\mathbb{A} \in \mathbb{R}^{N\times N}$ 是图的邻接矩阵。交通网络G上的每个节点以相同的采样频率检测F个测量值，也就是说，每个节点在每个时间片上生成一个长度为F的特征向量，如图2（b）中的实线所示。

![image-20220306164333446](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220306164333446.png)



#### Traffic Flow Forecasting

假设 $f$-th 时间系列的数据纪录在图网络$G$中的每个节点中, 

$f\in(1, \dots, F).$ $x_{t}^{c,i}$ 表示节点 $i$ 在时间 $t$ 的第 $c$ 个特征，

$\mathbb{X}_{t}^{i}\in \mathbb{R}^{F}$ 表示节点 $i$ 在时间 $t$ 的所有特征。

 $\mathbb{X}_t = (\mathbb{X}_t^1,\mathbb{X}_t^2,\dots, \mathbb{X}_t^N)^{T} \in \mathbb{R}^{N\times F}$ 表所有节点在$t$ 时刻的所有特征。

 $\mathcal{X} = (\mathbb{X}_1,\mathbb{x}_2,\dots,\mathbb{X}_\tau)^{T} \in \mathbb{R}^{N\times F \times \tau}$ 表示所有节点在 $\tau$ 时间切片的所有特征 

$y_t^i=x_t^{f,i}\in \mathbb{R}$ 表示节点 $i$ 在未来 $t$ 时刻的交通流





### Attention Based Spatial-Temporal Graph Convolutional Networks

ASTGCN的整体架构

![image-20220306171245123](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220306171245123.png)

网络由三个独立的部分组成，三个部分的输入 $\mathcal{X}_h,\mathcal{X}_d,\mathcal{X}_w$ 分别表示的几个小时，几天，几周的历史数据。















