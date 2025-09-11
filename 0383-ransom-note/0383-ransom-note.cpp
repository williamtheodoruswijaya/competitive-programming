class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> map;
        for (char ch : magazine) {
            map[ch]++;
        }

        for (char ch : ransomNote) {
            if (map.find(ch) == map.end()) {
                return false;
            } else if (map[ch] == 0) {
                return false;
            } else {
                map[ch]--;
            }
        }
        return true;
    }
};