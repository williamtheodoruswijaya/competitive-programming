class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        main idea: 2 + x = 9
        does x exists in hash_map? if not, store {2: index of 2} in hash_map.
        so, if nums = [2,7,11,15], the first iteration will store {2:0} on hash_map.
        when, 7 are iterated, it will check for x, which's 2. Does 2 exists? yes, therefore, return [0,1]
        '''
        # 1. create a hash_map {key: value}
        hash_map = {}

        # 2. loops through the list        
        for i, num in enumerate(nums):
            # 3. get x
            x = target - num
            # 4. if x exists in hash_map, return the value of the hash_map + current index, else, store it {num : index}
            if x in hash_map:
                return [hash_map[x], i]
            else:
                hash_map[num] = i 