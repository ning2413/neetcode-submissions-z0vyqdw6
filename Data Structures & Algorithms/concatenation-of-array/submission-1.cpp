class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int size = nums.size() * 2;
        vector<int> ans(size);
        for (int i = 0; i < nums.size(); i++) {
            ans[i] = nums[i];
            ans[i + nums.size()] = nums[i];
        }
        return ans;
    }
};