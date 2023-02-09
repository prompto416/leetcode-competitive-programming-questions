def isValid(s):
    pivot = s[0]
    res = False

    i = 1
    while i < len(s):

        a = ord(pivot)
        b = ord(s[i])
        print(a,b,"start")
        if (a<b):
            if (b-a == 1) or (b-a == 2):
                print(a,b)
                res = True
        else:
            res = False
        if i < len(s)-1:
            pivot = s[i+1]
            i+= 1
        i += 1
    return res
        

print(ord("("))
print(ord(")"))

print(ord("["))
print(ord("]"))


print(ord("{"))
print(ord("}"))

    

    
    
    
    
    
print(isValid("(){}}{"))