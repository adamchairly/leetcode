## Problem Link

[LeetCode Link](https://leetcode.com/problems/add-two-numbers/)

### Problem Description

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

## Example:

Input: l1 = [2,4,3], l2 = [5,6,4]

Output: [7,0,8].

### Solution

Using a while loop I go through all the values. The root is essentially a pointer to the starting of the list, it has a placeholder '0' value.
The carry makes sure that if the addition in a given position goes above 10, the remainig will be added in the next addition.

```py
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = root = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            result.next = ListNode(carry%10)
            carry = carry//10
            result = result.next
        return root.next
```
