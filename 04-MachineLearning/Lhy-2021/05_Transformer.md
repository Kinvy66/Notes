# Transformer



## 1. Sequence-to-sequence（Seq2seq）

**应用举例：**

- **NLP**

![image-20210810110048059](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210810110048059.png)

2. **多分类问题：**

![image-20211119161544783](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211119161544783.png)



## 2. Transformer

![image-20211119161718759](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211119161718759.png)





### 2.1 Encoder

- 一个Block中是有几个处理

  ![image-20211119162001661](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211119162001661.png)

- T中的Encoder

  ![image-20211119162952408](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211119162952408.png)

  > 输入一个向量，经过Self-attention的处理，输出的向量 $a$ 会再加上原始的输入 $b$, 得到 $a+b$ ,这种方式叫 $residual\  connection$ （残差网络）
  >
  > $layer\ normalization$ : 对输入向量计算方差和均值

  总结：

  ![image-20211119163306889](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211119163306889.png)





















