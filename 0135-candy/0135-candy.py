class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        goal:
            min candidies needed while following
                - each element in ratings gets >= 1 candies
                - high rating children get more candies than neighbours
                    equal rating children get same candies

        what is neighbour? left and right of element[i]

        [1, 0, 2]
         2  1  2


        [1,3,2,1]
         1 

        for each element:
            give one candy to start with
            check neighbour if rating high than neightbor, assign value high than both neighbour

        [1,2,2]
        min_heap [(1, 0), (2, 1), (2, 2)]
        rating 1
        index 0
        left_rating 1
        right_rating 2
        left 0
        right 0
        candies[index] 1
        total_candies 1
        ###################
        rating 2
        index 1
        left_rating 1
        right_rating 2
        left 1
        right 0
        candies[index] 2
        total_candies 3
        ###################
        rating 2
        index 2
        left_rating 2
        right_rating 2
        left 2
        right 0
        candies[index] 2
        total_candies 5
        ###################
        '''
        min_heap = []
        for index, rating in enumerate(ratings):
            heapq.heappush(min_heap, (rating, index))

        candies = [0] * len(ratings)
        total_candies = 0
   
        while min_heap:
            rating, index = heapq.heappop(min_heap)
           
            left = candies[index-1] if index-1 > -1 else 0 
            right = candies[index+1] if index + 1 < len(ratings) else 0
            left_rating = ratings[index-1] if index-1 > -1 else rating
            right_rating = ratings[index+1] if index+1 < len(ratings) else rating


            if rating > left_rating and rating > right_rating:
                candies[index] = max(left, right) + 1

            elif rating > left_rating:
                candies[index] = left + 1

            elif rating > right_rating:
                candies[index] = right + 1

            else:
                candies[index] = 1

    
 
   
            total_candies += candies[index]


        return total_candies
        
