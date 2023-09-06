## Problem Link

[LeetCode Link](https://leetcode.com/problems/split-linked-list-in-parts/)

### Problem Description

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.

Example

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

### Solution

First, I need to get the length of the list, so I will know the size of each split, as well as the 'extra' leftover from the list.
Then I can create k piece of subarray, and divide the 'extra' nodes equally among each part.

#### Implementation
```py
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        part_size = length // k
        extra = length % k

        node_array = []
        temp = head

        for i in range(k):
            sub_head = temp 
            prev = None 
            for j in range(part_size + (1 if extra > 0 else 0)):
                prev = temp
                temp = temp.next if temp else None
            if prev:
                prev.next = None
            node_array.append(sub_head)
            
            if extra > 0:
                extra -= 1
                
        return node_array
```

### Time Complexity
- _Time Complexity: O(n)_
- _Space Complexity: O(k) - k being the number of parts_