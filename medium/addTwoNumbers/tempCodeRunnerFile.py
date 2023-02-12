
count = 0 
def counter(num):
    count += 1
    if num > 10:
        return
    global count 
    counter(count)
    
counter()