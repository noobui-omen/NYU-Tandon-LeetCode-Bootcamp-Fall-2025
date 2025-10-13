class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        op = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        i = 0
        sign = 1
        
        while i<len(s) and s[i] == " ":
            i+=1

        if i == len(s):
            return 0

        if i<len(s) and s[i] == "-":
            sign = -1
            i+=1
        elif i<len(s) and s[i] == "+":
            i+=1
        
        while i<len(s) and s[i].isdigit():
            d = int(s[i])
            op = op*10 + d

            if sign*op < INT_MIN:
                return INT_MIN
            elif sign*op > INT_MAX:
                return INT_MAX

            i+=1

        return sign*op

# # BETTER SOLUTION
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31
        
#         i = 0
#         n = len(s)
#         result = 0
#         sign = 1
        
#         # 1️⃣ Skip leading whitespace
#         while i < n and s[i] == ' ':
#             i += 1
        
#         # 2️⃣ Check for sign
#         if i < n and (s[i] == '+' or s[i] == '-'):
#             sign = -1 if s[i] == '-' else 1
#             i += 1
        
#         # 3️⃣ Convert digits
#         while i < n and s[i].isdigit():
#             digit = int(s[i])
            
#             # 4️⃣ Check overflow
#             if result > (INT_MAX - digit) // 10:
#                 return INT_MAX if sign == 1 else INT_MIN
            
#             result = result * 10 + digit
#             i += 1
        
#         # 5️⃣ Apply sign
#         return sign * result