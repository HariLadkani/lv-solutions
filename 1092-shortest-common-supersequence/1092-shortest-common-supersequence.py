class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        input: string str1 and string str2
        Output: string result
        goal:
            shortest string from which we can form str1 and str2
            str1 and str2 would be subsequences of shortest string

        Question:
            min size of str1 and str2? 1
            max size of str1 and str2? 1000
            does str1 and str2 only contain english letters? yes lower case
        
                a   b   a   c
            c       bcac cac cab cab 
            a  abac bac ac ac ab
            b  abac bac bac bc  b                   
               abac bac  ac  c

    
        '''

        ROWS, COLS = len(str2), len(str1)
        dp_row = [""] * (COLS)
        
        postfix = ""
        for col in range(COLS-1, -1, -1):
            postfix =  str1[col] + postfix
            dp_row[col] = postfix
        
        for row in range(ROWS-1, -1, -1):
            current_row = [""] * (COLS)
            for col in range(COLS-1, -1, -1):

                if str1[col] == str2[row]:
                    current_row[col] = str1[col] + (dp_row[row+1] if row + 1 < ROWS else "")
                
                else:
                    use_str2 = dp_row[row+1] if row+1<ROWS else str1[col:COLS]
                    use_str1 = current_row[col+1] if col + 1 < COLS else str2[row:ROWS]

                    if len(use_str2) <= len(use_str1):
                        current_row[col] = str2[row] + use_str2
                    else:
                        current_row[col] = str1[col] + use_str1
            dp_row = current_row
  
        return dp_row[0]


        


            