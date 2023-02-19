def backspaceCompare(s: str, t: str) -> bool:
    count_s = 0
    count_t = 0 
    for i in reversed(range(len(s))):
        if s[i] == "#":
            count_s += 1
            s = s[:i] + s[i+1:]
        elif s[i] != "#" and count_s > 0:
            
            s = s[:i] + s[i+1:]
        

            count_s -= 1 
            
    for i in reversed(range(len(t))):
        print(t[i],count_t)
        if t[i] == "#":
            count_t += 1
            t = t = t[:i] + t[i+1:]
        elif t[i] != "#" and count_t > 0:
            t = t[:i] + t[i+1:]
            count_t -= 1 
    
    
    return s == t

            


print(backspaceCompare("xywrrmp","xywrrmu#p"))