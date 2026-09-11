class Solution:
    def minimumPushes(self, word: str) -> int:
        '''
        goal:
            min number of pushes to type word

        constraints:
            can map digits 2 to 9 to distinct letters
            one letter cannot belong to more than one digit


        "xyzxyzxyzxyz"

        x: 4
        y:4
        z:4


        aabbccddeeffgghhiiiiii
        a:2
        b:2
        c:2
        d:2
        e:2
        f:2
        g:2
        h:2
        i:6
        [(2,a),(2, b),(2,c),(2,d), (2,e), (2, f), (2,g), (2, h), (6,i), (0, k), (0, l)]

        [(6, i), (2,a), (2,b)......(0, l)]

         

        8 slots
        6*1 = (freq * keyDistance)
        7slots:
        2*1
        ....
        1 slot
        2*1
        0 slots

        slot reset to 8 but value of keyDistance increases
        maintain an array and sort it on freq and stop when freq gets 0
        [2,1,c,d,e,f,g,h,i,j...., z]

        aabbccddeeffgghhiiiiii
          i

        ord('a')-ord('a') = 0
        ord('b') - ord('a') = 1
        ord('z') - ord('a') = 25
         

        '''

        freq_arr = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            freq_arr[index] += 1
      

        freq_arr.sort(reverse=True)
        key_distance = 0
        res = 0

        for i in range(26):
            if i%8 == 0:
                key_distance += 1

            freq = freq_arr[i]
            res += freq * key_distance
        

  
        return res