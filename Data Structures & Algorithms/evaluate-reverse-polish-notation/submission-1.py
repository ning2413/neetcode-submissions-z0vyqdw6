class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+', '-', '*', '/'}
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        stk = []
        for i in tokens:
            if i not in op:
                stk.append(i)
            else:
                b = int(stk.pop())
                a = int(stk.pop())
                total = operations[i](a, b)
                stk.append(total)
        return int(stk[-1])