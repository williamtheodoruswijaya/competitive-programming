class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        use two-pointers, but put left and right on the same index (start with index 0).
        left will keep tracks of non-zero elements.
        right will keep tracks of iterating.
        ex.) [0,1,0,3,12]
        since left and right are on the index 0, we check if it is 0 or not, but since both are the same index, we can ignore it.
        now, nums[left] = 0, nums[right] = 1. since, right != 0, we swap it's position:
        [1,0,0,3,12]
        so everytime, right meet a non-zero element, we swap it
        [1,3,0,0,12] => [1,3,12,0,0]
        '''

        left = 0
        for right in range(len(nums)):
            # 1. if right is a non-zero element.
            if nums[right] != 0:
                # 2. swap it with left
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                
                # 3. move left once
                left += 1