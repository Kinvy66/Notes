# VISSIM 的基本使用

## 基本数据

### 分布

vissim的参数值设置成服从某个函数的分布

#### 1.期望速度

基本数据-->分布-->期望速度

![image-20220810102429203](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810102429203.png)



软件默认自带的速度配置

![image-20220810102828382](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810102828382.png)

![image-20220810102456799](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810102456799.png)





#### 2.颜色

颜色分布只用于仿真显示，对结果不会有影响

基本数据-->分布-->颜色

以下是软件默认配置的一些颜色

![image-20220810102928823](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810102928823.png)



![image-20220810103225992](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810103225992.png)

添加两种颜色

![image-20220810103353520](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810103353520.png)



#### 3. 时间

时间分布的使用，比如公交车停车时间，收费口的停车时间，停车场的停车时间

基本数据-->分布-->时间

自带的默认时间分布

![image-20220810103825263](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810103825263.png)



添加时间分布

![image-20220810103856078](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810103856078.png)





### 车辆种类&车辆类型&车辆类别

 ![image-20220810105458723](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810105458723.png)

例子

![image-20220810105724751](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810105724751.png)



#### 添加车辆模型流程

##### 1. 添加2D/3D 模型

基本数据-->2D/3D模型

![image-20220810110046224](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810110046224.png)

添加车辆模型

![image-20220810110200750](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810110200750.png)





##### 2. 添加2D/3D 模型分布

基本数据-->分布-->2D/3D模型

![image-20220810110519172](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810110519172.png)

添加后的数据

![image-20220810110618638](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810110618638.png)



##### 3. 添加车辆类型

基本数据-->车辆类型

![image-20220810111414442](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810111414442.png)

使用复制对象的方式添加

![image-20220810111635163](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810111635163.png)

##### 4. 车辆类别

基本数据--> 车辆类别

![image-20220810162151666](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810162151666.png)

![image-20220810162316367](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810162316367.png)



### 驾驶行为&路段驾驶行为



#### 1. 驾驶行为

基本数据-->驾驶行为

![image-20220810162816032](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810162816032.png)

添加驾驶行为，复制对象的方式添加

![image-20220810163340018](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810163340018.png)



#### 2. 路段驾驶行为类型

基本数据-->路段驾驶行为类型

![image-20220810163521697](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810163521697.png)

指定特定的类别的驾驶行为，其他的使用默认的驾驶行为



### 其他

#### 1.  显示类型

基本数据-->显示类型

配置不同的对象显示不同的颜色

![image-20220810163719081](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810163719081.png)

通过设置DrawOrder3避免出现叠影



#### 2. 层

基本数据-->层

侧边栏的层是查看当前所有的层，下面的是编辑各个层的参数

![image-20220810164747520](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810164747520.png)

添加一个高架层

![image-20220810165431007](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810165431007.png)



## 仿真参数

仿真-->参数

![image-20220810170606890](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220810170606890.png)





## 绘制路段

在路段编辑器中，按住 `ctrl` + 鼠标右键绘制一条路段



## 设置车辆输入

左侧导航栏车辆输入， 按住 `ctrl` + 鼠标右键对应的车辆输入的路段

![image-20220811102633623](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811102633623.png)





## 车辆路径设置

设置车辆的转向

![image-20220811102747819](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811102747819.png)



## 冲突区域









## 信号控制

![image-20220811171540926](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811171540926.png)

相关概念

**型号控制机**： 信号控制柜

**信号灯组**：同一个时间某几个信号灯的颜色是一样的

**信号灯头**：信号灯

建立的顺序，从大到小



### 信号控制机

信号控制-->信号控制机

![image-20220811174639554](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811174639554.png)







## 减速区域&期望速度决策点

### 减速区域

![image-20220811174823971](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811174823971.png)

在减速区域会以指定的速度行驶，使用场景左转或右转。在车开到减速区域之前就会提前减速，速度不是突变的



### 期望速度决策点

![image-20220811174925151](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220811174925151.png)

经过期望速度决策点后以期望的速度行驶，应用场景，进入小区，进入高速公路





## 停车标志&停车场

停车标志

![image-20220812102204103](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812102204103.png)



停车场

![image-20220812102701017](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812102701017.png)

设置停车车路径，需要在车辆的路径（静态）的内部

![image-20220812102754974](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812102754974.png)

停车场设置权重使车辆按顺序停放

![image-20220812103211366](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812103211366.png)

占道时间分布，模拟新手停车对车道的占用情况

![image-20220812103326859](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812103326859.png)

快速添加停车场

![image-20220812105028426](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220812105028426.png)





## 用户自定义属性&属性决策点

选择需要创建自定义属性的对象，比如车辆

![image-20220815111637296](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220815111637296.png)

![image-20220815111737263](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220815111737263.png)
