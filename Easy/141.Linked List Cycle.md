## Problem Link

[Problem Link](https://leetcode.com/problems/linked-list-cycle/)

### Problem Description

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:

Input: head = [3,2,0,-4], pos = 1
Output: true

### Approach

The approach is to have two 'pointers' running in the list. The first one, the faster always steps two nodes, the slower always steps one.
The idea is, that if there is a circle anywhere in the list, the faster will meet the slower.

Since the starting point for both is always the head, if there is only a single node (without loop edge), the program will return false instantly.

#### Solution
```py
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
```

### Time Complexity
- _Complexity_: O(n)
