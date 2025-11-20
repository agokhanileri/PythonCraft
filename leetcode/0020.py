# 0020. Valid Parentheses

# Given a string s consisting of parentheses '()[]{}' '(', ')', '{', '}', '[' ']', 
# determine if the input string is valid s.t. open brackets must be closed by the same 
# type of brackets in the correct order.

# ----------------------------------------------------------------------
# Clarifications:
# empty str --> True, 1 <= s.length <= 104

# Inputs:
s = "()[]{}"    # True
s = "{[())]}"    # True

# ----------------------------------------------------------------------
# Sol1: Using stack, O(n) / O(n)
n = len(s)
stack = []              # stack to keep/check the order
# if n == 0: ans = True  --> no need since it's given n >=1    
ans = None
for ch in s:
    #print(ch, stack, ans)      
    if ch in ['(', '[', '{']:       # push the open pharantheses encountered
        stack.append(ch)            #
    if ch in [')', ']', '}']:       # if closed bracket found
        if stack == []:             # but no open brackets yet
            ans = False; break      # invalid            
        popped = stack.pop()        # o.w. pop the last open pharanthesis and compare
        print(popped)
        if ch == ')' and popped = '(':  # if no pair matched, invalid!
            continue 
        elif ch == ']' and popped = '[':
            continue 
        elif ch == '}' and popped = '{':
            continue 
        elif len(stack) > 0:        # unclosed bracket remaining
            ans = False; break
        #else:                      # everything passes, valid!  
        #    ans = True


# ----------------------------------------------------------------------
# Sol2: Using case, O(n) / O()
stack = []              # stack to keep/check the order
ans = None

def comp(a, b):
    '(': 
for ch in s:    
    chase if ch in ['(', '[', '{']:       # push the open pharantheses encountered
        stack.append(ch)            #
    if ch in [')', ']', '}']:       # if closed bracket found
        if stack == []:             # but no open brackets yet
            ans = False; break      # invalid            
        popped = stack.pop()        # o.w. pop the last open pharanthesis and compare
        if ch == ')' and popped != '(':  # if no pair matched, invalid!
            ans = False; break 
        elif ch == ']' and popped != '[':
            ans = False; break 
        elif ch == '}' and popped != '{':
            ans = False; break 
        elif len(stack) > 0:        # unclosed bracket remaining
            ans = False; break
        else:                       # everything passes, valid!  
            ans = True
    print(ch, stack, ans) 


# ----------------------------------------------------------------------
# Submit: Sol1, O() / O()
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for ch in s:
            # print(ch, stack, ans)
            if ch in ['(', '[', '{']:
                stack.append(ch)
            if ch in [')', ']', '}']:       # if closed bracket found
                if stack == []:             # but no open brackets yet
                    return False            # invalid
                popped = stack.pop()
                if ch == ')' and popped != '(':  # if no pair matched, invalid!
                    return False
                elif ch == ']' and popped != '[':
                    return False
                elif ch == '}' and popped != '{':
                    return False
                else:                       # ignore other chars
                    pass    # ans = True

        #print(ch, stack, ans)
        if len(stack) > 0:                  # check for still open brakcets
            return False
        return True                         # if everything passes, valid!      
       
# --------------
# Test:
sol = Solution()
sol.isPalindrome(x)