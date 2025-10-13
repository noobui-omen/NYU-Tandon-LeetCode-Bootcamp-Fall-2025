class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_arr = [0] * 26
        p_arr = [0] * 26
        res = []

        for i in range(len(p)):
            s_arr[ord(s[i]) - ord("a")] += 1
            p_arr[ord(p[i]) - ord("a")] += 1
        
        if s_arr == p_arr:
            res.append(0)

        l = 0
        for i in range(len(p), len(s)):
            
            s_arr[ord(s[l]) - ord("a")] -= 1
            s_arr[ord(s[i]) - ord("a")] += 1
            # print(s_arr)

            l += 1
            if s_arr == p_arr:
                res.append(l)

        return res

# # ALTERNATE SOLUTION
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         res=[]
#         hashmap=Counter(p)
#         for i in range(len(s)-len(p)+1):
#             if Counter(s[i:i+len(p)])==hashmap:
#                 res.append(i)
#         return res        