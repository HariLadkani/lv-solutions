class Solution:
    def reorganizeString(self, s: str) -> str:
        '''

        Goal:
            return string with no two same characters adjacent
            return "" if not possible

        Constrains:
            no two same chars adjacent  

        approach:
            count freq of each character
            put in max heap and pop frequent element
            push to not available array to ensure next iteration does not use same char

            run time:
                o(n)
            space:
                o(n)
        
        "aaab"
    
      

        res = aba
        cooldown = 




        
        '''

        freq_map = Counter(s)
        max_heap = [(-freq, character) for character, freq in freq_map.items()]
        res = ""
        heapq.heapify(max_heap)
        coolDown = None

        while max_heap:
            freq, character = heapq.heappop(max_heap)
            res += character
            freq += 1

            if coolDown:
                heapq.heappush(max_heap, coolDown)
                coolDown = None

            if freq != 0:
                coolDown = (freq, character)


        return res if not coolDown else ""





        