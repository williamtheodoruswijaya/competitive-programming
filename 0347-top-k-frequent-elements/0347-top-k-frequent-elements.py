class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        use a heap to store number where the number are the pair value.
        to create the pair value, create a hash_map and count the number of the occurances
        ex. [1,1,1,2,2,3] => {1: 3, 2: 2, 3: 1}
        insert the values of the hash map into a min heap
        if the heap.size() > k, then pop the heap since the popped elements are not larger than the new inserted element
        it's the same as saying, if the heap.size() > k, extract/remove the smallest element
        '''
        # 1. create a hash_map and count for each number occurances
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        # 2. use a min heap and store the value from hash_map one by one
        min_heap = []
        for key, val in hash_map.items():
            tpl = (val, key)
            heapq.heappush(min_heap, tpl)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # 3. take the second value in the heap since we store it like this (value: key)
        return [val[1] for val in min_heap]