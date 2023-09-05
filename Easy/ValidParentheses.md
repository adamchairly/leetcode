## Problem Link

[Problem Link](https://leetcode.com/problems/valid-parentheses/)

### Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true


Example 2:
Input: s = "()[]{}"
Output: true

### Approach

The approach is to use a dictionary, which pairs the opening and closing bracket types. 
Then, every opening bracket is being put in a stack.
When encountering a closing bracket of any type, we check if the stack has the corresponding opening bracket on the top.
This forces the algorithm to return false, if the paranthesis are in an incorrect order, or there are not enough opening/closing.

#### Solution

```py
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                return False

        return not stack


```

### Complexity
- _Time Complexity_: O(n)
- _Space Complexity_: Depends on the input
