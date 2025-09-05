class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        there are 3 cases that can happen here:
        - u are on the first indexes (index=0)
            - check for the next index (index=1)
        - u are on the last indexes (index=flowerbed.size() - 1)
            - check for the prev index (index=flowerbed.size() - 2)
        - u are on the middle
            - check for both side
        '''
        # s-cases: size of flowerbed only -> [0] and n = 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n > 0:
            n -= 1
            return n == 0
        # s-cases: size of flowerbed only -> [0] and n = 0
        if len(flowerbed) == 1 and n == 0:
            return n == 0
        
        for i in range(len(flowerbed)):
            # early return if there are no more flower to plant
            if n == 0:
                break
            # 1. first cases (can place on index 0)
            if i == 0 and (flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            # 2. second cases (can place on index -1)
            if i == len(flowerbed)-1 and (flowerbed[i] == 0 and flowerbed[i-1] == 0):
                flowerbed[i] = 1
                n -= 1
            # 3. third cases
            if (i != 0 and i != len(flowerbed)-1) and flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n == 0