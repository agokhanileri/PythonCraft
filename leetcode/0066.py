# 0066. Plus One
# Each digits [i] is the i-th digit of the integer. LSB = Right. Noleading 0's.
# Inc the number by 1 and return the resulting array. 

# ----------------------------------------------------------------------
# Clarifications:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# Can modify in-place and return back? --> Yes

# Inputs:
digits = [9, 9, 9]             # ans = [1, 0, 0, 0]

# ----------------------------------------------------------------------
# Sol1: O(n) / O(1)
n = len(digits)
carry = 1   # mission is to spend the carry
i = n-1     # try from LSB to MSB
while i > 0 and carry == 1: 
    print(digits, i, carry)
    if digits[i] + carry == 10:
        digits[i] = 0   # add 1                
        if i == 1:                          # if MSB is reached already
            digits = [1] + [0]*n            # preceed it with 1 and set rest to 0             
            break                    
    else:             
        digits[i] = digits[i] + carry  # else, simply add +1 and exit
        carry = 0 
    i = i - 1                 
ans = digits
    
      
# ----------------------------------------------------------------------
# Submit: Sol1, O(n) / O(1)
class Solution:
    def plusOne(self, digits, val) -> int:
        n = len(digits)
        carry = 1   # mission is to spend the carry
        i = n-1     # try from LSB to MSB
        while i > 0 and carry == 1: 
            # print(digits, i, carry)
            if digits[i] + carry == 10:
                digits[i] = 0   # add 1                
                if i == 1:                          # if MSB is reached already
                    return [1] + [0]*n            # preceed it with 1 and set rest to 0                                     
            else: 
                digits[i] = digits[i] + carry  # else, simply add +1 and exit
                carry = 0 
            i = i - 1                 
            return digits
        return -1
    

# Q:
# Inputs:



# ----------------------------------------------------------------------
# Sol1:
# - Speed: O() / O()

n = len(digits)

carry = 0
for i in range(0,m)



# ----------------------------------------------------------------------
# Submit: Sol1, O(n) / O(1)


# --------------
# Test:
