class Solution {
public:
    int calculateArea(int height, int width) {
        return height * width;
    }

public:
    int maxArea(vector<int>& height) {
        int ans = -9999;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            int h = min(height[left], height[right]);
            int w =  right - left;
            ans = max(ans, calculateArea(h, w));
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return ans;
    }
};