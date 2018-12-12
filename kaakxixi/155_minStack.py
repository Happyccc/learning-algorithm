"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""

"""
直接构建一个数组,最后使用list的内置方法min()返回最小值,但复杂度高达O(n)——
参考(https://www.cnblogs.com/ajianbeyourself/p/4212042.html)
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack) #这里复杂度达到O(n)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
设计两个数组list，分别存放数据和最小数据（最小数的个数相等），每次push和pop都会计算该数据是否是最小数，最小则执行相应操作，
这样只增加较小的空间复杂度（平均O(1),最差O(n))，却将时间复杂度显著减小到O(1).
特别注意 x <= self.minstack[-1] 这里应是小于等于（保证两个数组中最小数个数相同），小于ERROR: stack先后push了2个1（最小），
但minstack只push进去1个1，最后pop1个1后，minstack变为空数组，导致getMin()报错IndexError: list index out of range。
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
    

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        #最小的数据从栈顶进入
        if len(self.minstack) == 0 or x <= self.minstack[-1]:  #注意这里的<=
            self.minstack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        #只有stack数组pop的是最小值，minstack才出栈
        if self.minstack[-1] == tmp:
            self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
