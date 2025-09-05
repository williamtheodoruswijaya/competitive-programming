class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        '''
        # 1. if last pointer wasn't a digit/character, move it until it meets a character
        last = len(s) - 1
        while last > 0 and not s[last].isalnum():
            last -= 1
        
        # 2. if it already a character, move it until it meet a space
        res = 0
        while last >= 0 and s[last].isalnum():
            last -= 1
            res += 1
        
        # 3. return the results
        return res