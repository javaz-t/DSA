class Solution(object):
    def longestCommonPrefix(self, strs):
        output=''
        minLen = min(len(word) for word in strs)
        if len(strs)==0:
            return output
        for i in range(minLen):
            tempVal = strs[0][i]
            for x in strs:
                if x[i]!=tempVal:
                    return output
            output = output + tempVal
        return output

        
        