## A Survey on Knowledge Graph-Based Recommender Systems



### Abstract

本文主要是调查已经提出的推荐系统对知识图谱的利用和可解释性，并提出了推荐系统一些潜在的研究方向

####  存在的挑战和问题

- 数据的稀疏 (data sparsity)
- 冷启动 (cold-start)



#### 分类

对于该领域已经发表的论文分为三类（从知识图谱数据的使用方式来分类）

1. 基于嵌入的方法 （embedding-based method）
2. 基于连接的方法 （connection-based methods）
3. 基于传播的方法 （propagation-based methods）





### 1. INTRODUCTION

#### 1.1 推荐算法的分类

1. 基于协同过滤的算法 （collaborative filtering (CF)-based）,  基于相似的用户或是用户的交互数据构建模型
2. 基于内容的算法 （content-based） ，利用内容的特征构建模型
3. 混合算法 （hybrid recommender systems）

第一种算法的应用比较多，它可以在多场景中实现，且不需要额外的内容特征。然而，它也存在一些问题，数据的稀疏 (data sparsity)和冷启动 (cold-start)。



==Ref==: Freebase [17], DBpedia [18], YAGO [19], Google’s Knowledge Graph [20]



**文章结构**

section2, 相关符号和概念，KG和推荐系统的基础

Section 3，4，从方法和使用的测试数据的角度回顾基于知识图谱的推荐系统

Section 5， 一些潜在的研究方向

Section 6， 总结





## 2. BACKGROUNDS

相关概念介绍

#### 1. Recommender Systems

推荐系统，推荐任务是将一个或一系列未知的items推荐给用户。它的步骤如下

首先，系统学习目标用户$u_i$ 和候选项目 $v_j$ . 然后学习一个计分函数 ：$f: u_i\times v_j \to \hat{y}_{i,j}$ ,表示用户 $u_i$ 对 $v_j$ 的喜爱程度，最后根据喜爱程度的排序生成推荐。

应用领域：POI (point of interest),news , transportation , and education.



#### 2. Heterogeneous Information Network (HIN)

异构信息网络，HIN是一个有向图 $G = (V,E)$ , V: Vertex (or node) attributes,E: Edge (or link) attributes and directions, 它有一个实体（节点）映射函数 $\phi:V\to\mathcal{A}$, 连边映射函数 $\psi:E\to\mathcal{R}$



#### 3. Knowledge Graph (KG)

知识图谱，KG $\mathcal{G}=(V,E)$ 是一个有向图，它的节点是实体，边是对主客实体的约束。每条连边的形式为（头实体，关系，尾实体）表示为 $<e_h,r,e_t>$ , 代表从实体$e_h$ 到实体 $e_t$ 的关系 $r$. 知识图片可以看作是HIN的实例。

描述一个KG通常遵循RDF(Resource Description Framework)标准，就是节点表示实体，连边表示两个实体之间的关系。

本文将收集的KGs相关论文分为两类

##### Item Knowledge Graph

物品知识图谱，物品作为图中的每个节点实体，连边的是物品之间的属性关系，比如品牌，分类，或者是于用户的关系，比如共同被浏览，共同被购买。这种图的节点是没有用户作为实体的

##### User-Item Knowledge Graph

用户-物品知识图谱，在这种图谱中，用户、物品及其关联的实体作为节点。除了item KG中与item相关的关系外，user-item KG中还包含了用户与item之间的关系，如“购买”、“点击”、“提及”等。

#### 4. Meta-path

Meta-path是定义在一个图网络 $G_T=(\mathcal{A},\mathcal{R})$ 的一条路径。它在 $A_0$ 和 $A_k$ 之间定义了一种新的复合关系 $R_1R_2\dots R_k$. 它是连接HIN中对象对的关系序列，可用于提取图中的连接特征。



#### 5. Meta-graph

与元路径类似，元图是另一个连接HIN中两个实体的元结构。不同的是，元路径只定义了一个关系序列，而元图是不同元路径的组合[43]。与元路径相比，元图可以包含图中实体之间更多的表达性结构信息。



#### 6. Knowledge Graph Embedding (KGE)

KGE是将一个KG G = (V, E)嵌入到一个低维空间[44]。在嵌入过程中，每个图的组成部分，包括实体和关系，都用一个d维向量来表示。低维嵌入仍然保留了图的固有属性，它可以通过图中的语义或高阶接近度进行量化。



#### 7.H-hop Neighbor  , Entity Triplet Set







## 3. METHODS OF RECOMMENDER SYSTEMS WITH KNOWLEDGE GRAPHS

基于知识图谱的推荐系统的方法，根据对知识图谱数据的使用方式分为三大类

1. 基于嵌入的方法 （embedding-based method）
2. 基于连接的方法 （connection-based methods）
3. 基于传播的方法 （propagation-based methods）

**相关方法总览表**

![image-20220305131040182](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220305131040182.png)



### 3.1 Embedding-based Method



