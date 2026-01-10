class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> counter;

        for (int i=0;i<nums.size(); i++) {
            int num = nums[i];

            if (counter.count(target - num)) {
                int first_index = counter[target-num];
                int second_index = i;
                return {first_index, second_index};
            }

            counter[num] = i;

        }
        return {};
    }
};