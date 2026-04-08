class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opens = ['(', '{', '[']
        close = {')': '(',
                 ']': '[',
                 '}': '{'}
        for i in s:
            if i in opens:
                stk.append(i)
            else:
                if len(stk) == 0 or close[i] != stk.pop():
                    return False
        return len(stk) == 0
