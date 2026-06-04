class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hash_s, hash_t ={},{}
        for x in s :
            if x in hash_s:
                hash_s[x]=hash_s[x]+1
            else:
                hash_s[x]=1
        for y in t:
            if y in hash_t:
                hash_t[y]=hash_t[y]+1
            else:
                hash_t[y]=1
        if hash_t == hash_s:
            return True 
        else:
            return False