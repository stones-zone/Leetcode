# -*- coding:utf-8 -*-


#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# push(x) -- Push element x onto stack.
#
#
# pop() -- Removes the element on top of the stack.
#
#
# top() -- Get the top element.
#
#
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        push 3 5 2 -1
        min  3 3 2 -1
        []   0 2 -1-3  push-p_min
        """
        self.min = 0
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
        

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
            # p_min = push - [] = self.min - x
            self.min = self.min - x
        

    def top(self):
        """
        :rtype: int
        """
        # not self.stack.pop
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
