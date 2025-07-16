class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hash_map;
        for(int num : nums){
            if(hash_map[num] != 0){
                return true;
            } else {
                hash_map[num]++;
            }
        }
        return false;
    }
};