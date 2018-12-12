（假设现在输入的是10000个node.val = 1的linked list. 那每次循环，都是只剔除掉一个元素，那要10000次quicksort递归... Orz.）

因此在每次Paritition过程中，将链表分成3段, Left, Reference, Right。(其中Left 与 Right 可能为空。) 

与参照值reference值相同的，全部放入reference这条链表中, 而这条链表在后续过程中是不需要继续递归的。

在Quick Sort的递归过程中，分别讨论Left, Right为空时的情况，来将三条链表链接到一起。
