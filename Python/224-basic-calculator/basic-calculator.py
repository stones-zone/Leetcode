# -*- coding:utf-8 -*-


# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#
#
#
#
# Note: Do not use the eval built-in library function.
#


class Solution(object):
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators, operands = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == "+" or s[i] == "-":
                operators.append(s[i])
            elif s[i] == "(":
                while operators[-1] != ")":
                    self.compute(operands, operators)
                operators.pop()
                
        while operators:
            self.compute(operands, operators)
        return operands[-1]
    
    def compute(self, operands, operators):
        digiA, digiB = operands.pop(), operands.pop()
        oper = operators.pop()
        if oper == "+":
            operands.append(digiA + digiB)
        if oper == "-":
            operands.append(digiA - digiB)
                
    def calculate(self, s):
        s = s.replace(" ","")
        stack = []
        res, sign, num = 0, 1, 0
        
        for n in s:
            if n.isdigit():
                num = num*10 + int(n)
            elif n in "+-":
                res += sign * num
                num = 0
                sign = 1 if n == "+" else -1
            elif n == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif n == ")":
                res += sign * num
                res = (res * stack.pop()) + stack.pop()
                num = 0
        
        return res + num * sign
