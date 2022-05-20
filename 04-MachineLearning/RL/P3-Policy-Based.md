# Policy-Based RL

参考 ：https://github.com/wangshusen/DeepLearning



## Policy Function Approximation

**Policy Function**  是一个概率密度函数（PDF）
$$
\pi( {\color{red}a} \vert {\color{green}{s}})
$$
策略函数输入当前的状态，输出所有动作的概率值，再随机抽样动作



## Policy Network  $\pi( {\color{red}a} \vert {\color{green}{s}}; \theta) $

**策略网络**： 使用一个神经网络来近似  $\pi( {\color{red}a} \vert {\color{green}{s}})$

- 在状态和动作是有限的情况下，我们可以用列表格的形式把所有的状态和对应的动作的概率值列出来。

- 在不可列举的情况下，使用策略网络 $\pi( {\color{red}a} \vert {\color{green}{s}}, \theta) $ 近似 $\pi( {\color{red}a} \vert {\color{green}{s}})$ ，其中 $\theta$ 是神经网络的参数



## State-Value Function Approximation



### Action-Value Function

- **Definition： 折扣回报**
  $$
  U_t = R_t + \gamma\cdot R_{t+1} + \gamma^{2}\cdot R_{t+2}
  +\gamma^{3}\cdot R_{t+3}
  $$
  $U_t$ 依赖于动作  ${\color{red}{A_t}}, {\color{red}{A_{t+1}}}, {\color{red}{A_{t+2}}},  {\color{red}{\cdots}}$  和状态  ${\color{green}{S_t}}, {\color{green}{S_{t+1}}}, {\color{green}{S_{t+2}}},  {\color{green}{\cdots}}$ 





- **Definition： Action-Value Function**
  $$
  Q_{\pi}({\color{green}{s_{t}}},{\color{red}{a_t}}) 
  = \mathbb{E}[U_t\vert {\color{green}{S_t = s_t}}, {\color{red}{A_t=a_t}}]
  $$
  求期望把未来时刻的 ${\color{green}{S}}, {\color{red}{A}}$ 都消掉了，使得 $Q_{\pi}$ 只依赖于当前时刻的  ${\color{green}{S}}, {\color{red}{A}}$ 

  不同的 $\pi$ ， $Q_{\pi}$  的值不一样， $Q_{\pi}$ 可以衡量在状态 ${\color{green}{S}}$  做出动作 ${\color{red}{A}}$  的好坏程度



- **Definition： State-Value Function**
  $$
  V_{\pi}({\color{green}{s_t}})=\mathbb{E}_{{\color{red}{A}}}[Q_{\pi}({\color{green}{s_t}}, {\color{red}{A}})]
  $$
  对 $Q_{\pi}$ 关于 $\color{red}{A}$ 求期望，就是对动作积分  ${\color{red}{A}} \sim \pi(\cdot \vert {\color{green}{s_t}})$ ，$V_{\pi}$ 只跟策略 $\pi$ 和当前状态 $\color{green}{s_t}$ 有关。

  给定策略 $\pi$ ，$V_{\pi}$  可以评价当前状态的好坏； 给定状态 $\color{green}{s}$ ，$V_{\pi}$ 可以评价策略的好坏。

  对于离散的情况
  $$
  V_{\pi}({\color{green}{s_t}})=\mathbb{E}_{{\color{red}{A}}}[Q_{\pi}({\color{green}{s_t}}, {\color{red}{A}})]
  =\sum_{{\color{red}{a}}} \pi({\color{red}{a}}\vert {\color{green}{S_t}})\cdot
  Q_{\pi}({\color{green}{s_{t}}},{\color{red}{a_t}})
  $$





## Policy-Based RL

State-Value Function
$$
V_{\pi}({\color{green}{s_t}})=\mathbb{E}_{{\color{red}{A}}}[Q_{\pi}({\color{green}{s_t}}, {\color{red}{A}})]
=\sum_{{\color{red}{a}}} \pi({\color{red}{a}}\vert {\color{green}{s_t}})\cdot
Q_{\pi}({\color{green}{s_{t}}},{\color{red}{a_t}})
$$
**Approximate State-Value Function**

- 通过 policy network $\pi( {\color{red}a} \vert {\color{green}{s_t}}; \theta)$ 近似策略函数  $\pi( {\color{red}a} \vert {\color{green}{s_t}})$

-  $V_{\pi}({\color{green}{s_t}})$ 可写成
  $$
  V_{\pi}({\color{green}{s_t}}; \theta) 
  =\sum_{{\color{red}{a}}} \pi({\color{red}{a}}\vert {\color{green}{s_t}}; \theta)\cdot
  Q_{\pi}({\color{green}{s_{t}}},{\color{red}{a_t}})
  $$
  其中 $\theta$ 是神经网络的参数

**Policy-based learning**  学习一个参数 $\theta$ 使得下式最大
$$
J(\theta)=\mathbb{E}_{{\color{green}{S}}} [V({\color{green}{S}}; \theta)]
$$
使用策略梯度上升的算法改进 $\theta$ 

- 观察状态 $\color{green}{S}$

- 更新策略： 
  $$
  \theta \leftarrow \theta + \beta\cdot \frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta}
  $$
  $\frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta}$ ： Policy gradient

 

## Policy Gradient

**近似状态价值函数**
$$
V({\color{green}{s}}; \theta)
=\sum_{{\color{red}{a}}} \pi({\color{red}{a}}\vert {\color{green}{s_t}}; \theta)\cdot
Q_{\pi}({\color{green}{s_{t}}},{\color{red}{a_t}})
$$
**Policy gradient：** 求导 $V({\color{green}{s}}; \theta)\ \text{w.r.t.} \ \theta$
$$
\begin{align}
\frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta}
& = \frac{\partial\ \sum_{{\color{red}{a}}}\pi({\color{red}{a}}\vert {\color{green}{s}};\theta)\cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}})}{\partial \ \theta} \\
& = \sum_{{\color{red}{a}}} \frac{\partial\ \pi({\color{red}{a}}\vert {\color{green}{s}};\theta)\cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}})}{\partial \ \theta} 
\ \text{提出连加} \\
& = \sum_{{\color{red}{a}}} \frac{\partial\ \pi({\color{red}{a}}\vert {\color{green}{s}};\theta)}{\partial \ \theta} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}})
\ \text{假设 $Q_{\pi}$ 不依赖于$\theta$}   \\
\end{align}
$$
这样就得到了策略梯度的公式
$$
\begin{align}
\frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta}
& = \sum_{{\color{red}{a}}} \enclose{box}{\frac{\partial\ \pi({\color{red}{a}}\vert {\color{green}{s}};\theta)}{\partial \ \theta}} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}}) \\
& =\sum_{{\color{red}{a}}} \ 
\enclose{box}{ 
\pi({\color{red}{a}}\vert {\color{green}{s}};\theta) \cdot \frac{\partial\ \log \pi({\color{red}{a}}\vert {\color{green}{s}}; \theta)}{\partial\ \theta}
} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}}) \\
& = \mathbb{E}_{{\color{red}{A}}} [\frac{\partial\ \log \pi({\color{red}{A}}\vert {\color{green}{s}}; \theta)} {\partial\ \theta} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{A}})]
\end{align}
$$
式 (14) 到 (15) 可从下往上进行验证
$$
\text{链式法则：} \frac{\partial \ \log[\pi(\theta)]}{\partial\ \theta} = \frac{1}{\pi(\theta)}
\cdot \frac{\partial \ \pi(\theta)}{\partial\ \theta} \\
\Rightarrow \ \pi(\theta)\cdot \frac{\partial \ \log[\pi(\theta)]}{\partial\ \theta} 
= \bcancel{\pi(\theta)} \cdot \frac{1}{\bcancel{\pi(\theta)}} \cdot \frac{\partial \ \pi(\theta)}{\partial\ \theta} 
= \frac{\partial \ \pi(\theta)}{\partial\ \theta}
$$


**综上** 策略梯度的两种等价形式
$$
\begin{align}
\text{Form 1: } \frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta} 
& = \sum_{{\color{red}{a}}} \frac{\partial\ \pi({\color{red}{a}}\vert {\color{green}
{s}};\theta)}{\partial \ \theta} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{a}})\\
\text{Form 2: } \frac{\partial\ V({\color{green}{s}};\theta)}{\partial\ \theta} 
& = \mathbb{E}_{{\color{red}{A }}\sim \pi(\cdot \vert{\color{green}{s}};\theta)} [\frac{\partial\ \log \pi({\color{red}{A}}\vert {\color{green}{s}}; \theta)} {\partial\ \theta} \cdot Q_{\pi}({\color{green}{s}},{\color{red}{A}})]
\end{align}
$$
公式(1) 用于动作空间式离散的， 公式(2) 用于动作空间式连续的











