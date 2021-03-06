### LeetCode 107 二叉树的层次遍历 II
2018-12-11
leetcode地址 https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/submissions/

#### 算法分析

方法1. 层次遍历,整体时间复杂度为O(n),空间复杂度为O(n). 构建了队列queue，但队列每次只存储一层的节点，最差的空间复杂度为n，队列循环：每次循环出父节点，进左右子节点，循环n次，时间复杂度为n.

方法2. 前序/后序/中序遍历,整体时间复杂度为常数级别O(n),空间复杂度为0. 使用递归方法

|步骤|时间复杂度|空间复杂度|
| - | :-: | -: | 
|层次遍历|n|n|
|前/后/中序遍历|n|1|


#### 堆、栈、堆栈、队列、二叉树

- 堆：有两种含义，一种是程序运行时申请的动态内存，另外一种含义是堆作为数据结构，通常被看做一棵树的数组对象，堆总是一颗完全二叉树。
- 栈和堆栈：是一种受限的线性表，可以理解为一个桶，只能在栈顶进行增加和删除，有着'LIFO'即后进先出的特点；两个主要操作是push和pop。
- 队列：也是一种受限的线性表，采用'FIFO'，只能在前端进行删除、后端进行插入。
- 二叉树：是一种特殊的树，最多只有2个节点[二叉树介绍](http://www.cnblogs.com/polly333/p/4740355.html) [二叉树](https://blog.csdn.net/qq_33414271/article/details/78506632)，其特点有：
  - 二叉树的每个结点至多只有二棵子树(不存在度大于2的结点)，二叉树的子树有左右之分，次序不能颠倒；
  - 二叉树的第i层至多有2^{i-1}个结点
  - 深度为k的二叉树至多有2^k-1个结点；
  - 对任何一棵二叉树T，如果其终端结点数为N0，度为2的结点数为N2，则N0=N2+1
- 二叉树的遍历[python实现](https://blog.csdn.net/lq_lq314/article/details/79176953)：
  - 前序遍历：根左右
  - 中序遍历：左根右
  - 后续遍历：左右根
  - 层次遍历：从左到右，从上到下




#### python中的队列

- python中四种队列：queue.Queue / asyncio.Queue / multiprocessing.Queue / collections.deque，主要用的deque实际上是一种两端队列，既能实现堆栈、又能实现队列[deque实战](http://python.jobbole.com/87577/).
- [python四种队列的对比](https://m.jb51.net/article/140534.htm)

