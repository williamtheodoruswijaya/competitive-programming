class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hash_map;
        for(int num : nums) {
            hash_map[num]++;
        }

        priority_queue<pair<int,int>> heap;
        for(auto val : hash_map) {
            heap.push({val.second, val.first});
        }

        vector<int> res;
        while(!heap.empty()) {
            if(res.size() == k) {
                break;
            }
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;
    }
};