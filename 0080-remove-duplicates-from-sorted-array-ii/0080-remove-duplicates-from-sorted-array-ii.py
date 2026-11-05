class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        each unique element atmost twice

        [1,1,2,2,3,3]
                 l
                   i


        if current i and last three are same elements:
            -  keep left same and increment i

        else:
            swap left and index and increment both left and increment both of them

         [0,0,1,1,2,3,3,3,3] 
                        l
                        i  

        [1,1,2, 2,3,3,1]
                      l
                         i


left 0
right 0
nums [1, 1, 1, 2, 2, 2, 3, 3]
last to last None
last None
current 1
##############
left 1
right 1
nums [1, 1, 2, 2, 1, 2, 3, 3]
                  l
                     r
last to last None
last 1
current 1
##############
left 2
right 2
nums [1, 1, 1, 2, 2, 2, 3, 3]
last to last 1
last 1
current 1
all three same
left 2
right 3
nums [1, 1, 1, 2, 2, 2, 3, 3]
last to last 1
last 1
current 2
##############
left 3
right 4
nums [1, 1, 2, 1, 2, 2, 3, 3]
last to last 2
last 1
current 2
##############
left 4
right 5
nums [1, 1, 2, 2, 1, 2, 3, 3]
last to last 2
last 1
current 2
##############
left 5
right 6
nums [1, 1, 2, 2, 2, 1, 3, 3]
last to last 2
last 1
current 3
##############
left 6
right 7
nums [1, 1, 2, 2, 2, 3, 1, 3]
last to last 3
last 1
current 3
##############


left 0
right 0
nums [1, 1, 1, 2, 2, 3]
            l
               r
last to last None
last None
current 1
##############
left 1
right 1
nums [1, 1, 1, 2, 2, 3]
last to last None
last 1
current 1
##############
left 2
right 2
nums [1, 1, 1, 2, 2, 3]
last to last 1
last 1
current 1
all three same
##############
left 2
right 3
nums [1, 1, 1, 2, 2, 3]
last to last 1
last 1
current 2
##############
left 3
right 4
nums [1, 1, 2, 2, 2, 3]
last to last 2
last 2
current 2
all three same
##############
left 3
right 5
nums [1, 1, 2, 2, 2, 3]
last to last 2
last 2
current 3
##############

        

        '''
        left = 0
        for r in range(len(nums)):
          
            last_to_last = nums[left-2] if (left-2) >= 0 else None
            last = nums[left-1] if (left-1) >= 0 else None
            current = nums[r]

         

            if current == last_to_last == last:
       
                continue

            nums[left], nums[r] = nums[r], nums[left]
            left += 1
           


        return left