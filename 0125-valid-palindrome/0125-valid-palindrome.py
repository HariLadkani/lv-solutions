class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1

     

        while left < len(s) and right >= 0:
            while left < len(s) and not(s[left].isalnum()):#start from char
                print(s[left])
                left += 1

            while right > 0 and not(s[right].isalnum()):
                print(s[right])
                right -= 1

            if left < len(s) and right > 0 and s[left].lower() != s[right].lower():
                return False

            if left < len(s):
                print("left", left)
                print(s[left])
            if right > 0:
                print('right', right)
                print(s[right])
            print("#####")

            left += 1
            right -= 1

           
            
        
        return True
        


        

        