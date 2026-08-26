class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        consecutive cards meaning? increasing order?

        goal:
            true if she can arrange cards
            false otherwise

            - split into group of size groupsize with increasing cards

            - cards in group can diff by atmost 1

        approach:
            return false if len(hand) not divisible by groupsize

            maintain a hashmap of value: count

            start with a min value and keep adding 1 and finding if value found in map:
            if value found, reduce count and increment group count.


        [1,2,3,6,2,3,4,7,8]

        starting = 1
        group = 
        total = 9
        (1,2,3)
        accumutated_count = 0
        1: 0
        2: 2
        3: 1
        4: 1
        6: 1
        7: 1
        8: 1

       
        (2,1)
        3: 2
        4: 1
        6: 1
        7: 1
        8: 1

        [1,2,3, 10^6, 10^6+1, 10^6+2]

        starting  = 1
        (1, 2, 3)
        accumulated = 0
        1: 0
        2: 0
        3: 0
        10^6: 1
        10^6+1: 1
        10^6+2:1

        (value, count)

       
     
        
        (10^6, 1)
        (10^6+1, 1)
        (10^6+2, 1)

        [1,2,3,6,2,3,4,7,8]

        '''

        if len(hand) % groupSize != 0:
            return False

        freq_map = Counter(hand)
        hand.sort()
        starting_index = 0
        total = 0

        
        while total < len(hand):
            starting_value = hand[starting_index]
            for value in range(starting_value, starting_value + groupSize):
                if value not in freq_map:
                    return False
                
                freq_map[value] -= 1
                if freq_map[value] == 0:
                    del freq_map[value]

                total += 1

            while starting_index < len(hand) and freq_map[starting_value] == 0:
                starting_index += 1
                starting_value = hand[starting_index] if starting_index < len(hand) else None


        return True
