class Solution {
public:
    bool isAnagram(string s, string t) {
        // s-cases:
        if(s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, int> hash_map;
        for(int i = 0; i < s.size(); i++) {
            hash_map[s[i]]++;
        }

        for(int i = 0; i < t.size(); i++) {
            hash_map[t[i]]--;
            if(hash_map[t[i]] < 0) {
                return false;
            }
        }

        return true;
    }
};