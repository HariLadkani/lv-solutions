class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if abs(diff) < abs(min_diff):
                min_diff = diff

        res = []
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1]
            if diff == min_diff:
                res.append([arr[i-1], arr[i]])

        return res
            



