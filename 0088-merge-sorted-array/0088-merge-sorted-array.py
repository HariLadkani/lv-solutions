class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        input: int arr nums1, int m, int n = len(nums2), int arr nums2
        Output: int array
        goal:
            merge two arrays
        
        input1 = [1,2,2,3,5,6]
                  iw
        input2 = [2,5,6]
                j

        Approach:
            -  i, j = m - 1, n-1
                w = m + n - 1
            - iterate till w >= 0
            - compare i and j and maintain write pointer w 
            - if i >= j: i -= 1
            - else j-=1
            - if i < 0: value at i assume float('-inf)
            - if j < 0, value at j assume float('-inf)

            run time=0(n+m)
            space=o(1)

        [1],
     iw=-1 
        []
         j=-1

       
        constraints:
            0<=m, n<=200

        """
        write_pointer = m + n - 1
        i = m - 1
        j = n -1

        while write_pointer >= 0:
            value_num1 = nums1[i] if i >= 0 else float('-inf')
            value_num2 = nums2[j] if j >= 0 else float('-inf')
            if value_num1 >= value_num2:
                nums1[write_pointer] = value_num1
                i -= 1
            else:
                nums1[write_pointer] = value_num2
                j -= 1
            write_pointer -= 1


        
        