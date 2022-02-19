# Self-attention

Attention is all you need：https://arxiv.org/abs/1706.03762





一个序列向量的输入，输出也是一个序列， ==seq2seq==

![image-20220129105435862](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129105435862.png)





## 二、Sequence Labeling

![image-20220129105733719](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129105733719.png)

对于上面的例子，使用Fully-connected 一个一个的计算，两个 saw会是一样的结果，一个解决的方式是使用窗口





## 二、 Self-attention

![image-20220129110112558](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129110112558.png)

经过self-attention的处理输出的向量是考虑了每个输入之间的关联性

![image-20220129110414422](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129110414422.png)



### 1. 生成 $b^1$

用 $\alpha$ 表示两个向量之间的关联性

![image-20220129110517847](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129110517847.png)

#### $\alpha$ 的计算

下面是一种计算方式，将输入向量分别和两个矩阵 $W^q,W^k$  相乘得到 $q, k$ 两个向量，$q,k$ 点积得到 $\alpha$ 

![image-20220129110707157](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129110707157.png) 



 计算 $a^1$ 和每一个输入向量的$\alpha$  

 ![image-20220129111128671](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129111128671.png)

除了和其他向量计算关联性，一般也会和自己计算关联性，最后还会有一个soft-max

![image-20220129111327726](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129111327726.png)

在计算每个输入向量的重要性 $v$

![image-20220129111624136](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129111624136.png)





## 三、 Self-attention矩阵表示

回顾，以 $b^2$ 为例

![image-20220129111851052](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129111851052.png)

###  矩阵运算

$q, k, v$ 的计算， $W^q, W^K, W^v$ 是需要学习的参数



![image-20220129111948540](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129111948540.png)

$\alpha$ 的矩阵

![image-20220129112339167](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129112339167.png)

$b$ 的输出

![image-20220129112412766](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129112412766.png)

**整体过程**

![image-20220129112500268](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129112500268.png)

## 四、Multi head Self attention

![image-20220129113047806](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129113047806.png)



Multi head Self attention就是多个 $q,k,v$ 不同的 $q,k,v$ 负责不同的类型的相关性



## 五、Positional Encoding

各个输入向量之间的位置关系是没有任何区别的（在没有加入位置信息之前）。

![image-20220129113526907](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220129113526907.png)



原始的 Transformer的位置信息是如上右图，每一列表示一个位置信息的向量，将对应的位置信息向量直接加到原始的输入向量中。Positional Encoding生成的方式有很多，甚至可以通过训练得到 