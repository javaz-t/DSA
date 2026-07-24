class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isAlphaNumeric(s[l]):
                l+=1
            while l<r and not self.isAlphaNumeric(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l = l+ 1 
            r =r- 1
        return True



    def isAlphaNumeric(self, char):
        return (ord('A')<= ord(char) <=ord('Z') or 
        ord('a')<= ord(char)<=ord('z') or 
        ord('0')<= ord(char)<=ord('9')) 
  
        