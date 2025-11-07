# The runtime complexity of this solution is O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'(' : ')', '[' : ']', '{' : '}' }
        if (len(s) % 2) != 0:
            return False
        for char in s:
            if char in dictionary:
                stack.append(char)
            elif not stack or dictionary[stack.pop()] != char:
                return False
        if stack:
            return False
        else: 
            return True


'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''