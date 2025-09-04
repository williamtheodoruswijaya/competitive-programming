class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        use dictionary to count for each letter
        if the hash_map are the same, it is an anagram
        else, it's not

        use one hash_map to count for each letter in s
        decrement each value in hash_map for each letter in t
        if there are negative value, or the key doesn't exists, it's not an anagram
        '''
        # 0. s-cases: early return if the length of s and t are different
        if len(s) != len(t):
            return False

        # 1. create a hash_map
        hash_map = {}

        # 2. count for each letter occurances in s
        for letter in s:
            if letter not in hash_map:
                hash_map[letter] = 1
            else:
                hash_map[letter] += 1
        
        # 3. decrement each letter in hash_map for each letter in t
        for letter in t:
            if letter not in hash_map:
                return False
            else:
                hash_map[letter] -= 1
            if hash_map[letter] < 0:
                return False
        
        # 4. if succeed, return True
        return True