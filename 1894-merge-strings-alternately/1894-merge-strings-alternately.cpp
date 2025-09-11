class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int length = word1.size() <= word2.size() ? word1.size() : word2.size();

        string res = "";
        int last = 0;
        for (int i = 0; i < length; i++) {
            res += word1[i];
            res += word2[i];
            last = i;
        }

        if (word1.size() > word2.size()) {
            for (int i = last + 1; i < word1.size(); i++) {
                res += word1[i];
            }
        } else {
            for (int i = last + 1; i < word2.size(); i++) {
                res += word2[i];
            }
        }
        return res;
    }
};