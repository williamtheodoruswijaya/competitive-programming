class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> sets;

        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++) {
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                if (nums[i] + nums[left] + nums[right] < 0) {
                    left++;
                } else if (nums[i] + nums[left] + nums[right] > 0) {
                    right--;
                } else {
                    sets.insert({nums[i],nums[left],nums[right]});
                    left++;
                    right--;
                }
            }
        }

        vector<vector<int>> res(sets.begin(), sets.end());
        return res;
    }
};