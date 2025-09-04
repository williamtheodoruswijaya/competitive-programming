class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        create a left and right pointer
        if the character in left nor right are not digits nor number, keep moving the pointer until it meets a digit/number.
        if both pointer, points to a digits/number, lowercase the character and check
        if it already difference, make an early return and return False
        after that, move both pointer.
        after all of letter are checked, return True
        '''
        # 1. create left and right pointer
        left = 0
        right = len(s) - 1

        # 2. check for each letter in s
        while left <= right:
            # 3. as long as left/right didn't meet a digits/number, keep moving it
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # 4. if both left and right are a character, check if it's the same or not
            if s[left].lower() != s[right].lower():
                # 5. if not, make an early return
                return False
            # 6. if yes, then move both pointer until all letters are checked
            left += 1
            right -= 1
        # 7. if the check are completed, return True
        return True