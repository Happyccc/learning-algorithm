
## LeetCode 206 反转链表

2018-12-10 leetcode地址 https://leetcode-cn.com/problems/reverse-linked-list/submissions/

### 算法分析

方法1. 倾倒法，整体时间复杂度为O(n),空间复杂度为O(1). 使用1个指针循环遍历链表,并将指针指向的节点不断往空箱子（辅助变量）里面倾倒,并使用一个临时变量存储该指针下一步的链表.

方法2. 逐个反转法，整体时间复杂度为常数级别O(n),空间复杂度为O(1). 使用2个指针p和q（前2个节点）先交换指向:p->q 变为q->p，然后不断循环遍历这两个指针，并使用一个临时变量存储q下一步的链表，通过不断交换p和q的指向可以最终完成整个链表的反转，最终的反转结果就是p。

方法3. 递归方法，整体时间复杂度为常数级别O(n),空间复杂度为O(1). 但是在leetcode上运行时间反而比前两种方法要长很多. 这里注意递归的是子链表，递归后还要加上分裂点（分裂前的头结点）作为尾结点。

方法4. 逐个插入法，从第二个节点一直到最后一个节点，逐个插入到第一个节点前边. 尚待实现。

方法5. 数组法，先将链表读入到数组，再逆序读出数组元素到链表，空间复杂度为O(n)。

|方法|时间复杂度|空间复杂度|
| - | :-: | -: | 
|倾倒法|n|1|
|逐个反转法|n|1|
|递归法|n|1|

### 链表
- 链表：非连续、非顺序的存储结构，通过指针相连，因此在增加、删除操作上效率很高。
- [python中的链表操作](https://blog.csdn.net/su_bao/article/details/81065746)
- [看图理解链表反转](https://blog.csdn.net/feliciafay/article/details/6841115)
