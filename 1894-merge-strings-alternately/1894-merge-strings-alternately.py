class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        take the minimum length between the two word.
        iterate from index 0 until minimum length.
        in the iteration, add char from word1 first follow up by the word2.
        after that, check if word1 length are larger then word2 length and append the rest char.
        vice versa.
        '''
        res = ''

        # 1. take the minimum length between two word
        length = min(len(word1), len(word2))
        
        # 2. iterate from index 0 until minimum length
        for i in range(length):
            # 3. add char from word1 and word2
            res += word1[i]
            res += word2[i]

        # 4. check for the rest char that hasn't been taken
        if len(word1) > len(word2):
            for i in range(len(word2), len(word1)):
                res += word1[i]
        else:
            for i in range(len(word1), len(word2)):
                res += word2[i]
        
        # 5. return the results
        return res