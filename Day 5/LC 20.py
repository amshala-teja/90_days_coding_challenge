# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []
        for char in s:
            if char in hash_map.values():
                stack.append(char)
            elif char in hash_map:
                if not stack or stack[-1] != hash_map[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
