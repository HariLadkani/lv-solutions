class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map= {}

        for index in range(len(nums)):
            num = nums[index]
            if num in hash_map:
                return [hash_map[num],index]
            hash_map[target-num] = index

        
        