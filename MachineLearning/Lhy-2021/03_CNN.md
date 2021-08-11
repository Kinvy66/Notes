# Convolutional Neural Network(CNN)



## 1. 图片分类

### Fully Connected Network

![image-20210809092013759](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809092013759.png)

假设输入是一张100\*100\*3的RGB图片，将图片的像素点拉成3个长向量，以上的架构叫做全连接网络，这种网络在处理图像时需要的参数比较多。







## 2. Observation1 

我们对一张图片分类，可能不需要看整张图片，只看图片的一部分就可以识别出来

![image-20210809092619732](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809092619732.png)



**简化**

每个Neural负责一个小区域的处理，区域之间是可以重叠的。

![image-20210809092807173](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809092807173.png)

**CNN中的一些参数和概念**

![image-20210809094619901](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809094619901.png)

* kernel size：核大小
* stride:  步长，Receptive filed每次移动的步长
* padding： 超出图像的范围，补值方式，补0，。。。



## 3. Observation 2 

如图，鸟嘴出现在不同的位置，但是对于Neural来说是做一样的动作，那每一个Receptive filed都需要放一个处理鸟嘴的Neural吗？这时候可以使用共享参数。

![image-20210809095017392](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809095017392.png)



**共享参数**

![image-20210809095932865](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809095932865.png)

常见的设置

![image-20210809100041259](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809100041259.png)

## Summary



![image-20210809100144172](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809100144172.png)





## 4. Observation 3 （Pooling)

对一张图片进行一定的裁剪，比如把奇数列去掉，并不会影响图片表达的实物

![image-20210809111810180](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809111810180.png)



### Pooling - Max Pooling

Pooling有许多的版本，以Max Pooling为例

![image-20210809111956808](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809111956808.png)

![image-20210809112011961](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809112011961.png)

> Max Pooling就是选取一个范围的最大值，范围的大小是自定义的



![image-20210809112139068](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809112139068.png)

> 一般一层卷积一层池化



![image-20210809114344708](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210809114344708.png)

> Flatten:把图片中本来是矩阵的表示拉直



