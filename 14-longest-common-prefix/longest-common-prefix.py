class Solution(object):
    def longestCommonPrefix(self, strs):
        output=''
        for i in range(len(strs[0])): # first word len
            tempVal = strs[0][i]
            for x in strs:
                if i == len(x) or x[i]!=tempVal:#check reach the min word length 
                    return output
            output = output + tempVal
        return output

        
        