# 用于多智能体协同的双层演员-评论家算法（Actor-Critic）



## 摘要

协调是多智能体系统的基本问题之一。通常情况下，多智能体强化学习（MARL）方法对智能体一视同仁，其目标是在存在多个均衡时，将马尔可夫博弈解为任意纳什（Nash）均衡（NE），但是缺少NE选择的解决方案。在本文中，我们并不是平等的对待智能体，根据帕累托（Pareto）最优把斯塔克伯格（Stackelberg  ）均衡作为一个潜在的比Nash均衡更好的收敛点，特别是在多智能体协调的环境中。在马尔可夫博弈中，我们定义了寻找Stackelberg均衡的双层强化学习问题。我们提出了一种新的双层AC学习方法，允许智能体拥有不同的知识库（因此是智能的），同时他们的行为仍然可以同时和分布式执行。我们发现，所提出的双层AC算法在矩阵博弈中成功地收敛到Stackelberg均衡，并在高速公路汇流环境中找到了一个非对称解。



## 介绍

在多智能体系统中，任何智能体的动作对环境的影响也取决于其他智能体执行的动作，需要协调一致地打破同样好的行动或策略之间的联系（Bu et al. 2008）。这个问题非常重要，尤其是在智能体无法通信的情况下。在博弈论中，协调博弈被定义为具有多个纳什均衡的博弈。博弈论文献中提出了纳什均衡选择的各种标准，如显著性（Vanderschraaf 1995）和公平性（Rabin 1993），其中假智能体在应用这些标准之前知道博弈模型。对于智能体无法了解博弈模型，但可以通过与环境的交互学习博弈模型的情况，提出了多智能体强化学习方法来寻找纳什均衡，包括Nash Q-learning（Hu and Wellman 2003），MADDPG（Lowe et al.2017）和MeanField Q-learning (Yang et al. 2018)。这些无模型方法集中训练之虐成收敛到纳什均衡，然后分布式执行智能体。然而，这些方法不能保证特定的收敛纳什均衡，从而导致不确定性和次优性。

为了解决这个问题，我们从非对称的角度重新考虑协调问题。虽然原始博弈模型是对称的，即智能体同时做出决策，但我们仍然能够在训练阶段为智能体定义决策优先级，并在执行阶段保持同步决策。在这个不对称的博弈模型中，Stackelberg均衡（SE）自然地被设定为学习目标，而不是纳什均衡。SE优化了领导者的策略，因为跟随者总是执行最佳响应策略。尽管对跟随者有歧视，但我们惊讶地发现SE在一个大环境中比NE更优越。例如，在合作博弈中，SE保证是帕累托最优的，而只有一个NE达到这一点，如表1a所示。在表1b所示的非合作情况下，SE不包括在NEs集合中，并且是帕累托优于任何NE的。总体而言，我们的实证研究表明，在合作水平较高的博弈中，SE可能比平均NE更具帕累托优势。

![image-20220412095946020](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220412095946020.png)

<div align="center" > 
    表1： 协调博弈。(a)A-X, C-Z 是NE, C-Z是SE和Perato最优点 <br>
     （b）非协调博弈,A-X是SE,B-Y和C-Z是NE.在这个博弈中，SE比<br>
    任何NE都要优越。
</div>

为了解决SE问题，提出了多种双层优化方法（Dempe 2018）。然而，我们的问题设置在两个方面不同于传统的双层优化问题。1）我们考虑一个多状态的环境，其中目标函数是一个连续的折扣奖励的总和；2） 我们的游戏模型是未知的，只能通过互动学习。实际上，传统的双层优化问题可以看作是基于模型的无状态问题。我们将问题正式定义为双层强化学习问题，并提出了一种新的双层actorcritic算法来解决该问题。我们集中训练跟随者的Actor和两个智能体的Critic，以找到一个SE，然后分别执行智能体。我们在小型环境和模拟高速公路合并环境中的实验证明了我们算法的有效性，性能上算是一个SOAT（the state-of-the-art）算法。



## 前置知识

### 马尔可夫博弈（Markov Game）

在一个 $n$ 个玩家的马尔可夫博弈（Littman 1994）（或者随机博弈） $\langle \mit{S},A_i,P,R_i,\gamma  \rangle$ , $S$ 表示状态空间，$A_i$ 表示第 $i$ 个智能体的动作空间，$A$ 表示联合动作空间，$P:S\times A \rightarrow PD(S)$ 表示转移函数，$R_i : S\times A_i \rightarrow \mathcal{R}$ 表示智能体 $i$ 的奖励函数，$\gamma$ 表示折扣因子。智能体在每个状态都会根据自己的策略 $\pi_{i}:S\rightarrow PD(A_i)$ 同时执行动作。智能体的目标是最大化累积奖励 $\sum_t\gamma_{t}r_i^t$ ，$r_i^t$ 是智能体在每个时间步$t$ 的奖励。我们把马尔可夫博弈叫做多智能体强化学习问题（MARL）。



### MARL 相关的解决

对于马尔可夫博弈，我们使用贝尔曼方程描述最优动作-价值函数 $V_i^*(\mathcal{s})$ 和最优动作-价值函数 $Q_i^*(\mathcal{s},a)$ :
$$
Q_i^*（\mathcal{s},\vec{a})=R(\mathcal{s},\vec{a})+\gamma\sum_{s^{'}}P(\mathcal{s},\vec{a},\mathcal{s}^{'})V_i^*(\mathcal{s^{'}})
$$
Minimax-Q方法（Littman 1994）试图找出零和博弈中的最高最坏情况值，其状态-价值函数计算如下：
$$
V_1^*=\underset{\pi_1\in\prod_1}{max}\  \underset{a_2\in A_2}{min}\ Q_1^*(\mathcal{s},\pi_1,a_2)=-V_2^*(\mathcal{s})
$$
其中 $Q_1^*(\mathcal{s},\pi_1,a_2)=\sum_{a_1\in A_1}\pi_1(\mathcal{s},a_1,a_2)$ ,  $\prod_1$ 表示智能体1的策略空间。 我们的双层方法将极大极小方法从零和对策推广到一般和对策。

Nash-Q方法（Hu和Wellman 2003）试图找到纳什均衡，其状态-价值函数计算如下：
$$
V_i^*=NASH_i(Q_1^*(\mathcal{s}),Q_2^*(\mathcal{s}),\dots,Q_n^*(\mathcal{s}))
$$
其中 $NASH_i(\vec{x}_1,\vec{x}_2,\dots,\vec{x}_n)$ 表示第 $i$ 个智能的回报在矩阵博弈中的纳什均衡。Nash-Q方法也将极大极小方法推广到一般和博弈，但方向与我们的方法不同。我们的双层方法试图找到斯塔克伯格均衡，而不是纳什均衡。

### 双层优化

在本文中，我们假设两人马尔可夫博弈中的主体是不对称的，即后面的智能体观察前面的智能体的动作，从而解决马尔可夫博弈的双层优化问题。原始的双层优化问题公式如下：
$$
\begin{aligned}
 \underset{x_1}{\tt{min}} \quad & f_1(x_1,x_2)\\
 s.t. \quad &g_1(x1, x2) \leq 0\\
&\begin{aligned}
\underset{x_2}{\tt{min}}& \quad f_2(x_1,x_2)\\
 s.t. &\quad g_2(x_1,x_2) \leq 0
\end{aligned}
\end{aligned}
$$
其中 $f_i,i=1,2$ 是目标函数，$g_i,i=1,2$ 是每一层的约束函数。

双层优化问题可以等价地描述为一个Stackelberg博弈，其中上层优化器是领导者，下层优化器是追随者，双层优化问题的解是Stackelberg均衡。



## 双层强化学习

### 问题描述

将双层优化与马尔可夫博弈相结合，公式（4）$x_i$ 对应第 $i$ 个智能体的策略 $\pi_i$ , $f_i$ 对应第 $i$ 个智能体的累积奖励，$g_i$ 对应动作空间的约束。假设智能体 1 作为领导者，智能体 2 作为跟随者，我们问题可以描述为：
$$
\begin{aligned}
\underset{\pi_1}{\tt{max}} \quad & \mathbb{E}_{r_1^1,r_1^2\dots\sim\pi_1,\pi_2}
\sum_{t=1}^{\infty}\gamma_tr_1^t\\
\text{s.t.} \quad & \pi_1\in \prod\nolimits_1 \\
&\begin{aligned}
\underset{\pi_2}{\tt{max}}  \quad & \mathbb{E}_{r_1^1,r_1^2\dots\sim\pi_1,\pi_2}
\sum_{t=1}^{\infty}\gamma_tr_1^t\\
\text{s.t.} \quad  &\pi_2\in \prod\nolimits_2 \\
\end{aligned}

\end{aligned}
$$
我们把这个问题叫做双层强化学习（bi-level reinforcement learning ，BiRL）。BiRL可以被视为Stackelberg博弈的多状态版本（Von Stackelberg 2010），并在扩展了标准的双层优化问题，包括1）目标是连续状态下折扣奖励的总和，2）目标函数的形式未知，只能通过与环境的无模型交互来学习。标准的双层优化问题可以被视为我们问题的一个基于模型的无状态版本



### 斯塔克伯格（Stackelberg）均衡与纳什（Nash）均衡

我们定义了BiRL来解决MARL中的协调问题。在博弈论中，协调博弈被定义为一个具有多个纳什均衡的博弈，协调问题可以看作是一个纳什均衡选择问题。在本文中，我们考虑Stackelberg平衡作为协调博弈的一个潜在更好的解决方案。图1是展示马尔可夫博弈中NE和SE之间差异的示例。我们发现SE比NE有两个优势。

![image-20220412101532083](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220412101532083.png)

<div align='center'>
     图1：BiRL的一个协调博弈例子
</div>

SE的第一个优点是确定性或唯一性。博弈中可能存在多个NE，而多个SE仅在非常严格的条件下存在。现有的MARL方法主要收敛于任意NE，这导致了不确定性。由于SE在大多数博弈中都是独一无二的，因此作为学习目标更清晰、更稳定。通过将SE设置为目标，我们实际上试图避免协调问题（或NE选择问题），而不是解决它。

SE的第二个优点是性能。就帕累托最优而言，在协调环境中，SE可能比平均NE获得更好的回报。一个极端的例子是合作博弈。在合作博弈中，SE总是达到帕累托最优点，而只有最好的NE达到帕累托最优点，如表1b和图1所示。换句话说，领导者和追随者在SE中获得的回报都高于平均NE。我们直觉地认为，在合作水平较低（但仍较高）的博弈中，这一结果仍然有效。

为了证明我们的观点，我们将两人马尔可夫博弈的合作水平正式定义为智能体累积奖励之间的相关性：
$$
CL=\frac{\sum_{\vec\pi}(V_1^{\vec\pi}-\bar{V}_1)(V_2^{\vec\pi}-\bar{V}_2)}
{\sqrt{\sum_{\vec\pi}(V_1^{\vec\pi}-\bar{V}_1)^2(V_2^{\vec\pi}-\bar{V}_2)^2}}
$$
其中 $V_i^{\vec\pi}$ 是 $V_i^{\vec \pi}(s_0)$ 的缩写，表示智能体使用策略 $\vec{\pi}$  从初始状态 $s_0$ 开始的累积折扣奖励，并且 $\bar{V}_i=\frac{1}{\vec \pi}\sum_{\vec \pi}V_i^\vec \pi$. 在此定义下，合作博弈和零和博弈的合作水平分别为1和-1。

我们研究了博弈的合作水平与智能体在平均NE和SE中获得的平均收益之间的关系。图2中的结果表明，领导者和跟随者在SE中不仅在完全合作的博弈中，而且在高合作水平的博弈中都获得了更高的回报。

![image-20220412101740362](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220412101740362.png)

<div align='center'>
     图2：SE与NE
</div>

我们还发现，博弈中的纳什均衡数与合作水平呈正相关，这表明在合作水平较高的博弈中更容易出现协调问题。因此，我们认为，在协调问题上，特别是在高度合作的博弈中，SE可能总体上优于平均NE。



### 双层表格Q学习

与minimax-Q和Nash-Q类似，我们可以通过指定计算方法来定义双层Bellman方程：
$$
V_i^*(s)=Stackelberg_i(Q_1^*(s),Q_2^*(s))
$$
其中 $Stackelberg_i(\vec x_1,\vec x_2)$ 表示第 $i$ 个智能体在矩阵博弈中的Stackerberg 均衡由 $\vec x_1, \vec x_2$ 构成。

基于双层贝尔曼方程，我们可以通过等式（1）和（7）迭代更新Q值。形式上，我们有 $Q_1$ 和 $Q_2$ 表的更新规则，给定学习率为 $\alpha_i$ 的转移 $〈s,a_1,a_2,s^′,r_1,r_2〉$：
$$
\alpha_1^{'} \leftarrow \underset{a_1}{\tt{argmax}}\ Q_1(s^{'},a_1,
\underset{a_2}{\tt{argmax}}\ Q_2(s^{'},a_1,a_2)),
$$

$$
\alpha_2^{'} \leftarrow \underset{a_2}{\tt{argmax}}\ Q_2(s^{'},a_1^{'},a_2),
$$

$$
Q_1(s,a_1,a_2) \leftarrow  (1-\alpha_1)Q_1(s,a_1,a_2) 
  +\alpha_1(r_1+\gamma Q_1(s^{'},a_1^{'},a_2^{'}))
$$

$$
Q_2(s,a_1,a_2) \leftarrow  (1-\alpha_2)Q_2(s,a_1,a_2) 
  +\alpha_2(r_2+\gamma Q_2(s^{'},a_1^{'},a_2^{'}))
$$

在（Littman and Stone 2001）和（Kononen 2004）中也对这种表格法进行了研究.然而，这些工作主要集中在解决不对称问题上，而我们的动机是使用不对称方法解决对称协调问题。



### 双层演员-评论家（Actor-Critic）

在公式（8）中，我们需要列举两个级别的动作，以选择动作 $a_1^{'}$，这将导致对$Q_2$表的 $| A1 |·| A2 |$ 访问。当$Q_2$由近似函数（即神经网络）建模时，公式（8）的计算可能会很耗时。此外，如果我们将双层Q-learning方法扩展到多层，$a_1^{'}$的计算复杂度将指数增加。

为了解决这个问题，我们提出了双层演员-评论家方法（Bi-AC），该方法在保持领导者为Q学习者的同时，为跟随者引入一个演员。形式上，设 $π2(s,a1;φ2)∈ PD(A2)$表示智能体2的策略模型（或参与者），它将智能体1的动作作为当前状态之外的输入。我们还使用两个智能体的近似函数对这两个评论家进行建模。对于学习率为 $αi$，$β$ 的转移$〈s,a_1,a_2,s^′,r_1,r_2〉$，我们有以下更新规则：
$$
\alpha_1^{'} \leftarrow \underset{a_1}{\tt{argmax}}\ Q_1(s^{'},a_1,\pi_2(s^{'},a_1; \phi_2);
\theta_1),
$$

$$
\alpha_2 \leftarrow \pi_2(s^{'},a_1; \phi_2),
$$

$$
\delta_i \leftarrow r_i + \gamma Q_i(s^{'},\vec a^{'};\theta)
-Q_i(s,\vec a; \theta_i),i=1,2,
$$

$$
\theta_i \leftarrow \theta_i + \alpha_i\delta_i\nabla_{\theta_i}
Q_i(s,\vec a; \theta_i), i = 1, 2,
$$

$$
\phi_2 \leftarrow \phi_2 + \beta\nabla_{\phi_2}\log\pi_2(s,\vec a;\phi_2)Q_2(s,
\vec a; \phi_2)
$$

其中 $π^′_2(s,a_1;φ2)$ 由Gumbel Softmax估计器（Jang，Gu和Poole 2016）建模，该估计器直接计算 $a_2^{'}$. 

对于具有连续动作空间的环境，我们使用确定性模型μ2（s，a1；φ2）对agent 2的策略进行建模∈ A2，由确定性政策梯度法更新（Silver等人，2014年）。agent 1的Q网络可以通过软Q学习（Haarnoja et al.2017）方法进行更新。































