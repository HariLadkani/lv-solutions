class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        if slope=0; becomes slope = +inf and -inf
        if slope=2; becomes
        (0, 1)
        (1, 2)
        (2, 1)
        (1, 0)


        10:4
        11: 2

        max should return 4 and min should return 2

        '''

        def calculate_distance(p1, p2):
            x1,y1 = p1
            x2,y2=p2
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)

        distance = [
            calculate_distance(p1, p2),
            calculate_distance(p1, p3),
            calculate_distance(p1, p4),
            calculate_distance(p2, p3),
            calculate_distance(p2, p4),
            calculate_distance(p3, p4),
        ]

        freak_counter = collections.Counter(distance)

        if len(freak_counter) != 2:
            return False
        
        diag = min(freak_counter.values())
        sides = max(freak_counter.values())

        return diag == 2 and sides == 4


            