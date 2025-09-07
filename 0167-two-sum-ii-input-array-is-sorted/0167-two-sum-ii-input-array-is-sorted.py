class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        create a two pointer
        add number on left + number on right
        if equal target: return left+1, and right+1
        elif < target: since it was sorted, just pick a larger number by moving left = left + 1
        elif > target: since it was sorted, just pick a smaller number by moving right = right - 1
        '''
        left = 0
        right = len(numbers) - 1

        while left < right:
            ans = numbers[left] + numbers[right]
            if ans < target:
                left += 1
            elif ans > target:
                right -= 1
            else:
                return [left+1, right+1]