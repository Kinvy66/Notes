# C++ STL



## 1. STL体系结构基础介绍



### 1.1 STL六大部件

- 容器（containers）
- 分配器（allocator）
- 算法（algorithms)
- 适配器（adapters)
- 仿函数（functors)



这些部件的关系图:

![image-20210827101710110](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210827101710110.png)



示例：

```c++
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

int main()
{
    int ia[6] = {27,210,12,47,109,83};
    vector<int, allocator<int>> vi(ia,ia+6);
    
    cout << count_if(vi.begin(), vi.end(),
                    notl)
}
```

