class Solution:
    def maxLength(self, arr: list[str]) -> int:
        res = 0

        def dfs(index, curr_string):
            nonlocal res
            if index == len(arr):
                res = max(res, len(curr_string))
                return

            current_element = arr[index]
            current_element_set  = set()
            skip = False
            for char in current_element:
                if char in current_element_set or char in curr_string:
                    skip=True
                    break

                current_element_set.add(char)

            if skip == False:
                new_string = curr_string.union(current_element_set)
                dfs(index+1, new_string)

            dfs(index+1, curr_string) #skipped

        dfs(0, set())
        return res