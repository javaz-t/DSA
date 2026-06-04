class Solution(object):
    def isAnagram(self, s, t):
        #check same length or not 
        if len(s)!=len(t):
            return False
        hash_s, hash_t ={},{}
        for i in range(len(s)) :
            # s 
            if s[i] in hash_s:
                hash_s[s[i]]=hash_s[s[i]]+1
            else:
                hash_s[s[i]]=1
            # t
            if t[i] in hash_t:
                hash_t[t[i]]=hash_t[t[i]]+1
            else:
                hash_t[t[i]]=1
        if hash_t == hash_s:
            return True 
        else:
            return False