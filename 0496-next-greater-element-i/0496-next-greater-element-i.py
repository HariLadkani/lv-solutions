class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        '''
        res = [-1] * len(nums1)

        num_map = {}
        for index, num in enumerate(nums1):
            num_map[num] = index


        stack = []

        for num in nums2:
            if not stack:
                stack.append(num)
                continue

            while stack and stack[-1] < num:
                if stack[-1] in num_map:
                    index = num_map[stack[-1]]
                    res[index] = num
                stack.pop()

            stack.append(num)

        return res



            


