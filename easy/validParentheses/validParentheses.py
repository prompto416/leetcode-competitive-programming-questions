def isValid(s):
    myStack = []
    
    for i in range(len(s)):
        
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            
            myStack.append(s[i])
        elif (s[i] == ")" or s[i] == "]" or s[i] == "}") :
            myStack.append(s[i])
            if s[i] == ")" and myStack[len(myStack)-2] == "(":
                for i in range(2):
                    myStack.pop()
            elif s[i] == "]" and myStack[len(myStack)-2] == "[":
                for i in range(2):
                    myStack.pop()
            elif s[i] == "}" and myStack[len(myStack)-2] == "{":
                for i in range(2):
                    myStack.pop()
            

    return (len(myStack) == 0)
        
    
    
print(isValid("()"))