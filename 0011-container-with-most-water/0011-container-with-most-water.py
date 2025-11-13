class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        clarify: we are given heights array. Return max water that can be contained 
        between two heights(vertical lines)

        heights = [1, 8, 6, 2,  5, 4, 8, 3, 7]
        ans = 49

        goal:
            max area between any two heights



        size of heights: 0 to 10^4
        can heights[i] < 0: no
        if len(heights) == 0: return 0
        if all heights have 0s? return 0
        can there be duplicate heights? yes
        can answer be 0? yes    
        area would be (height2_index - height 1 index) * min(heigh1, height2)?\

        Brute force:
            iterate with index over the entire array
            for each index, nest iterate over index + 1 to end of array
                find out max area 

            return max area

            run time: o(n^2)
            space: o(1)

        Properties:
            to maximize area:
                maximize width(diff in index)
                maximize height


        Optimized approach:
        iterate till left < right:
            Two pointer approach
            start from left and right and shrink inwards
            area = compute diff in index * min(height1, height2)
            max_area = max(area, max_area)

            if height1<=height2:
                left += 1

            else:
                right -= 1

        run time = o(n)
        space = o(1)
        '''

        if len(height) == 0:
            return 0


        left, right = 0, len(height)-1
        max_area = float("-inf")
        while left < right:
            width = right - left
            height_curr = min(height[left], height[right])
            max_area = max(max_area, width * height_curr)

            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

        return max_area 
        