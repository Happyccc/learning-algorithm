## LeetCode 148 排序链表

2018-12-12 leetcode地址 https://leetcode-cn.com/problems/sort-list/submissions/

### 算法分析

方法1. 快速排序，整体时间复杂度为O(nlogn),空间复杂度为O(1). 在每次partition过程中，将链表分成left,reference,right三段（left和right可能为空），与参照值reference相同时，全部放入reference这个链表，后续递归该链表。递归过程讨论left和right为空的情况，并连接三条链表.

方法2. 插入排序，整体时间复杂度为常数级别O(n^2),空间复杂度为O(1). 

方法3. 归并排序，整体时间复杂度为常数级别O(nlogn),空间复杂度为O(1). 


|方法|时间复杂度|空间复杂度|
| - | :-: | -: | 
|快速排序|nlogn|1|
|插入排序|n^2|1|
|归并排序|nlogn|1|
|冒泡排序|n^2|1|
|选择排序|n^2|1|

### 链表
- 链表：非连续、非顺序的存储结构，通过指针相连，因此在增加、删除操作上效率很高。
- [python中的链表操作](https://blog.csdn.net/su_bao/article/details/81065746)
- [看图理解链表反转](https://blog.csdn.net/feliciafay/article/details/6841115)


（假设现在输入的是10000个node.val = 1的linked list. 那每次循环，都是只剔除掉一个元素，那要10000次quicksort递归... Orz.）

因此在每次Paritition过程中，将链表分成3段, Left, Reference, Right。(其中Left 与 Right 可能为空。) 

与参照值reference值相同的，全部放入reference这条链表中, 而这条链表在后续过程中是不需要继续递归的。

在Quick Sort的递归过程中，分别讨论Left, Right为空时的情况，来将三条链表链接到一起。
