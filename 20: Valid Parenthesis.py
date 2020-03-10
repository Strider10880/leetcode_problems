'''

20: Valid Parenthesis

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

'''
class Solution:
    def isValid(self, s: str) -> bool:
        ref={
            ')':'(',
            '}':'{',
            ']':'['
        }
        x=['(','[','{']
        c=[]
        for i in range(len(s)):
            if not c:
                c.append(s[i])
            elif s[i] in x:
                c.append(s[i])
            elif c[-1]==ref[s[i]]:
                c.pop()
            else:
                c.append(s[i])
        return not c
            