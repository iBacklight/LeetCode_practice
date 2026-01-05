"""
155 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
 

示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

medium

注意：在 Python 里：

    list.append() 和 list.pop() 操作时间复杂度都是 O(1)；

    list[-1] 访问栈顶元素也是 O(1)；

    所以用 list 完全满足“常数时间 push/pop/top/getMin”的要求。

"""

class MinStack:
    """dict + linked list"""

    def __init__(self):
        self.stack = {}
        self.len = 0
        self.min = None
        self.min_list = {}
        self.stack[self.len] = None
        

    def push(self, val: int) -> None:
        # last = {"val": val, "next": None}
        self.len += 1
        self.stack[self.len-1] = val
        if self.min == None :
            self.min_list[val] = {"val":val, "nums":1, "last": None}
            self.min = val
        elif self.min > val:
            self.min_list[val] = {"val":val, "nums":1, "last": self.min_list[self.min]}
            self.min = val
        elif val in self.min_list:
            self.min_list[val]["nums"] += 1
            
        return None

    def pop(self) -> None:
        if self.len > 0:
            # check if the min val
            last_val = self.stack[self.len-1]
            if self.min == last_val:
                if self.min_list[last_val]["nums"] > 1:
                    self.min_list[self.min]["nums"] -= 1# still has the same number in the stack
                elif len(self.min_list) > 0:
                    # print(self.min_list[last_val])
                    if self.min_list[last_val]["last"] != None:
                        self.min = self.min_list[last_val]["last"]["val"]
                    else:
                        self.min = None
                    del self.min_list[last_val]
            del self.stack[self.len-1]
            self.len -= 1 
        return None

    def top(self) -> int:
        return self.stack[self.len-1]

    def getMin(self) -> int:
        return self.min
    
class MinStack:
    """list"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()