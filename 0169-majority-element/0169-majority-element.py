class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        if we sort the number in nums, and pick the median, it will return the majority element
        since median represent the most element that appears in a data (data science moment)
        '''
        # 1. sort the nums O(n log n)
        nums.sort()
        
        # 2. takes the median
        return nums[len(nums)//2]