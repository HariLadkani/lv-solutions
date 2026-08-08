class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        [4,5,0,-2,-3,1]
         4 9 9  7  4 5

         j - i % k = 0

         j%k = i%k
         
         res = 1 + 2 + 3 + 1
         4:4
         2:1
         0



        '''
        module_to_count = {0:1}
        res = 0
        running_sum = 0

        for num in nums:
            running_sum += num

            res += module_to_count.get(running_sum % k, 0)
            module_to_count[running_sum % k] = module_to_count.get(running_sum % k, 0) + 1

        return res
     
   