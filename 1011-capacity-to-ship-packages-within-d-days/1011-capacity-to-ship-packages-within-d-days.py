class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = 0, sum(weights)


        #[1, 2, 3, 4, 5]
        def can_ship(capacity):
            total_days = 0
            curr_weight = 0
            for weight in weights:
                if weight > capacity:
                    return False
                if curr_weight == 0:
                    total_days += 1

                curr_weight += weight
                if curr_weight == capacity:
                    curr_weight = 0

                elif curr_weight > capacity:
                    total_days += 1
                    curr_weight = weight

            print("capacity", capacity)
            print("total_days", total_days)
            return total_days<=days


       

        while left < right:
            capacity = (left + right) // 2

            

            if can_ship(capacity):
                right = capacity 
            
            else:
                left = capacity + 1

            print("#########3")

        return right
