class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. store the frequency inside a hash map
        unordered_map<int, int> hash_map;
        for(int num : nums) {
            hash_map[num]++;
        }

        // 2. create a min heap to auto sort the value
        priority_queue<pair<int,int>> heap;
        for(auto val : hash_map) {
            heap.push({val.second, val.first});
        }

        // 3. pop the heap and take only the K-th element.
        vector<int> res;
        while(!heap.empty()) {
            if(res.size() == k) {
                break;
            }
            res.push_back(heap.top().second);
            heap.pop();
        }

        // 4. return the vector
        return res;
    }
};