class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        '''
        trips is integer and can never be decimal value


        goal:
            all buses completed trips must sum atleast totalTrips

        max = min(time) * totalTrips

        time = [2, 1] totalTrips = 4



        '''

        def valid(target_time):
            total_finished_trips = 0
            for time_per_trip in time:
                total_finished_trips += target_time//time_per_trip

            return total_finished_trips >= totalTrips


        left = 0
        right = min(time) * totalTrips
        res = float("inf")

        while left <= right:
            mid = (left + right) // 2

            if valid(mid):
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1

        return res
        