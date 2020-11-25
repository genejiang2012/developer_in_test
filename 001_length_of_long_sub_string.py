class Solution:
    def get_length_of_longest_substring(self, s: str) -> int:
        dic = {}
        start = 0
        maxlen = 0

        # choose the bigger indexs between last start and repeate elem. 
        # for example, "abba", start = 0, repeate index = 1, choose 1. 
        for i,x in enumerate(s):
            if s[i] in dic:
                start = max(start, dic[x]+1) 
                dic[x] = i
            else:
                dic[x] = i

            if i - start + 1 > maxlen:
                maxlen = i- start + 1
            
        return maxlen

s = Solution()
print(s.get_length_of_longest_substring('abba'))
print(s.get_length_of_longest_substring('aaaa'))

