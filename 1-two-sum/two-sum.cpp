class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash_map;
        for(int i = 0; i < nums.size(); i++){
            int key = target - nums[i];
            if(hash_map.count(key)){
                return {hash_map[key], i};
            } else {
                hash_map[nums[i]] = i;
            }
        }
        return {};
    }
};