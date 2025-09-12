class Solution {
public:
    bool isVowel(char ch) {
        switch(ch) {
            case 'a':
                return true;
            case 'i':
                return true;
            case 'u':
                return true;
            case 'e':
                return true;
            case 'o':
                return true;
            default:
                return false;
        }
    }

    bool doesAliceWin(string s) {
        int numOfVowel = 0;
        for (int i = 0; i < s.size(); i++) {
            if (isVowel(s[i])) {
                numOfVowel++;
            }
        }

        if (numOfVowel == 0) {
            return false;
        } else {
            return true;
        }
    }
};