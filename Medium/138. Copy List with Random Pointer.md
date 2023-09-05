## Problem Link

[LeetCode Link](https://leetcode.com/problems/copy-list-with-random-pointer/)

### Problem Description

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

### Solution

To make a deep copy of a list, we will need to copy each object (in case Nodes), then set their attributes accordingly.
I can map all the Nodes of the deep copy, to the Nodes of the original list, and can easily set the attributes afterwards.

#### Implementation
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        node_map = {}
        
        #Create nodes
        current = head
        while current:
            node_map[current] = Node(current.val, None, None)
            current = current.next
        
        #Set the 'next' and 'random'
        current = head
        while current:
            if current.next:
                node_map[current].next = node_map[current.next]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next
        
        #Return the head of the deep copied list
        return node_map[head]
```

