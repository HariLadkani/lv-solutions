class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''
        start at (0,0)
        input: moves array where valid moves are (l, r, u, d)
        goal:
            true if end at (0,0) after all moves
            false else

        constraint:
            r = move right by 1 magnitude
            same for l, up, down

        Ups must be equal to downs
        lefts must be equal to rights

        approach:
            maintain a hashmap of 4 elements U, D, L, R
            iterate over each char
            increment freq

            return true if (U.freq == D.freq) and (l.freq == r.freq)
        run time = o(n)
        space = 0(1)
        '''
        freq_map = {"U":0, "D":0, "L":0, "R":0}

        for move in moves:
            freq_map[move] += 1

        return ((freq_map["U"] == freq_map["D"]) and 
                (freq_map["L"] == freq_map["R"]))
        