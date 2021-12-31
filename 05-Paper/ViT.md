# AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE



## Abstract

Transformer在NLP任务上几乎是一种标准的模型，但是在CV领域中还是有比较多的限制。在视觉领域通常Transformer是和CNN一起使用，或是在保持整体架构的同时使用T替换CNN的部分组件。本文直接使用纯T模型在图片的分类任务上得到了很好的性能表现。先在一个大的数据集上训练好，然后将其用到中小模型中也很好的结果。相比CNN使用的计算资源更少。



## 1. INTRODUCTION

受到T在NLP领域的成功，论文将标准的T模型直接用在图片识别，同时尽可能少的改动。为了做到这点，论文是将一张图片分割成多个小块，这类比于原始NLP中发的每个word。使用监督训练的方式训练模型。

在小的数据集的训练效果不是很好，比ResNET低几个点 ，但是在大的数据集（14M-300M images）上可以得到excellent results





## 2. RELATED WORK

Navie self-attention 用在图片处理的话，是需要处理每一个像素和其他所有的像素的相关型，对于真实的图片的尺寸这是不现实的。









##　３. METHOD

模型的设计尽可能的和原始的T一样，从而能够做到开箱即用的优点。



### 3.1 VISION TRANSFORMER (VIT)

![image-20211118121228009](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211118121228009.png)















**MLP**

![image-20211121104035082](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211121104035082.png)

> $ GELU(x)=x\Phi(x)$
>
> Dropout:在一个全连接的网络中，某个神经元的激活值以一定的概率$p$进行工作
>
> Linear: 全连接网络