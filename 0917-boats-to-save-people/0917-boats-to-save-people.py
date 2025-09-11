class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        sort the people from the minimum weight to the maximum weight.
        there are two cases that can happen:
            case #1: two people can fit into the boat:
                put those two.
            case #2: only one people can fit into the boat:
                pick the largest people to fit into the boat.
        '''
        # 1. sort the people
        people.sort()

        # 2. create two pointers, to check for the cases
        left = 0
        right = len(people) - 1

        # 3. iterate the peoples
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                right -= 1
                boats += 1
        
        return boats