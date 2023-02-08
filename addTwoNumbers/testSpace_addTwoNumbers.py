class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1, l2):
    
    l1.reverse()
    l2.reverse()
    
    x = ""
    y = ""
    for i in range(len(l1)):
        x += str(l1[i])
    for i in range(len(l2)):
        y += str(l2[i])
    temp = str((int(x) + int(y)))
    temp = temp[::-1]
    res = []
    for i in range(len(temp)):
        res.append(int(temp[i]))
    return res
    
    
def myReverse(l):
    currentLength = myLength(l)
    head = l
    tail = None
    currentNode = l    
    while currentNode.next != None:
        tail = currentNode.next
        currentNode = currentNode.next
    
    
   
    pass
def myLength(l):
    
    count = 1
    while True:
        if l.next != None:
            count += 1
            l = l.next
        else:
            break
        
    return count

l1 = ListNode(1,ListNode(2,ListNode(3)))

print(myReverse(l1))
# print(addTwoNumbers([2,4,3],[5,6,4]))