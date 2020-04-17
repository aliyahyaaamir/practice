def helper(str1: str, str2: str, shortest: str):
    
    if not str1:
        print('wow')
        if not str2:
            return shortest
        return helper(str2, str2, shortest)
    
    if str1[0] != str2[0]:
        print('here')
        return helper(str1[1:], str2, shortest + str1[0])
    
    if str1[0] == str2[0]:
        print('there')
        return helper(str1[1:], str2[1:], shortest + str1[0])

# class Solution:
    
#     def helper(self, str1: str, str2: str, shortest: str):
        
#         if not str1:
#             if not str2:
#                 return shortest
#             return self.helper(str2, str2, shortest)

#         if not str2:
#             if not str1:
#                 return shortest
#             return self.helper(str1, str1, shortest)
        
#         if str1[0] != str2[0]:
#             output1 = self.helper(str1[1:], str2, shortest + str1[0])
#             output2 = self.helper(str1, str2[1:], shortest + str2[0])
#             if len(output1) < len(output2):
#                 return output1
#             return output2

#         if str1[0] == str2[0]:
#             return self.helper(str1[1:], str2[1:], shortest + str1[0])
    
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         return self.helper(str1, str2, '')


if __name__ == "__main__":
    output = helper('abac', 'cab', '')