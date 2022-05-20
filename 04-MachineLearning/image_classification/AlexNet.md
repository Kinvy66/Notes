## AlexNet

A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” *Commun. ACM*, vol. 60, no. 6, pp. 84–90, May 2017, doi: [10/gbhhxs](https://doi.org/10/gbhhxs).

ref :[3.1 AlexNet网络结构详解与花分类数据集下载_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1p7411T7Pc?spm_id_from=333.999.0.0)

![image-20220227154106224](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220227154106224.png)



![image-20220227154155402](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220227154155402.png)

- Dropout， 以一定的概率对神经元失活，目的是避免过拟合

$N = (W-F+2P)/S+1$

`conv(kernel_num, kernel_size, padding, stride)`

`pool(kernel_size, padding, strie)`

`in/out(H,W,C)`

| layer    | net                   | in            | out           |                           |
| -------- | --------------------- | ------------- | ------------- | ------------------------- |
|          | 输入图像              | 224\*224\*3   |               |                           |
| Conv1    | (48*2,  11, [1,2], 4) | [224, 224, 3] | [55, 55, 96]  | [224 - 11=(1+2)]/4+1 = 55 |
| Maxpool1 | (3, 0, 2)             | [55, 55, 96]  | [27, 27, 96]  | (55-3)/2+1=27             |
| Conv2    | (128*2, 5, [2, 2], 1) | [27, 27, 96]  | [27, 27, 256] | (27-5+4)/1+1=27           |
| Macpool2 | (3, 0, 2)             | [27, 27, 256] | [13, 13, 256] | (27-3)/2+1=13             |
| Conv3    | (192*2, 3, [1,1], 1)  | [13, 13, 256] | [13, 13, 384] | (13-3+2)/1+1 = 13         |
| Conv4    | (192*2, 3, [1,1], 1)  | [13, 13, 384] | [13, 13, 384] | (13-3+2)/1+1 = 13         |
| Conv5    | (128*2, 3, [1,1], 1)  | [13, 13, 384] | [13, 13, 256] | (13-3+2)/1+1 = 13         |
| Maxpool3 | (3, 0, 2)             | [13, 13, 256] | [6, 6, 256]   | (13-3)/2+1 = 6            |
| FC*3     |                       |               |               |                           |

每个conv后都有一个`ReLu`



