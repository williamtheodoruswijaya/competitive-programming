class Solution {
public:
    // hash function to sort the string (ex. "tea" -> "aet")
    string hash(string s) {
        sort(s.begin(), s.end());
        return s; 
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 1. create a hash table instead of hash map to store vectors of string
        unordered_map<string, vector<string>> hash_table;

        // 2. create a 2D vector to store the results
        vector<vector<string>> res;

        // 3. insert the value into the hash table
        for(string str : strs) {
            string key = hash(str);
            hash_table[key].push_back(str);
        }

        // 4. take the 2D vector that were stored
        for(auto& val : hash_table) {
            res.push_back(val.second);
        }

        // 5. return the 2D vector
        return res;
    }
};