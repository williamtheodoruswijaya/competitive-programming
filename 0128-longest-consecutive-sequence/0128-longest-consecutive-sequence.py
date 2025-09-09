class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        To solve this, we need to understand first the indications of a longest consecutive elements.
        Which's the first number will not have 'n-1' on nums, therefore, if a number doesn't have the 'n-1' on nums, we can conclude it's the first number.
        After we have the first number, we will check 'n+1' number, if it exists on nums, then we update the length and so on.
        If it's not, reset the length calculation but keep stores the main length.
        '''
        # 1. changes nums into set() for O(1) search
        sets = set(nums)

        ans = 0
        for num in sets:
            # 2. check for the beginning number (n-1) not in sets then we can assume it's the first number in the longest consecutive
            if num - 1 not in sets:
                # 3. if it's the beginning, check for (n+1) in sets repeatedly
                length = 0
                while num + length in sets:
                    length += 1
                    # 4. keep updates the main calculation
                    ans = max(ans, length)
        # 5. return the answer
        return ans