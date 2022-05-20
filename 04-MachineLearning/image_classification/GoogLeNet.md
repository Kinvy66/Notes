# GoogLeNet

C. Szegedy *et al.*, “Going deeper with convolutions,” in *2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, Boston, MA, USA, Jun. 2015, pp. 1–9. doi: [10.1109/CVPR.2015.7298594](https://doi.org/10.1109/CVPR.2015.7298594).

ref: [5.1 GoogLeNet网络详解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1z7411T7ie?spm_id_from=333.999.0.0)



**GoogLeNet**

![image-20220228192026871](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228192026871.png)



网络图

![image-20220228191948201](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228191948201.png)

**Inception**（黑框）和 **辅组分类器**(黄框)

![image-20220228192429656](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228192429656.png)

### Inception

![image-20220228192920341](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228192920341.png)

每条分支输出的特征矩阵高和宽必须相等，将所有的分支在深度方向拼接，1\*1的卷积的作用是降维



### 网络详解

![image-20220228194545019](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228194545019.png)



![image-20220228194729299](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220228194729299.png)
