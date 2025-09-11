class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            int key = target - nums[i];
            if (map.find(key) == map.end()) {
                map[nums[i]] = i; 
            } else {
                res.push_back(map[key]);
                res.push_back(i);
                break;
            }
        }
        return res;
    }
};