class Solution:
    def hash(self, s: str) -> str:
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        create a hash_table {key : [val, val, ...]}
        hash key using a hash function (sort each alphabet and make it as a key)
        get each values and return it
        '''
        # 1. create a hash_table
        hash_table = {}

        # 2. iterate through each strings
        for s in strs:
            # 3. hash strings and insert it as a key
            key = self.hash(s)
            # 4. store each string according to the key
            if key not in hash_table:
                hash_table[key] = [s]
            else:
                hash_table[key].append(s)

        # 5. get each value in hash_table
        return list(hash_table.values())