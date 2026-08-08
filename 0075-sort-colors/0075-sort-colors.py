class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [2,0,2,1,1,0]
         l 
                    r

        [0,1,2]
         l
           r
              i

         

        process:
            l = 0
            r = len(nums)-1
            i=0
            loop till i < r

                loop r -=1 till nums[r] == 2
                loop l +=1 till nums[l] == 0

                if nums[i] == 0:
                    swap with nums[left]

                if nums[i] == 2:
                    swap with nums[right]

                i += 1


        nums [1, 0, 2]
              l
                 r
                 i
        i 0
        left 0
        right 2
        nums [1, 2, 0]
        end++++++
        nums [1, 2, 0]
        i 1
        left 0
        right 2
        nums [1, 0, 2]
        end++++++
        nums [1, 0, 2]
        i 2
        left 0
        right 2
        nums [1, 0, 2]
        end++++++



        """

        l = 0
        r = len(nums) - 1
        i = 0 
        
        while i <= r:
            while r > i and nums[r] == 2:
                r -= 1

            while l < len(nums) - 1 and nums[l] == 0 and l < i:
                l += 1
            print("nums", nums)
            print("i", i)
            print("left", l)
            print("right", r)

            
            
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]

            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]

            i += 1

            print("nums", nums)
            print("end++++++")

            
        