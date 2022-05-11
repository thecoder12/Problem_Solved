'''
https://www.geeksforgeeks.org/find-largest-word-dictionary-deleting-characters-given-string/

Giving a dictionary and a string ‘str’, find the longest string in dictionary which can be formed by deleting some characters of the given ‘str’. 
Examples: 

Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple 

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
                                        " forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks
'''

dict1 = ["ale", "apple", "monkey", "plea"]
str1 = "abpcplea" 

for d in dict1: #ale
    for dd in list(d):
        for i in list(str1): #a
            if i == dd:
                continue
            else:
                