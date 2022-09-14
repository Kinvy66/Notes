# 自动驾驶综述笔记



## 1. Deep Reinforcement Learning for Autonomous Driving: A Survey

B. R. Kiran *et al.*, “Deep Reinforcement Learning for Autonomous Driving: A Survey,” *IEEE Transactions on Intelligent Transportation Systems*, pp. 1–18, 2021, doi: [10.1109/TITS.2021.3054625](https://doi.org/10.1109/TITS.2021.3054625).



### 摘要

本综述总结了深度强化学习（DRL）算法，并对自动驾驶任务的分类。除此之外还描述了相似领域的但不是经典RL的算法如克隆学习，模仿学习，逆强化学习。还讨论了仿真器在训练 Agent 中的作用，对验证、测试和鲁棒性RL中现有的解决方案。



### AD 系统的组成

AD 系统主要是由以下这个些部分组成：

- **场景理解（Scene Understanding）**感知，融合多种传感器的数据为更高层的决策和动作提供一种统一的和简化的上下文表示。
- **定位和地图（Localization and Mapping）** ，地图是AD关键，拥有某个地方的地图就能够对车辆进行定位。
- **规划和驾驶策略（Planning and Driving Policy）**，轨迹规划是AD中一个至关重要的模块，基于给定的地图，生成引导智能体运动级别的命令。
- **控制（control）**， 控制器的定义是给出每个点的速度值，转向角和刹车动作



### 强化学习



































