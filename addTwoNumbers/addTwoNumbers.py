class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    len1 = myLen(l1)
    len2 = myLen(l2)
    final = l1
    most = []
    temp1 = []
    temp2 = []
    if len1 > len2: 
        most = l1
    else:
        most = l2
    temp = l1
    while True:
        try:
            temp1.append(temp.val)
        
            temp = temp.next
        except:
            break
    temp = l2
    while True:
        try:
            temp2.append(temp.val)
        
            temp = temp.next
        except:
            break
    temp1.reverse()
    temp2.reverse()
    x = ""
    y= ""
    for i in range(len(temp1)):
        x += str(temp1[i])
    for i in range(len(temp2)):
        y += str(temp2[i])
    sum = str(int(x)+int(y))
    count = myLen(most)
    while count > 0:
        try:
            print(most.val)
            most = most.next 
        except:
            break


def myLen(l):
    
    count = 1
    while True:
        if l.next != None:
            count += 1
            l = l.next
        else:
            break
        
    return count


l1 = ListNode(5,ListNode(6,ListNode(7,ListNode(8))))
l2 = ListNode(2,ListNode(4,ListNode(3)))

print(addTwoNumbers(l1,l2))