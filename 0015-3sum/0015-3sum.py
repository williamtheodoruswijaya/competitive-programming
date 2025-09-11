class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        basically two sum II is the sub-problem if nums is sorted.
        so, we can just have i iterate through nums.
        and per-iteration, we add left and right.
        and then move left if i + left + right < 0, viceversa.
        if i + left + right == target (which's 0) add it into a set.
        why set? because there can be a duplicates if we are using list.
        '''
        # 1. sort nums (to change the sub-problem into a two-sum-ii problem)
        nums.sort()
        
        # 2. initialize an empty set
        res = set()

        # 3. iterate through each number
        for i in range(len(nums)):
            # 4. initialize left and right pointer
            left = i + 1
            right = len(nums) - 1

            # 5. find left and right (two-sum-ii sub-problems)
            while left < right:
                if left < right and nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif left < right and nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    # 6. if the combination are founded, don't return because we can have more then 1 combinations.
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1

        # 7. return sets that are converted into a list to match the return-type
        return list(res)