class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 1. create a hash map to keep track of the num [key -> value]
        unordered_map<int, int> hash_map;

        for(int i = 0; i < nums.size(); i++){
            // 2. store the number partner
            int partner = target - nums[i];

            // 3. check if the partner exists in the hashmap
            if(hash_map.count(partner)) {
                return {hash_map[partner], i};
            } else {
                // 4. if not, store the other partner as the key and index as the value
                hash_map[nums[i]] = i;
            }
        }

        // 5. return an empty array if there are no correlated partner
        return {};
    }
};