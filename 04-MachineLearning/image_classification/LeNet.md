## LeNet

[1]Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning applied to document recognition,” PROCEEDINGS OF THE IEEE, vol. 86, no. 11, p. 47, 1998, doi: 10/d89c25.

LetNet是CNN的雏形，它的网络架构如下图所示
![20220226104730](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20220226104730.png)

- 

卷积后输出尺寸计算

$N = (W-F+2P)/S + 1$

- 输入图片大小 $W*W$
- Filter大小 $F*F$ （卷积和的尺寸）
- 步长 $S$
- padding的像素 $P$

eg: $input(3*32*32),\ \ output = (32-16+2*0 )/ 1 + 1 = 28$ 输出是 16 \* 28\* 28



- 卷积层 `ConvNet(in_channels, kernel_num, kernel_size)`, eg(3, 16, 5): 输入数据的通道是3，卷积核个数是16，卷积核尺寸是5\*5.  kernel_num 也是`out_channels`

- 池化层（下采样） `Pool(pool_size, stride)`, eg(2, 2)
- 全连接 `FC(in, nn_num)` in 输入的向量， nn_num神经元的个数（节点个数）

| layer | Net | input | output | des |
| ---- | ---- | ----| ---- | ---- |
| 输入 |  | 3\*32\*32 | | |
| conv1|(3, 16, 5)|3\*32\*32| 16 \* 28\* 28 |reru|
| MaxPool1 | (2, 2)          |16 \* 28\* 28| 16\*14\*14    ||
| conv2 | (16, 32, 5)     |16\*14\*14| 32\*10\*10    |relu|
| MaxPool2 | (2, 2)          |32\*10\*10| 32\*5\*5      ||
| FC1 | (32\*5\*5, 120) |32\*5\*5| 120           |输入要先将所有维度的向量展平成一维,relu|
| FC2 | (120, 84)       |120| 84            |relu|
| FC3 | (84, 10)        |84| 10            |输出的类别的数目|

使用的数据集是 CIFAR10













