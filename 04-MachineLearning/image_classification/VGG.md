## VGG

K. Simonyan and A. Zisserman, “Very Deep Convolutional Networks for Large-Scale Image Recognition,” *arXiv:1409.1556 [cs]*, Apr. 2015, Accessed: Feb. 11, 2022. [Online]. Available: http://arxiv.org/abs/1409.1556

rer: [4.1 VGG网络详解及感受野的计算_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1q7411T7Y6/?spm_id_from=pageDriver)

![image-20220227192547816](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220227192547816.png)

VGG网络的创新点：多个小的卷积核可替代一个大的卷积核，感受视野范围不变，但是可以减少参数



Net:

![image-20220227192853836](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220227192853836.png)

conv 的stride为1， padding为1

maxpoolde的size为2，stride为2



![yygx.net_](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/yygx.net_.jpg)

