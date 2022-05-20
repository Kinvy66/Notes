# 强化学习

参考 ：https://github.com/wangshusen/DeepLearning

## 1. 基本概念

我们使用大写字母，比如 $X$ ，表示随机变量，用小写字母，比如 $x$ ，表示随机变量的观测值。$\mathbb{P}(X=x)$ 是事件   "$X=x$"  的概率。$\mathbb{P}(Y=y \lvert X=x)$ 是条件概率，在事件 "$X=x$" 发生的情况下 "$X=x$" 发生的概率。



**Agent**: 智能体，在一个环境中执行动作改变环境的状态。比如机器人，工业控制器，超级玛丽里面的马里奥。



**State $(S)$** : 状态，状态可以看作是对系统历史的总结以及对决定未来会怎么变化。$\text{State space}\ \mathcal{S}$  （状态空间 $\mathcal{S}$ ）包含了所有可能状态的集合。在时间步 $t$ ，可以观察到的过去状态为： $s_1, \cdots , s_t$ ; 但是未来的状态 $S_{t+1},S_{t+2},\cdots$ 是无法观察到的随机变量。



**Action $(A)$** : 动作，agent决策是基于状态和其他一些限制条件。$\text{Action space}\ \mathcal{A}$ （动作空间 $\mathcal{A}$ ）是包含所有动作的集合。动作空间可以是离散的集合比如 $\{\text{“left", “right", “up"}\}$ 或者连续的比如 $[0,1]\times[-90,90]$. 在时间步 $t$ 过去的动作可以观察到：$a_1, \cdots,a_t$ ，但是未来的动作 $A_{t+1},A_{t+2},\cdots$ 是不可观察到的随机变量。



**Reward $(R)$** : 奖励， 奖励是一个值，它是智能体执行了一个动作后环境所给出的一个响应。在时间步 $t$ 所有过去的奖励我们可以得到： $r_1, r_2, \cdots , r_t$ , 但是未来的奖励 $R_i\ (\text{for}\ i>t)$ 是无法得到的，并且它决定于随机变量 $S_{t+1}, A_{t+1}$ ，因此在时间步 $t$ 未来奖励 $R_{t+1}, R_{t+2},\cdots$ 是随机变量。

![image-20220417185058070](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220417185058070.png)

<div align="center">
    图1： 随机性的说明 </br>
    动作 A 是根据策略函数随机采样 </br>
    新的状态 S' 是根据状态转移函数随机采样
</div>
**Policy function $(\pi)$** : 策略函数，策略函数是agent决策的函数。策略是一个概率密度函数（==PDF==）： $\pi (a \lvert s)=\mathbb{P}(A=a \rvert S=s)$.  策略函数是观察到状态 $S=s$ ，将所有的动作集合 $\mathcal{A}$ 映射到一个分布。因为 $\pi$ 是一个概率密度函数 （PDF），$\sum_{a\in\mathcal{A}}\pi(a\lvert s)=1$ . agent 以 $\pi (a\lvert s)$ 的概率执行动作 $a$. 在图1中有说明。



**State transition $(p)$** : 状态转移，给定当前的状态 $S=s$ ，agent执行动作 $A=a$ ，环境会变成一个新的状态 $S^{'}$ . 状态转移函数是一个概率密度函数（==PDF==）$p(s^{'}\lvert s,a)=\mathbb{P}(S^{'}=s^{'}\lvert S =s, A=a)$ . 对所有的 $s^{'}\in \mathcal{S}$ ，环境是以概率 $p(s^{'}\lvert s,a)$ 变成状态 $s^{'}$ .



**Trajectory** : 轨迹，agent和环境交互的结果用 $(\text{state, action, reward})$ 序列表示： $s_1, a_1, r_1, s_2,a_2,r_2,s_3,a_3,r_3,\cdots$



**Return $(U)$** : 回报，也就未来累积奖励，定义为 
$$
U_t=R_t+R_{t+1}+R_{t+2}+R_{t+3}+\cdots
$$
折扣回报（未来累积折扣奖励），定义为：
$$
U_t=R_t+\gamma \cdot R_{t+1}+\gamma^{2}\cdot R_{t+2}+\gamma^{3}\cdot R_{t+3}+\cdots
$$
其中 $\gamma\in(0,1)$ 是折扣因子。回报 $U_t$ 是随机的，因为未来奖励 $R_t,R_{t+1}, R_{t+2},\cdots$ 不可观察到的随机变量。前面有提到过，$R_i (i \geq t)$ 的随机性来自于未来状态 $S_i$ 和动作 $A_i$ . 这里使用折扣因子 $\gamma$ 是基于未来的不确定性这样一个事实，比如现在给你 100 块钱和一年后给你100块钱，你肯定选择现在得到这100. 所以未来奖励肯定没有现在的那么可信，需要打折扣，而且越远的奖励需要大越大的折扣。

> Reward 和 Return的区别， Reward，奖励是表示执行一个动作后环境给出的，可观察到，单步；Return，回报，所以奖励的和，存在随机性且不可观察到。



**Action-value function $(Q_\pi)$** : 动作-价值函数 $Q_\pi(s_t, a_t)$ , 用来衡量给定状态 $s_t$ 和策略 $\pi$ 下，动作 $a_t$ 的好坏程度，公式为：
$$
Q_{\pi}(s_t, a_t)=\mathbb{E}[U_t\lvert S_t=s_t, A_t= a_t]
$$
这是关于随机变量未来动作 $A_{t+1},A_{t+2},\cdots$  和 未来状态 $S_{t+1},S_{t+2},\cdots$ 的表达式。$Q_{\pi}(s_t,a_t)$ 取决于策略函数 $\pi$ 和状态转移概率函数 $p$ .

**Optimal action-value function $(Q^*)$** : 最优动作价值函数 $Q^*(s_t,a_t)$ 是用来衡量在状态 $s_t$ 下执行动作 $a_t$ 有多好
$$
Q^*(s,a)=\underset{\pi}{max}Q_{\pi}(s,a)
$$
 $Q^*(s,a)$ 与策略函数 $\pi$  无关的



**State-value function $(V_{\pi})$** : 状态价值函数 $V_{\pi}(s_{t})$ , 给定策略 $\pi$ 当前的状态有多好
$$
V_{\pi}(s_t)=\mathbb{E}_{A\sim \pi(\cdot \vert s_t)} [Q_{\pi}(s_t,A)]
=\int_{\mathcal{A}}\pi(a\vert s_t)\cdot Q_{\pi}(s_t, a) \,{\rm d}a
$$
这里动作 $A$ 被认为是一个随机变量并且被积分。







