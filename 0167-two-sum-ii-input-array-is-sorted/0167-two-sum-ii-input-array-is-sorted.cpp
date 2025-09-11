class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        vector<int> res;
        while(left < right) {
            if(target > numbers[left] + numbers[right]) {
                left++;
            } else if(target < numbers[left] + numbers[right]) {
                right--;
            } else {
                res.insert(res.end(), {left+1, right+1});
                break;
            }
        }
        return res;
    }
};