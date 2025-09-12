class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        use three pointers:
        left1 on nums1
        right1 on nums1
        right2 on nums2
        and insert it backwardly
        
        [1,2,7,0,0,0]
             ^     ^
        [2,5,6]
             ^

        check number that left1 pointed into, if larger then number that right2 pointed, move the number on left1 into number on right1, and move both right1 and left1.

        [1,2,7,0,0,7]
           ^     ^
        if number that left1 pointed are smaller, assign number that right2 pointed into right1 and move right1 and right2

        [1,2,7,0,6,7]
           ^   ^
        [2,5,6]
           ^

        and so on...

        [1,2,7,5,6,7]
           ^ ^
        [2,5,6]
         ^

        [1,2,2,5,6,7]
           ^ ^
        [2,5,6]
         ^
        exit loop if left1 is 0 or right2 is 0
        '''
        left1 = m - 1
        right1 = m + n - 1
        right2 = n - 1

        while left1 >= 0 and right2 >= 0:
            if nums1[left1] > nums2[right2]:
                nums1[right1] = nums1[left1]
                left1 -= 1
            else:
                nums1[right1] = nums2[right2]
                right2 -= 1
            right1 -= 1
        
        while right2 >= 0:
            nums1[right1] = nums2[right2]
            right1 -= 1
            right2 -= 1
        