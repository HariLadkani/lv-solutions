class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        /*
        [1,5,4,2,9,9,9]
         l 
             r
        2 - 0 =  3 > 3
        res = 15  
        sum = 0
        set={9}
        
        while r - left + 1 > k:
            move left
            reduce sum 
            remove from set too

        while current_num in set:
            remove left element from set
            reduce sum by left element
            move left
        add to set current num
        if right - left = k:
            res = max(sum, res)
        */

        int left = 0;
        unordered_set<int> membership;
        long long current_sum = 0;
        long long res = 0;

        for (int r=0; r<nums.size(); r++) {
            if (r-left+1 > k) {
                current_sum = current_sum - nums[left];
                membership.erase(nums[left]);
                left += 1;
            }

            while (membership.count(nums[r])) {
                membership.erase(nums[left]);
                current_sum = current_sum - nums[left];
                left += 1;
            }

            membership.insert(nums[r]);
            current_sum += nums[r];

            if (r - left + 1 == k) {
                res = max(current_sum, res);
            }
            
        }
        return res;
    }
};