class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        create a set from 1 to n where n = len(nums).
        check each num in nums if the num exists in sets then remove the num from the sets.
        '''
        # 1. create a set from 1 to n
        sets = set()
        n = len(nums) + 1
        for i in range(1, n):
            sets.add(i)
            
        # 2. check does num in nums exists in set
        for num in nums:
            if num in sets:
                sets.remove(num)
        
        return list(sets)