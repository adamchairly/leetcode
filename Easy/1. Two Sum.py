class Solution(object):
    def twoSum(self, nums, target):
        dc = {}
        length = len(nums)
        for i in range(length):
            if target - nums[i] in dc: 
                return [i, dc[target - nums[i]]]
            dc[nums[i]] = i
        return []