# 深度学习和神经网络训练



## 1. 机器学习任务攻略



1. 一般的流程：

   

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629165202.png" alt="image-20210629165202341" style="zoom: 33%;" />

2. **Model Bias**

   设计的Model的太过于简单，以至于没有包含到loss最小的，如图所示：

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629165828.png" alt="image-20210629165828063" style="zoom:50%;" />

   解决方法：重新设计Model，使其弹性更大





3. **Optimization Issue**

   loss比较大并不是一定是Model Bais导致的，有可能是**Optimization Issue**，最小的loss包含在内，但是没法找到

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629170331.png" alt="image-20210629170331321" style="zoom:50%;" />

   

4. **判断是 Model Bias 还是 Optimization Issue**

   如果说一个简单的和复杂的网络，在训练数据上，复杂的网络loss反而更高，这就是Optimization Issue

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629170850.png" alt="image-20210629170850803" style="zoom:50%;" />

5. **Overfitting**

   在训练数据上loss小，在测试数据loss大，就是Overfitting

   举个很简单的例子：如果一个网络就是针对训练数据生成的，那么在测试数据的loss就会很大

   

6. 交叉验证的方法

   <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210629172301.png" alt="image-20210629172301744" style="zoom: 33%;" />







## 2. 局部最小值（Local minima）与 鞍点（saddle point）

gradient为0的点统称为critical point，在critical point的时候需要判断是local minima 还是saddle point，因为local minima是不能继续减小的，而saddle point还是可以继续减小



















