# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# def addTwoNumbers(l1, l2):
    
#     pass
    
    
# def myReverse(l):
#     currentLength = myLength(l)
#     head = l
#     tail = None
#     currentNode = l    
#     while currentNode.next != None:
#         tail = currentNode.next
#         currentNode = currentNode.next
    
    
   
#     pass
# def myLength(l):
    
#     count = 1
#     while True:
#         if l.next != None:
#             count += 1
#             l = l.next
#         else:
#             break
        
#     return count

# l1 = ListNode(9,ListNode(2,ListNode(9,ListNode(4))))
# l2 = ListNode(1,ListNode(2,ListNode(3)))
# res = ListNode()
# currentNode = ListNode()
# carry = 0
# sum = l1.val + l2.val 
# if sum >= 10:
#     sum -= 10 
#     carry += 1
# res.val = sum 
# l1= l1.next
# l2 = l2.next
    
# while l1 or l2:

#     if l1 != None and l2 != None:
       
#         sum = l1.val + l2.val + carry
#         carry = 0 
#         if sum >= 10:
#             sum -= 10 
#             carry += 1
#         print("sum",sum )       
#         l1= l1.next
#         l2 = l2.next
#         currentNode.val = sum
#         res.next = currentNode.val
#         currentNode = ListNode()
#     elif l1 != None and l2 == None:
#         sum = l1.val + carry
#         carry = 0
#         if sum >= 10:
#             sum -= 10 
#             carry += 1
#         print("l1",sum)
#         l1 = l1.next
#         currentNode.val = sum
#         res.next = currentNode.val
#         currentNode = ListNode()
#     elif l1 == None and l2 != None:
#         sum = l2.val + carry
#         carry = 0
#         if sum >= 10:
#             sum -= 10
#             carry += 1
        
#         print("l2",sum)
#         l2 = l2.next
#         currentNode.val = sum
#         res.next = currentNode.val
#         currentNode = ListNode()
#     else:
#         break
    
    
    
    



# # print(addTwoNumbers([2,4,3],[5,6,4]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
l2 = l1

dummy = ListNode()
cur = dummy


i= 0 
while l1 and i < 2:
    cur.next = ListNode(l1.val)
    l1 = l1.next
    cur = cur.next

    i += 1
res = dummy.next
quit()
while res:
    print(res.val)
    res= res.next

    
    



