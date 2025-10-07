class Solution:
    def twoSum(self, num: List[int], t: int) -> List[int]:
        ln = len(num)
        i, j = 0, ln-1
        while i<j:
            if num[i]+num[j]>t: 
                j-=1
            if num[i]+num[j]<t:
                i+=1
            if num[i]+num[j]==t: 
                return [i+1,j+1]
            