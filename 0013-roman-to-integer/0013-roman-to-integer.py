class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        use dictionary to map each character value.
        iterate through each character and do something.
        notice if the next character have a larger value then the current character, the current character will be a minus.
        for example: "IV" is -1 + 5 = 4.
        else, if the next character have a smaller value then the current character, add the current character.
        for example: "VI" is 5 + 1 = 6.
        '''
        # 1. use a dictionary to map each roman character
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # 2. initialize sum for storing calculation data
        sum = 0

        # 3. iterate through each character
        for i in range(len(s)):
            # 4. check if the next character are larger then the current value or not
            if i != len(s) -1 and map[s[i]] < map[s[i+1]]:
                sum -= map[s[i]]
            else:
                sum += map[s[i]]

        # 5. return the calculation
        return sum