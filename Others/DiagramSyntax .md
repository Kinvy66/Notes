# mermaid 语法



## 1.  流程图

流程图是由节点，不同形状的图形，箭头和线等组成的。



* 一个节点和定义文本的节点

  ```mermaid
  graph LR
  	id
  	id1[这是文本]
  ```



* 图形(Graph)

  ```mermaid
  graph TB
  	Start --> Stop
  ```

  ```mermaid
  graph LR
  	Start --> Stop
  
  ```

  

  > LR, TD表示的是流程图的方向，即从左到右，从上到下,更多
  >
  > - TB - top to bottom
  > - TD - top-down/ same as top to bottom
  > - BT - bottom to top
  > - RL - right to left
  > - LR - left to right



* 外框的形状

  圆角：`(文本)`  椭圆：`([])`
  
  ```mermaid
  graph LR
  	id(这是文本)
  	id1([椭圆])
  ```
  
  
  
  
  
  

