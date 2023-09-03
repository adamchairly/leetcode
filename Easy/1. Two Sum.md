## Problem Link

[LeetCode Link](https://leetcode.com/problems/two-sum/)

### Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

nums = [2,7,11,15], target = 9 -> nums[0] + nums[1] == 9, we return [0, 1].

### Solution

Using Brute Force and going through the array for each element works. The time complexity for that is O(n^2).
An optimized approach would be to use a dictionary where we can store key-value pairs. The idea is to use the difference
of the current value and the target. If that difference is in the dictionary, then we can return the indices.
Since the lookup time in dictionaries are constant, the complexity of this will be O(n).
#### Brute Force Solution
```py
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

#### Optimized Solution

```py
class Solution(object):
    def twoSum(self, nums, target):
        dc = {}
        length = len(nums)
        for i in range(length):
            if target - nums[i] in dc: 
                return [i, dc[target - nums[i]]]
            dc[nums[i]] = i
        return []
```
### Time Complexity
- _Brute force Complexity_: O(n^2)
- _Optimized Complexity_: O(n)
