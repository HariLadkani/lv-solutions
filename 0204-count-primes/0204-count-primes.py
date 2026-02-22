class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        [false,false,TRUE,TRUE,false,TRUE,False,TRUE,False,fa;se]
          0    1    2    3         
        initialize (n) elements wit true
        set 0 and 1 to false

        run sieve algorithm
        '''
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False
        print(int(math.sqrt(n)))
        for number in range(2, int(math.sqrt(n)+1)):
            if isPrime[number]: 
             
                for mul in range(number*number, n, number):
                 
                    isPrime[mul] = False
        count = 0
        for boolean in isPrime:
            if boolean == True:
                count += 1
        return count


        