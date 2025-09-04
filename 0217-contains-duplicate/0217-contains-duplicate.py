class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        use a set to store an element.
        if the element already exists in the set, return False.
        else, return True.
        '''
        # 1. create a set to store each elements
        hash_set = set()

        # 2. insert each element to the set
        for num in nums:
            # 3. if the number already in set, don't insert it (it's a duplicate)
            if num in hash_set:
                return True
            hash_set.add(num)
        
        # 4. if all number managed to be inserted, there are no duplicates
        return False