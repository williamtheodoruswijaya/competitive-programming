class Solution {
public:
    string hash(string s) {
        sort(s.begin(), s.end());
        return s; 
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash_map;
        vector<vector<string>> res;

        for(string str : strs) {
            string key = hash(str);
            hash_map[key].push_back(str);
        }

        for(auto& val : hash_map) {
            res.push_back(val.second);
        }

        return res;
    }
};