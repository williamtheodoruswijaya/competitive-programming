class Solution {
public:
    bool isVowels(char ch) {
        switch (ch) {
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

    string reverseVowels(string s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            while (left < right && !isVowels(tolower(s[left]))) {
                left++;
            }
            while (left < right && !isVowels(tolower(s[right]))) {
                right--;
            }
            if (isVowels(tolower(s[left])) && isVowels(tolower(s[right]))) {
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
            }
            left++;
            right--;
        }
        return s;
    }
};