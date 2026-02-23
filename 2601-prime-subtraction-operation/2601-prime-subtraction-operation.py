class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        '''

        goal:
            return increasing array where each element is nums[i] - prime number<3

        [4,9,6,10]

         4: 2 and 3 = 2,11
         9: 2,3,5,7 = 7,6,4,2
         10 = 7,5,3,2

         nums[i] - prime(maximum)
        6-5 = 1
        1, 2, 6, 10

        [5,8,3]

        5 or (5-3)
        8 or (8-7) = 1
            8 - 5 = 3
        2,3,5,7
           l     r
        8-3 = 5
        8 - 5 = 3
        [2, 3]

        violation: we need bigger diff
        diff = nums[i] - prime

        diff = 

        goal:
            smallest possible difference that works for the increasing order

            if diff maintains increasing order:
                make diff smaller
                increase prime by moving to the right in binary search
            else:
                make diff large 
                reduce the prime and move left

        [False, False, True, True, False, True, False, True, False, False, False, True, False,  True, False, False, False, True, False, True]

        2,3,5,7,11,13,17,19
                   l                 
                   r
        '''
        if len(nums) < 2:
            return True
        max_value = max(nums)
        def calculate_primes(n):
            is_primes = [True] * n
            is_primes[0] = is_primes[1] = False

            for number in range(2, int(math.sqrt(n))+1):
                if is_primes[number]:
                    for mul in range(number * number, n, number):
                        is_primes[mul] = False
            
            return is_primes

        primes = calculate_primes(max_value)
        primes = [i for i in range(len(primes)) if primes[i]]
    
        print("primes", primes)
        res = []
        for number in nums:
            last_valid_diff = None
            left,right = 0, len(primes)-1 #2, 3

            while left <= right:
                mid = (left + right) // 2 
                print("mid", mid)
                prime = primes[mid]
                print("prime", prime)

                if number <= prime:
                    right = mid - 1 #2
                    continue

                diff = number - prime
                if len(res) == 0 or diff > res[-1]: #monotonic property maintained
                    left  = mid + 1
                    last_valid_diff = diff
                else: #monotonic property violated
                    right = mid - 1
                    

            
            print(last_valid_diff)
            if last_valid_diff is None:
                if len(res) == 0 or number > res[-1]:
                    res.append(number)
                else:
                    return False
            else:
                res.append(last_valid_diff)

            print("res", res)
        return len(res) == len(nums)




