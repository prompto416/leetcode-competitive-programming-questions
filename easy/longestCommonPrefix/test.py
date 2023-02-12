import os
 
# Initializing the list of strings
ini_strlist = ['akshat', 'aweqweqwdqw', 'azxczxcxz', 'agfgfgf']
 
# Using the Python built-in function os.path.commonprefix() to find the common prefix of the list of strings
prefix = os.path.commonprefix(ini_strlist)
 
# Printing the result
print("Resultant prefix", prefix)