class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        operations could be >= 0 till infinity

        goal:
            true if atleast one element in triplets array equal to target triplet

        [max(ai, aj), max(bi, bj), max(ci, cj)]

        [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
            i              j

        iterate over all triplets
        maintain first_target_found, second_target_found, third_target_found


        triplets = []
        target = [2,2,2]
        '''

        triplets_copy = []
        first_found, second_found, third_found = False, False, False
        target_first, target_second, target_third = target
        for first,second,third in triplets:
            if first <= target_first and second <= target_second and third<=target_third:
                triplets_copy.append([first,second,third])


        for first, second, third in triplets_copy:
            if first == target_first:
                first_found = True

            if second == target_second:
                second_found = True
            
            if third == target_third:
                third_found = True

            
            if first_found and second_found and third_found:
                return True

        return False


        

