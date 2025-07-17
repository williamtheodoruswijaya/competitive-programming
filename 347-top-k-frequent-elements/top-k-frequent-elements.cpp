class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. store the frequency inside a hash map
        unordered_map<int, int> hash_map;
        for(int num : nums) {
            hash_map[num]++;
        }

        // 2. create a min heap to auto sort the value
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> heap;
        for(auto val : hash_map) {
            heap.push({val.second, val.first});

            // 3. min heap makesure that the top element are not included on the K-th frequent element
            if(heap.size() > k) {
                heap.pop();
            }
        }

        // 4. take out the value {frequencies : value}
        vector<int> res;
        while(!heap.empty()) {
            res.push_back(heap.top().second);
            heap.pop();
        }

        // 5. return the vector
        return res;
    }
};