# Proximal Policy Optimization (PPO)

参考：

[1] [李宏毅老师DRL Lecture 2: Proximal Policy Optimization (PPO)](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DOAKAZhFmYoI%26index%3D2%26list%3DPLJV_el3uVTsODxQFgzMzPLa16h6B8kWM_)

[2] [【点滴】策略梯度之PPO - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/43114711)

[3] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal Policy Optimization Algorithms,” Jul. 2017, doi: [10.48550/arXiv.1707.06347](https://doi.org/10.48550/arXiv.1707.06347).



# 目录

[TOC]

## on-Policy and off-Policy

- **On-Policy : ** 智能体学习和交互的环境是一样的（同一个）， 常用的有 Q-learning
- **Off-Policy : ** 智能体学习和交互的环境是不一样的，这里的不一样是指不是同一个环境，但是应该是"相同"的环境。~~比如通过看别人直播学玩游戏，通常我学玩什么游戏就会看什么游戏直播的。~~

PPO就是一种 Off-Policy 的算法。



## Policy Gradient

策略梯度，公式推导参考 [(1) 深度强化学习(3/5)：策略学习 Policy-Based Reinforcement Learning - YouTube](https://www.youtube.com/watch?v=qI0vyfR2_Rc&list=PLvOO0btloRnsiqM72G4Uid0UWljikENlU&index=3&ab_channel=ShusenWang)
$$
g = \nabla J(\theta)
= \mathbb{E}_{(a_t,s_t)\sim \pi(\theta)}[Q_{\pi(\theta)}(s_{t},a_t)\nabla\log\pi_{\theta}(a_t\vert s_t)]
$$
在使用 on-policy的时候，每更新一次参数 $\theta$ 就需要重新重新采样训练数据，而 off-policy 值需要采样一次数据就可以。

 



## Importance Sampling

假设我们需要计算期望值 $\mathbb{E}_{x\sim p}[f(x)]$ ，$p$ 是变量 $x$ 的分布：
$$
\begin{align}
\mathbb{E}_{x\sim p}[f(x)]  
& = \int p(x)f(x)dx  \\
& \approx \frac{1}{N}\sum_{i = 1}^{N}f(x^{i})
\end{align}
$$
期望值可以通过公式(2) 积分得到，如果分布 $p$ 很难积分，我们往往会通过 $p$ 采样来进行期望的估计。但是如果 ![[公式]](https://www.zhihu.com/equation?tex=p) 采样很麻烦，我们就得借助另一个更简单的分布 $q$ 来代为采样了，这就是重要性采样的初衷，具体的关系如下：
$$
\begin{align}
\mathbb{E}_{x\sim p}[f(x)]
& = \int p(x)f(x)dx  \\
& = \int f(x) \frac{p(x)}{q(x)} q(x) dx \\
& = \mathbb{E}_{x\sim q} [f(x)\frac{p(x)}{q(x)}]
\end{align}
$$
所以从 $p$ 中采样转换为从 $q$ 中采样
$$
\mathbb{E}_{x\sim p}[f(x)] = \mathbb{E}_{x\sim q} [f(x)\frac{p(x)}{q(x)}]
$$
理论上可以用任意的 $q$ 替换 $p$ ，但实际上两者相差太大的话，它们的方差会相差较大，下面是$p,q$ 方差计算：

$p$ 的方差
$$
Var_{x\sim p}[f(x)] = \mathbb{E}_{x\sim p}[f(x)^2] 
-(\mathbb{E}_{x\sim p}[f(x)])^2
$$
$q$ 的方差
$$
\begin{align}
Var_{x\sim q} [f(x)\frac{p(x)}{q(x)}] 
& = \mathbb{E}_{x\sim q} 
	\left[ 
		\left(
			fx\frac{p(x)}{q(x)}
		\right)^2
	\right] 
	- \left( 
	  	\mathbb{E}_{x\sim q}
	  	\left[
	  		f(x)\frac{p(x)}{q(x)}
	  	\right]
	  \right)^2 \\
& = \mathbb{E}_{x\sim p}
	\left[
		f(x)^2 \frac{p(x)}{q(x)}
	\right]
	-(\mathbb{E}_{x\sim p}[f(x)])^2

\end{align}
$$
 可以看到 $p, q$ 的方差后面一项是相同的，只有前面一项是不同， 比较 公式(13)(15)。如果两者比较相近，那么它们的方差也会比较接近，否则方差就会相差比较大。





## PPO

已知策略梯度为：
$$
g = \nabla J(\theta)
= \mathbb{E}_{(s_t,a_t)\sim \pi(\theta)}[Q_{\pi(\theta)}
(s_{t},a_t)\nabla\log\pi_{\theta}(a_t \vert s_t)]
$$

**pg实际上就是一种on-policy的学习方法**，我们容易发现采样的策略跟被优化的策略就是是同一个 $\pi$ ，这种做法的一个不足是，每进行一次更新，又得采样，然后进行下一次更新，导致学习效率不高。为了提高学习效率，我们一般先采样多次，再更新，而且我们希望采样的样本可以重复使用，从而节省大量训练成本。为此，需要另一个策略 $\pi ^{'}$ 代为采样，即转换为off-policy的方法，对应的更新梯度变为：
$$
g = \nabla J(\theta)
= \mathbb{E}_{(s_t,a_t)\sim \pi(\theta)^{'}}
\left[
	\frac{\pi(\theta)}{\pi(\theta)^{'}} 
	Q_{\pi(\theta)^{'}}(s_{t},a_t)\nabla\log\pi_{\theta}(a_t\vert s_t)
\right]
$$
由上式，变成**off-policy实际上就是引入了重要性采样，就得考虑之前提到的重要性采样的不足**。



PPO就是为了解决这个不足而产生的，此外，它与传统的策略梯度还有一点点不一样，它考虑的是每步收益会比期望的收益好多少，也就是advantage：
$$
A_{\pi(\theta)}(s_t,a_t)
= Q_{\pi(\theta)}(s_t,a_t)-V_{\pi(\theta)}(s_t)
$$
此时策略梯度可以写为：
$$
g =\nabla J(\theta) = \mathbb{E}_{(a_t,s_t)\sim \pi(\theta)}
[A_{\pi(\theta)}(s_t, a_t)\nabla\log\pi_{\theta}(a_t\vert s_t)]
$$
通过另一个策略帮助采样（重要性采样），$\pi_{\theta}, \pi_{\theta^{'}}$ 是两个不同的策略分布得：
$$
\begin{align}
g & =\nabla J(\theta)\\
 & = \mathbb{E}_{(a_t,s_t)\sim \pi(\theta)^{'}}
\left[
	\frac{\pi_\theta(a_t,s_t)}{\pi_{\theta^{'}}(a_t,s_t)} A_{\pi(\theta)^{'}}
	\nabla\log\pi_{\theta}
\right] \\
& = \mathbb{E}_{(a_t,s_t)\sim \pi(\theta)^{'}}
\left[
	\frac{\pi_\theta(a_t\vert s_t)}{\pi_{\theta^{'}}(a_t\vert s_t)} 
	\bcancel{\frac{\pi_{\theta}(s_t)}{\pi_{\theta^{'}}(s_t)}}
	A_{\pi(\theta)^{'}}
	\nabla\log\pi_{\theta}
\right]  \ \ \text{条件概率公式}  \\   
& = \mathbb{E}_{(a_t,s_t)\sim \pi(\theta)^{'}}
\left[
	\frac{\pi_\theta(a_t\vert s_t)}{\pi_{\theta^{'}}(a_t\vert s_t)} 
	A_{\pi(\theta)^{'}}
	\nabla\log\pi_{\theta}
\right]   \\  
\end{align}
$$




又因为：$\nabla f(x)=f(x)\nabla\log f(x)$  得：
$$
g =\nabla J(\theta) = \mathbb{E}_{a\sim \pi_{\theta^{'}}}
\left[
	\frac{\nabla \pi_{\theta}}{\pi_{\theta^{'}}} A_{\pi(\theta)^{'}}(s_t,a_t)
\right]
$$
:question: 得到一个新得目标函数：
$$
J(\theta ) ^{'}=
\mathbb{E}_{a\sim \pi_{\theta^{'}}}
\left[
	\frac{\pi_{\theta}}{\pi_{\theta^{'}}} A_{\pi(\theta)^{'}}(s_t,a_t)
\right]
$$
为了克服采样分布与原分布差距过大的不足，PPO对采样分布和原分布做了约束，其做法是为目标函数引入KL距离作为正则项：
$$
J_{PPO}(\theta )^{'} =
\mathbb{E}_{a\sim \pi_{\theta^{'}}}
\left[
	\frac{\pi_{\theta}}{\pi_{\theta^{'}}} A_{\pi(\theta)^{'}}(s_t,a_t)
\right]
- \beta KL(\pi_{\theta^{'}}, \pi_{\theta})
$$
这里KL并不是把 $ \pi(\theta)^{'}, \pi(\theta)$  当作两个分布计算他们之间的KL，而是把同一个 状态 $s_t$ 输入到这两个策略的环境中，他们分别会给出动作的概率分布，这里计算的是这两个动作的概率分布的KL

系数 $\beta$ 的动态调整过程：

- 如果 $KL > KL_{max}$ ，增大系数
- 如果 $KL<KL_{min}$ ， 减小系数

 

**PPO算法** 就是解决下面的约束的优化问题：
$$
\underset{\theta}{\text{maxmize}} \ 
\mathbb{E}_t
\left[
	\frac{\pi_{\theta}(a_t\vert s_t)}{\pi_{\theta_{old}}(a_t\vert s_t)}
	A_t - \beta KL[\pi_{\theta_{old}}(\cdot\vert s_t),\pi_{\theta}(\cdot\vert s_t)]
\right]
$$


### PPO2

改进的目标函数（Loss)：
$$
L^{CLIP}(\theta)=
\mathbb{E}[\text{min}(r_t(\theta)A_t,
\text{clip}(r_t(\theta),1-\epsilon, 1+\epsilon)A_t)]
$$
其中 $r_t(\theta) = \frac{\pi_{\theta}(a_t\vert s_t)}{\pi_{\theta_{old}}(a_t\vert s_t)}$ 

clip:
$$
r_t(\theta) < 1-\epsilon \Rightarrow 1-\epsilon \\
r_t(\theta) > 1+\epsilon \Rightarrow 1+\epsilon \\
1-\epsilon <  r_t(\theta) < 1+\epsilon \Rightarrow r_t(\theta)\\
$$
<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220516103238598.png" alt="image-20220516103238598" style="zoom:80%;" />

如果使用在策略和价值函数之间共享参数的神经网络结构，我们必须使用结合策略替代物和值函数误差项的损失函数， 即：
$$
L^{CLIP+VF+S}(\theta) 
= \mathbb{E}_t[
L^{CLIP}(\theta)-c_1L^{VF}(\theta)+c_2S[\pi_{\theta}](s_t)
]
$$
其中$c_1, c_2$ 是系数，  $L_t^{VF}$ 是值函数的平方误差 $(V_{\theta}(s_t)-V_t^{targ})^2$ ，$S$ 表示熵损失，使actor有足够的探索性



$$
L^{CLIP}(\theta)=
\mathbb{E}[\text{min}(r_t(\theta)A_t,
\text{clip}(r_t(\theta),1-\epsilon, 1+\epsilon)A_t)]
$$



$$
\begin{align}
A_{t}^{GAE(\gamma, \lambda)} 
& = (1-\lambda) \left( A_t^{(1)} + \lambda A_t^{(2)} + \lambda^{2} A_t^{(3)} + \cdots \right) \\
& = \sum_{k = 0} ^{T-1}(\gamma \lambda)^{k}\delta_{t+k}
\end{align}
$$

$$
\begin{align}
A_t^{(n)} = \sum_{k = 0}^{n-1}\gamma^{k}\delta_{t+k} 
=  & -V_{\phi}(S_t) + r_t + \gamma_{t+1}+\gamma^{2}r_{t+2}   \\
& +\cdots +\gamma^{n-1}r_{t+n-1}+\gamma^{n}V_{\phi}(s_t + n)
\end{align}
$$

$$
\theta^{'} \leftarrow \theta - \eta \nabla_{\theta}\mathcal{L}_{clip}(\theta)
$$


$$
b_v,b_R\in [-1,1] \\
e_v,e_R\in [0,k]
$$
