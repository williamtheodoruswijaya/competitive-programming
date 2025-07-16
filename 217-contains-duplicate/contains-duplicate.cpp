class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hash_map;
        for(int num : nums){
            if(!hash_map.count(num)){
                hash_map[num]++;
            } else {
                return true;
            }
        }
        return false;
    }
};