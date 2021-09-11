# Self-attention



## 1. Self-attention解决的问题

输入是以系列vector时会怎样?

![image-20210810090601793](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810090601793.png)

举例：语音识别，关系图谱，分子式



### 关于输出

输入和输出一样，输入和输出不一样，输出不确定

![image-20210810093221056](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810093221056.png)



## 2. self-attention

### 2.1 self-attention

对于生成的新向量，不是独立的，是根据上下文内容生成的

![image-20210810094218799](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810094218799.png)

### 2.2 self-attention原理

**如图产生 $b^1$​​​​ 的过程**

1. 找出 $a^1$ 和 其他向量的关联性用 $\alpha$ 表示

![image-20210810095000970](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810095000970.png)

2. $\alpha$​ 的计算

   两种计算方式，以dot-produt为例

   ![image-20210810095312415](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810095312415.png)

   > 过程：输入的向量分别乘矩阵 $W^q,W^k$ 得到 $q,k$ 两个向量，$q,k$ 做内积运算，得到的结果就是 $\alpha$



3. 计算结果

   ![image-20210810095905807](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810095905807.png)

   $a^1$​ 还需要自己和自己计算关联性

   ![image-20210810100157353](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810100157353.png)

4. 计算 $b^1$

   ![image-20210810100235434](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810100235434.png)

   > $V^i$ 表示的是从输入中抽取的一些重要信息

5. 用一样的方法计算 $b^2,b^3,\dots$ , 在实际计算式 $b^1,b^2,b^3,\dots$​​, 是并行计算的，没有先后次序



### 2.3 self-attention 的矩阵理解

1.  q，k， v矩阵

   ![image-20210810100707918](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810100707918.png)

   > $W^q,W^k,W^v$  是通过训练得来的参数

2.  $\alpha$​  的计算

   ![image-20210810101544673](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810101544673.png)



3. 计算 $b$

   ![image-20210810101841210](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810101841210.png)

4. summary

   ![image-20210810101932468](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810101932468.png)



## 3. Multi-head Self-attention

![image-20210810104159716](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810104159716.png)





## 4. Position Encoding

![image-20210810104423925](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810104423925.png)







## 5. self-attention  V.S.  CNN 

![image-20210810104958795](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810104958795.png)

