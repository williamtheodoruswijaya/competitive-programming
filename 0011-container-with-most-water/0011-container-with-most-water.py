class Solution:
    def calculateArea(self, height: int, width: int) -> int:
        return height * width

    def maxArea(self, height: List[int]) -> int:
        '''
        have two pointers iterate each other (left on first index, right on last index).
        calculate the area of the water for each iteration.
        if height on left < height on right, move left once (right stills in the position).
        if height on left > height on  right, move right once (left stills in the position).
        '''
        ans = -9999
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, self.calculateArea(h, w))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans