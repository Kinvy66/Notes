# Value-Based RL



参考 ：https://github.com/wangshusen/DeepLearning



## Action-Value Function

- **Definition： 折扣回报**
  $$
  U_t = R_t + \gamma\cdot R_{t+1} + \gamma^{2}\cdot R_{t+2}
  +\gamma^{3}\cdot R_{t+3}
  $$
  $U_t$ 依赖于动作  ${\color{red}{A_t}}, {\color{red}{A_{t+1}}}, {\color{red}{A_{t+2}}},  {\color{red}{\cdots}}$  和状态  ${\color{green}{S_t}}, {\color{green}{S_{t+1}}}, {\color{green}{S_{t+2}}},  {\color{green}{\cdots}}$ 

  动作是随机的：  $\mathbb{P}[{\color{red}{A=a}}\vert {\color{green}{S=s}}] = \pi({\color{red}{a}}\vert{\color{green}{s}})$

  状态是随机的： $\mathbb{P}[{\color{green}{S^{'}=s^{'}}}\vert {\color{green}{S=s}}, {\color{red}{A=a}}]=p({\color{green}{s^{'}}}\vert{\color{green}{s}}, {\color{red}{a}})$




- **Definition:  Action-value function for policy $\pi$**
  $$
  Q_{\pi}({\color{green}{s_t}},{\color{red}{a_t}})
  =\mathbb{E}[U_t\vert {\color{green}{S_t=s_t}}, {\color{red}{A_t=a_t}}]
  $$
    对 $U_t$ 求期望，$\text{w.r.t.}$  动作 ${\color{red}{A_t}}, {\color{red}{A_{t+1}}}, {\color{red}{A_{t+2}}},  {\color{red}{\cdots}}$  和状态  ${\color{green}{S_t}}, {\color{green}{S_{t+1}}}, {\color{green}{S_{t+2}}},  {\color{green}{\cdots}}$ 

  未来的随机性都消除了，$Q_{\pi}$ 只依赖于 $\pi$ 和当前动作，状态 （${\color{red}{A_t=a_t}}, {\color{green}{S_t=s_t}}$）

- **Definition: Optimal action-value function**
  $$
  Q^*({\color{green}{s_t}},{\color{red}{a_t}})
  =\underset{\pi}{\tt{max}}\ Q_{\pi}({\color{green}{s_t}},{\color{red}{a_t}})
  $$
  进一步消除策略函数 $\pi$ ，对 $Q_{\pi}$ 关于 $\pi$ 求最大化， 得到最优动作-价值函数。$Q^*$ 的值告诉我们基于当前状态 $\color{green}{s_t}$ ，执行动作 $\color{red}{a_t}$ 的好坏程度，所以 $Q*$ 可以指导 agent 做决策

  

  

##  Deep Q-Network (DQN)



### Approximate the Q Function



**目标：** 最大化累积奖励

**问题： ** 假设 $Q^*$ 已知， 那么什么是最好的动作？

显然，最好的动作是 ${\color{red}{a^*}}=\underset{{\color{red}{a}}}{\text{argmax}} \  Q^*({\color{green}{s}},{\color{red}{a}}) $ 

但是我们不知道 $Q^*$ ，DQN ，使用神经网络 $Q({\color{green}{s}},{\color{red}{a}}; \tt{w})$  近似 $Q^*({\color{green}{s}},{\color{red}{a}})$

![image-20220512194824400](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512194824400.png)

  

  ## Temporal Difference (TD) Learning

以一个 :chestnut: 说明TD算法

- 开车从 NYC 到 Atlanta
- 模型 $Q(\text{w})$ 估计需要耗时 1000 min

**问题： **我们怎么更新模型



<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512195843037.png" alt="image-20220512195843037" style="zoom:50%;" />

- 完成整个旅程更新？  到达 DC 的时候就更新 $\text{w}$ ？

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512200211649.png" alt="image-20220512200211649" style="zoom:50%;" />

假设我们没有到达 Atlanta， 只到达了 DC， 

- 出发前模型估计需要 1000 min

  <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512200519279.png" alt="image-20220512200519279" style="zoom:50%;" />
  
- 到达 DC 的时候实际花了 300 min

  ![image-20220512200724036](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512200724036.png)

- 模型更新估计， 从 DC 到 Altanta 要 600min

  <img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220512200837486.png" alt="image-20220512200837486" style="zoom:50%;" />

  TD target $y = 300 + 600 = 900$，TD target 明显比一开始的估计 1000 更加可靠，因为 TD target 有一部分 (NYC-DC) 是实际花费的时间



- Loss: $L = \frac{1}{2}(Q({\text{w}}) - y)^2$  ，其中 $Q({\text{w}}) - y$ 是 TD error

  对Loss 求梯度，使用梯度下降方法对 $\text{w}$ 进行更新



## TD Learning For DQN

上面的:chestnut: 
$$
{\color{red}{T_{NYC\rightarrow ATL}}} \
\approx {\color{blue}{T_{NYC\rightarrow DC}}} + {\color{red}{T_{DC\rightarrow ATL}}}
$$
应用到深度强化学习(deep reinforcement learning) 表示为：
$$
{\color{red}{Q(s_t,a_t;\bf{w})}}
\approx {\color{blue}{r_t}} + {\color{red}{\gamma \cdot Q(s_{t+1}, a_{t+1}; \bf(w))}}
$$
TD算法中，等式的右边的两项，其中第一项是实际值，第二项是估计值，在


$$
\begin{align}
U_t 
& = {\color{blue}{R_t}} + {\color{red}{\gamma}} \cdot {\color{blue}{R_{t+1}}}
+{\color{red}{\gamma^2 }} \cdot {\color{blue}{R_{t+2}}}
+{\color{red}{\gamma^3 }} \cdot {\color{blue}{R_{t+3}}}
+{\color{red}{\gamma^4 }} \cdot {\color{blue}{R_{t+4}}} + \cdots \\
& = {\color{blue}{R_t}} 
+ {\color{red}{\gamma}} \cdot 
(\underbrace{
{\color{blue}{R_{t+1}}}
+{\color{red}{\gamma^1 }} \cdot {\color{blue}{R_{t+2}}}
+{\color{red}{\gamma^2 }} \cdot {\color{blue}{R_{t+3}}}
+{\color{red}{\gamma^3 }} \cdot {\color{blue}{R_{t+4}}}
}_{=U_{t+1}}) + \cdots
\end{align}
$$

$$
U_t = {\color{blue}{R_t}} + {\color{red}{\gamma}}\cdot U_{t+1}
$$

**TD learning for DQN : **

- DQN 的输出 $Q({\color{green}{s_t}}{\color{red}{a_t}};\bf{w})$ ,  是 $U_t$ 的估计值

- DQN 的输出 $Q({\color{green}{s_{t+1}}}{\color{red}{a_{t+1}}};\bf{w})$ ,  是 $U_{t+1}$ 的估计值

- 因此 
  $$
  Q({\color{green}{s_{t}}}, {\color{red}{a_{t}}}; {\bf{w}}) 
  \approx {\color{blue}{r_t}} 
  + {\color{maroon}{\gamma}} \cdot 
  Q({\color{green}{s_{t+1}}}{\color{red}{a_{t+1}}}; {\bf{w}})
  $$



**Train DQN using TD learning : **

- Prediction : $Q({\color{green}{s_{t}}}, {\color{red}{a_{t}}}; {\bf{w}}) $

- TD target :
  $$
  \begin{align}
  y_t 
  & ={\color{blue}{r_t}} 
  + \gamma \cdot Q({\color{green}{s_{t+1}}},{\color{red}{a_{t+1}}}; {\bf{w}}_t)\\
  & = {\color{blue}{r_t}} 
  + \gamma \cdot \underset{{\color{red}{a}}}{\text{max}}\  
  ({\color{green}{s_{t+1}}},{\color{red}{a}}; {\bf{w}}_t)
  \end{align}
  $$

- Loss:
  $$
  L_t = \frac{1}{2}[Q({\color{green}{s_{t}}}, {\color{red}{a_{t}}}; {\bf{w}})
  - y_t]^2
  $$

- Gradient descent ：
  $$
  {\bf{w}}_{t+1} = {\bf{w}}_t - \alpha \cdot
  \frac{\partial\ L_t}{\partial\ {\bf{w}}} \Bigg|_{{\bf w}={\bf w}_t}
  $$
  































