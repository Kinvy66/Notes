# 深度强化学习的攻击特征

[paper site](https://arxiv.org/abs/1907.09470)

## 〇、摘要

DRL在各种应用中取得了巨大的成功，然而最近研究表明，机器学习模型很容易受到对抗性攻击。一方面，可以通过给观测值添加扰动，另一方面，也是更具实操性的攻击方式，比如操纵环境动态。因此，论文建议从各个角度分析DRL的漏洞，并对潜在的攻击进行彻底的分类。我们对分类学中未探索的领域进行了一组实验。除了基于观察值的的攻击外，论文还提提出了第一个基于行动空间和环境动态的目标攻击。还介绍了基于帧间时间一致性的在线顺序攻击。为了更好地估计黑盒环境下的梯度，我们提出了一种采样策略，并从理论上证明了其有效性和估计误差界。在游戏，机器人控制和制动驾驶进行了实验，以比较不同攻击在各种环境中的有效性。

> keywords:对抗性机器学习，强化学习



## 一、介绍

最近几年，DNN发展快速，在众多的商业系统中多有应用，并且带动了DRL的发展。DRL系统被用于游戏，自动导航，机器人控制等。为利用DRL的特点(通过学习获得一个能够与环境互动并且可获得最大回报的智能体)，工业生产正在把DRL融入到生产系统中。DNN容易受到对抗性干扰，使用DNN感知和决策的DRL也有同样的缺陷。比如，DRL的一个主要缺陷是它严重依赖输入的观察值，因为它是用DNN来带动处理观察值的，此外，由于DRL是训练用来解决顺序决策问题，攻击者可以干扰多个观测值。事实上，由于随机噪声   和对抗性操作以及训练和测试数据的分布可能不同，在对抗环境学习的测率可能是脆弱的。

在本文中，首先介绍了对DRL系统的对抗性攻击的分类研究，其次提出并评估了10中对抗性攻击，以探索分类中以前没有研究过的点。根据受害者模型的细节和攻击者的其他属性，将针对DRL的对抗性攻击进行分类：

1. 根据攻击者能够干扰哪个系统组件分类，这种分类的组织类似于MDP
2. 根据攻击者执行攻击所需的知识分类，通俗来说就是分为白盒攻击和黑盒攻击

现有的干扰观察值的攻击一在每一帧上独立运行的，这种攻击计算量太大以至于无法实时运行本文提出了两种新的==策略==：

1. `N-attack`,训练一个神经网络用来产生一个扰动
2. 利用RL的特性（state不是独立的，后一个state取决与前一个sta和act），提出了`online sequential attacks`. 使用几个帧的信息生成扰动，然后作用到后面的几个帧。



<p style = "color:red ; font-size: 25px" >贡献:</p>

1. 系统的将针对DRL的对抗性攻击进行了分类，并设计和测试了十种新的攻击
2. 提出了在有限计算能力下实施对抗攻击的两种策略：N-attack, online sequential attacks
3. 提出了两种在黑盒攻击中有效的查询方法：基于自适应采样的有限差分方法(SFD),最优帧选择方法
4. 对所提出的梯度估计方法进行了理论分析，证明了其有效性和估计误差界
5. 提出了第一种有针对性的攻击，这种攻击会对DRL的环境干扰，从而是智能体以特定的方式失败，这种方法在实际应用中更为实用。





## 二、相关工作

* **对机器学习模型的攻击**

  从以前的对抗攻击吸取了一些技术，比如FGSM,等参考方法，这些方法本来是用于白盒攻击的，本文将其用于黑盒攻击



* **对DRL模型攻击**

  <span style= "color: orange">huang的研究</span>，使用FSGM干扰观测值实现干扰，然而这种方法的白盒设置是需要知道训练的模型，最优的动作，并且不清楚攻击者的恶意目标是什么，此外，还提出了一种黑盒攻击（依赖transferability.）。基于这个，本文提出了一种新的黑盒攻击方法（不依赖transferability）。此外，还提出了集中降低计算复杂度的方法。

  <span style= "color: orange">Lin的研究</span>，提出了一种算法实现了对DRL的目标攻击，然而，他们的方法只考虑目标攻击并且需要训练一个模型用来预测未来的状态，这是一个计算密集性的任务。

  <span style= "color: orange"> Behzadan and Munir </span>，提出了一种黑盒攻击的方法，该方法是训练另一个DNQ网络用来使得最小化预期回报，这个仍然使用的FSGM作为攻击方法。

  <span style= "color: orange"> Pan</span>，使用候选推断攻击来推断用于训练候选策略的可能动态。



* **通过对抗训练的鲁棒RL**

  各种机器人技术和自动驾驶技术的安全和通用性问题引起了很大关注。了解RL模型怎么被攻击有利与训练更加健壮的模型。

  <span style= "color: orange"> Pinto的研究</span>，提出在训练RL时加入对抗攻击，这样的模型在对动态变化具有鲁棒性。然而，由于他们手动选择perturbations on environment dynamics,他们的攻击不能推广到更广泛的RL系统。此外，他们的方法依赖与准确的environment dynamics，这不适用与现实世界。



## 三、DRL攻击的分类

现有的针对DRL的对抗攻击都是扰动观测值，这的确有比较好的成效。在特定的环境中，对RL的其他环节引入扰动会是怎样的呢？考虑以下情况：

1. 攻击者对agent了解有限
2. 攻击者可以实施实时攻击
3. 攻击者可以引入物理扰动

为了系统探讨者个问题，提出了一个对抗攻击的可能分类



### 1. 攻击组件

第一层，根据攻击者选择攻击MDP中的哪个组件（observations，actions，environment dynamics.）分类，

设定场景，

observations，通过安装病毒改变图像的像素值，无线传输就干扰通信数据。

actions，安装硬件病毒在执行器上，修改动作的输出。比如控制信号由蓝牙方式发出，可攻击蓝牙通信的漏洞

environment ，在自动驾驶中，改变道路的材料表面特性，机器人控制，改变机器人的质量分布



### 2. 攻击者的知识

第二层，根据攻者在进行攻击时需要的信息进行分类，可分为白盒攻击和黑盒攻击。根据攻击者对策略网络架构，权重参数，攻击者是否可以查看网络进行进一步的分类。

白盒攻击：攻击者知道策略网络架构，权重参数，也可以查看网络

黑盒攻击：攻击者不知道策略网络的权重参数，可能可以查看略网络架构



### 3. 进一步的分类

考虑的攻击的附加属性

实时：有些攻击需要实时，快速运行，为每一个步骤生成扰动。将这三个实用属性作为分类的一部分

物理：物理扰动的可行性

时间依赖性：区分每一帧独立的扰动和在线顺序攻击（使用前一帧的信息产生扰动作用与后一帧）。





## 四、强化学习策略的对抗攻击 （方法）

这节开发出了几种具体的攻击，Table 1

![image-20210713111339120](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713111339120.png)





### 1. 攻击State Observations

攻击者使输入 $s\rightarrow \tilde{s}=s+h(s;w)$ , 其中 $h(s;w)$ 是从原始 $s$ 和 $w$ 生成的扰动。 为了使扰动最小，要求

$\rVert h(s;w)\rVert_\infty \leq \epsilon\ ,\epsilon > 0$



#### 1.1 白盒攻击

在这个设置中，假定攻击者知道agent的策略网络 $\pi(a|s)$ , Huang et al. 的研究描述了这种攻击方式，仅在观测值上使用FGSM生成一个白盒扰动。本文复现了这种方法（`obs-fgsm-wb`).这种攻击的应用场景是当我们知道策略网络的架构和参数。这个方法还有一个变体（`obs-cw-wb`)，使用基于优化的方法代替FGSM。

此外，还提出了一种攻击策略N-attacl，$h(s;w)$  是通过一个DNN计算得到的，这个方法叫`obs-nn-wb`.  这种方法是知道策略网络的架构和参数。基于给定的策略 $\pi$ 训练攻击者网络的参数 $w$，以在应用扰动时最小化被攻击者策略的预期回报：
$$
w= \underset{w}{arg\ max} \mathbb E_{\pi(a|\tilde{s})}[\sum_t \gamma^t\tilde{r_t}]=\underset{w}{arg\ max}\mathbb E_{\pi(a|s+h(s,w))}[-\sum_t \gamma^t r_t]
$$
$\overset{\sim}{r}$ 是正的环境奖励，对于固定的被攻击策略 $\pi$ ，这种攻击类似与训练一个策略。例如，在DQN中，目标是基于以下损失函数对 $w$ 执行梯度更新:
$$
L(w)=(Q(s+h(s,w),a)-(\tilde{r}+\gamma\ \underset{a^{'}}{max}\ Q(s^{'}+h(s^{'^2},w^{'}),a^{'})))^2
$$
其中 $Q$ 是被攻击的模型，$s^{'}$ 是当前状态 $s$ 的下一个状态。在使用DDPG的连续控制中，目标是基于以下lossdvw

更新：

 ![image-20210713130109722](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713130109722.png)

其中Q是value function，$\mu$ 是action function



#### 1.2 黑盒攻击

一般来说，RL模型是保密的。对于这种黑箱模型的攻击，需要采取更加复杂的策略。根据攻击者所掌握的信息可以有不同的场景：

首先，攻击者不知道任何模型的信息包括模型架构，参数，甚至查询信息。在这种场景下，攻击者可以通过替代模型来执行“可转移性”的攻击，然后转移到要攻击的模型。 Huang et al介绍了一种利用可转移性的FGSM攻击的黑盒变体，称之为`obs-fgsm-bb`. 这种攻击需要获取原始的训练环境。本文介绍了其他几种新颖的黑盒攻击方法，并提出了提高这些攻击效率的方法。



#### 1.3 基于模仿学习的黑盒攻击 

`obs-imi-bb`这一攻击灵感来自Rusu et al.在策略提炼方面的研究，攻击者训练一个策略 $\hat{\pi}(a|s,\theta)$ 用来模仿被攻击的策略 $\pi$ . 攻击者使用白盒攻击的方式用于 $\hat{\pi}$ 生成一个扰动，然后将扰动用于策略 $\pi$

攻击的细节，在一个DQN的例子中，给一个黑盒策略 $\pi^T$ ,只可以访问其输出。收集一些数据集  $D^T = \{(s_i，q_i)\}_{i=0}^{N}$ ,每个数据样本包含一个观测值 $s_i$ 和一个为规范化的 $Q$ 值向量 $q_i$ 组成，一个值对应一个动作。通过过模仿学习学得一个新策略 $\pi^S(\cdot|s,\theta)$ ,通过对参数 $\theta$ 梯度更新的方式使得以下loss最小：

![image-20210713162413888](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713162413888.png)

$T$ 时被攻击的策略，$S$ 是模仿的策略， $\tau$ 是一个温度系数。这种攻击在我们无法访问策略网络的体系结构或参数，但可以查询网络。



#### 1.4 基于有限差分的黑盒攻击

obs-fgsm-bb 和obs-imi-bb重新训练一个替代的策略。 Bhagoji et al提供了一种有限差分的方法用于DRL系统

（`obs-fd-bb`），这个不需要重新训练一个策略。这种攻击的设定是不知道网络的策略架构和参数，但是可以查询网络，FD的DRL攻击时使用FD来估计输入观测值的梯度，然后执行梯度下降对输入观测值产生扰动动。FD的关键步骤时估计梯度。用 $L$ 表示loss，$s \in \mathbb R^n$ 表示状态输入，规定基向量 $e_i$ 是一个 $d$ 维向量， 第 $i$ 维是 1， 其他全部是0. 有限差分方法通过以下的公式估计梯度：

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713164535748.png" alt="image-20210713164535748" style="zoom: 80%;" />

$\delta$ 是控制估计精度的参数，对于n维数输入，有限差分方法需要2n次查询来获得估计，这对于像图像这样的高维输入是计算密集型的。我们提出了一种采样技术来降低这种计算成本.（见1.5）



#### 1.5 基于自适应采样的有限差分（SFD）

许多的DL模型需要从输入中逐块提取特征，并且具有稀疏的激活图。将CIFAR-10中图像的梯度模式与随机分布的梯度模式进行比较。可以看到大梯度更集中在某个区域，而不像右图分布在整个图像中

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713165925340.png" alt="image-20210713165925340" style="zoom:80%;" />







提出了一种利用这种空间结构来估计梯度的方法。用这种方法，我们首先估计相对与一些随机采样像素的梯度，然后，识别梯度具有高幅值的像素，并且估计周围的梯度。

给定一个函数 $f(\cdot;w): \mathbb R^d \rightarrow \mathbb R^1$ , $w$ 是模型的参数，目标是估计 $f$ 关于输入 $x\in \mathbb R^d$ 的梯度：$\nabla_x\hat{f}(\chi)$ , 把 $f$ 在 $\chi$ 上的梯度的nontrivial dimension定义为 ：$\{j\in\{1,2,\dots,d\};|\nabla_jf(\chi)|\geq\theta\}$, 梯度绝对值大于或等于阈值 $\theta > 0$ ,为了估计梯度的nontrivial dimension ，首先，在 $\{1,\dots,d\}$  中随机抽样 $k$ 个维度，得到一组维度 $S=\{S_1.S_2,\dots,S_k\}$ ，然后用FD估计 $S$ 中维度的梯度，然后选中一组维度 $S^{'}=\{j\in S;| \nabla_jf(X;w)|\geq \theta \}$ ,使用FD估计 $S^{'}$相邻维度 $S^{''}$的梯度。具体的算法 `obs-sfd-bb` ,这个和obs-fd-bb是工作与同样的场景

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713174742777.png" alt="image-20210713174742777" style="zoom:80%;" />



几个相关定义：(Neighbor Dimension’s Gradient，Non-trivial Gradient Dimension，Gradient Sample Probability

引理1

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713180114830.png" alt="image-20210713180114830"  />

定理2：

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210713180223113.png" alt="image-20210713180223113" style="zoom:95%;" />





#### 1.6 在线顺序攻击

在DRL的环境中，观测值不是独立同分布的，相反他们是高度相关的，每个状态取决于之前的状态。这样就可能比在每个独立的状态上执行攻击的计算量更少。例如，自主机器人可以将实时视频作为输入来帮助做决策，攻击者的动机是仅基于以前的状态生成扰动，并将其应用于未来的状态，我们称之为在线顺序攻击。我们假设以这种方式产生的扰动对后续状态有效。



#### 1.7 基于接近攻击的方法

利用观测的结构，提出了 obs-seq-fgsm-wb, obs-seq-fd-bb, obs-seq-sfd-bb.   obs-seq-fgsm-wb是在标准的白盒环境中，obs-seq-fd-bb 和obs-seq-sfd-bb 工作环境和 obs-fd-bb 一致。在这些攻击中，首先收集 $k$ 个观察帧，并使用这些帧上的平均梯度生成单个扰动。然后将这些扰动应用与后续的帧。

在 `obs-seq-sfd-bb` 中，将接近攻击方法和自适应采样技术结合起来用于有限差分估计。通过找到最重要的一组帧并使用这些帧的梯度来改进上述攻击。我们希望保持攻击的有效性，同时减少所需的查询次数。

推论3：





### 2. 对动作的攻击

这是第二类攻击时直接攻击动作输出，最小化预期回报。在白盒场景下对这一类别的中攻击进行了实验（`act-nn-wb`). 这里我们训练了一个策略网络，它接受状态 $s$ 并输出对 $Q$ 函数的扰动: $Q^{'}(s,a,w)$ , 目标也是最小化预期回报。

例如，在 DQN 中 ， loss:$L(w)=(Q(s,a)+Q^{'}(s,a,w)-\tilde r - \gamma\ max_{a^{'}}(Q(s^{'},a^{'})+Q^{'}(s^{'},a^{'},w)))^2$

对于 DDPG loss：$L(w)=(Q(s,a=\mu(s))+Q^{'}(s,a=\mu(s),w)-\tilde r - \gamma(Q(s^{'},a^{'}=\mu(s^{'}))+Q^{'}(s^{'},a^{'}=\mu(s^{'}),w)))^2$

其中 $\tilde r=-r$

> This second approach to learn the attack h is to treat the environment and the original policy π together as a new environment, and view attacks as actions.





### 3.对环境的攻击

第三类，攻击扰乱环境，需要实现目标攻击，使agent被干扰到指定的类。定义 environment dynamics ：$\mathcal M$

agent的策略：$\pi$ , $s_t$ 表示第 $t$ 步的状态 $s$ ，定义映射 $\pi ,\mathcal M \rightarrow s_t:s_t \sim f(s_t|\pi,\mathcal M,s_0)$

在给定的初始 $s_0, \pi,\mathcal M$ 第 $t$ 步输出的状态为 $s_t$. 攻击的任务使找到另外一个 $\mathcal M^{'}$ 使agent在第 $t$ 步达到目标状态 $s_t^{'}$ 

$\mathcal M^{'}=arg\ min_{\mathcal M}\rVert s_t^{'}-\mathbb E_{s_t\sim f(s_t|\pi,\mathcal M,s_0)}[s_t]\rVert$ 



#### Random dynamics search

在`env-rand-bb` 中演示了一种非常简单的寻找dynamics 的方法（随机搜索）。具体做法是随机生成一个dynamics，然后看agent是否会到我们设定的状态 $s_t^{'}$ ，测试环境是黑盒。



#### Adversarial dynamics search

设计了一种基于RL的算法用来搜索dynamics（`env-search-bb`).在每个步骤，攻击者会对环境做出一些扰动改变$\Delta \mathcal M$,  $\rVert \Delta \mathcal M/ \mathcal M \rVert$ 受限与某个常数 $\epsilon$. 我们发现在环境 $\mathcal M^{'} =  \Delta \mathcal M+ \mathcal M$ 新的 $s_t, \mathcal M^{'}$ 会遵循当前策略。然后攻击agengt会获得  $\overset{\sim}{r}=1/ \rVert s_t,\mathcal M^{'}-s_t^{'}\rVert $ .在env-search-bb中使用了DDPG训练攻击者。为了证明这个方法有效，还和env-rand-bb进行了比较。





## 五、实验

实验部分，攻击了五种不同环境训练的RL：Atari games Pong （<span style="color:aqua;"> DQN</span>），Enduro [3]（<span style="color:aqua;"> DQN</span>）, HalfCheetah（<span style="color:aqua;"> DDPG</span>） ， Hopper in MuJoCo [34]（<span style="color:aqua;"> DDPG</span>）, the driving simulation TORCS [28]（<span style="color:aqua;"> DQN</span>）. 对于这些agent的训练使用不同的随机种子和不同的架构。具体细节在附录



### 1. 实验设计

比较了所有的agent在攻击下和没有攻击下的性能表现，没有攻击用 `non-adv` 表示。



#### 1.1 攻击观测值

Atari games 和MuJoCo simulations 设置 $\epsilon = 0.005,\ 0.01$ , TORCS.为 $\epsilon = 0.05,\ 0.1$

1. 首先在五种环境中测白盒攻击obs-fgsm-wb 和obs-nn-wb 
2. 在两种不同的环境测试obs-fgsm-bb，第一种环境，攻击者和被攻击的agent使用相同的网络，第二种环境，使用不同的我网络
3. 测试obs-imi-bb在五种不同的环境，同样是使用相同和不同的网络架构，使用FGSM生成扰动
4. 





#### 1.2 攻击action

> We test the action selection attack act-nn-wb on the Atari games, TORCS, and MuJoCo robotic control tasks.



#### 1.3 攻击环境





### 2. 实验结果



#### 1. Attacks on observation

Torcs的攻击结果：

![image-20210714175620909](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210714175620909.png)







## 六、结论

论文虽然是在讨论关于 DRL的对抗性攻击，但是一个重要的方向是为了开发更加健壮的RL以更好的给防御攻击。以下是一些观点的讨论

* 试图研究更加泛化的攻击：具有不同的攻击方式的结合体，可以扰动RL的不同部分，并使用新技术降低计算成本。在实验中并没有穷举所有可能的攻击，一个通用的攻击者可以获取RL的多个部分的信息，并可以利用新技术计算有效的扰动。

* 改善RL的鲁棒性，



* 针对特定攻击的防御优先级



* 潜在防御

