class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> sets;

        for (int i = 1; i <= nums.size(); i++) {
            sets.insert(i);
        }

        for (int num : nums) {
            if (sets.find(num) != sets.end()) {
                sets.erase(num);
            }
        }

        vector<int> res(sets.begin(), sets.end());
        return res;
    }
};