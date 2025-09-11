class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        turn magazine into a dictionary.
        takes each letter from the dictionary.
        '''

        # 1. turn magazine into a dictionary
        map = Counter(magazine)

        # 2. try to take the item from dictionary
        for ch in ransomNote:
            # 3. if item not in magazine, then ransomNote can't be build with that magazine
            if ch not in map:
                return False
            # 4. if item already empty, then ransomNote can't be build with that magazine
            elif map[ch] == 0:
                return False
            # 5. if item exists and not empty, take that item
            else:
                map[ch] -= 1
        
        # 6. if ransomNote can be builded (iteration finish), return True
        return True