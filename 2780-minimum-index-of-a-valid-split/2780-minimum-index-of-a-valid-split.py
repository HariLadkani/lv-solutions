class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        [2,1,3,1,1,1,7,1,2,1]
                     i
        1:6
        2:2
        3:1
        7: 1


        goal:
            min index split to have same dominant value in both splits

        [1,1,6,6,6,6,6,6,2]
             i
        freq_map_entire_array Counter({6: 6, 1: 2, 2: 1})
        index 0
        freq_map_left_array 1
        max_freq 0
        max_freq 1
        max_value 1
        freq_for_dominant_element_other_half 1
        len(nums) 9
        i 0
       
        ############
        index 1
        freq_map_left_array 2
        max_freq 1
        max_freq 2
        max_value 1
        freq_for_dominant_element_other_half 0
        len(nums) 9
        i 1

        ############
        index 2
        freq_map_left_array 1
        max_freq 2
        max_freq 2
        max_value 1
        freq_for_dominant_element_other_half 4
        len(nums) 9
        i 2
   
        '''

        freq_map_entire_array = Counter(nums)
      
        freq_map_left_array = {}
        max_freq = 0
        max_value = None
        for i in range(len(nums)):
            freq_map_left_array[nums[i]] = freq_map_left_array.get(nums[i], 0) + 1
   

            if freq_map_left_array[nums[i]] > max_freq:
                max_freq = freq_map_left_array[nums[i]]
                max_value = nums[i]

            if max_freq > (i+1) // 2:
                freq_for_dominant_element_other_half = freq_map_entire_array[max_value] - max_freq
       
                if freq_for_dominant_element_other_half > ((len(nums)-(i+1)) // 2):
                    return i

            print("############")

        return -1
