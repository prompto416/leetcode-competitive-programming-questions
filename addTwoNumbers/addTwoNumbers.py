def addTwoNumbers(l1, l2):
    
    dummy = ListNode()
    cur = dummy
    carry = 0 

    
    while l1 or l2:
        if l1 and l2:
            sum = l1.val + l2.val + carry 
            carry = 0 
            if sum >= 10:
                carry = 1
                sum -= 10 
            cur.next = ListNode(sum)
            cur = cur.next
            #print(l1.val,l2.val,sum)
            l1 = l1.next
            l2 = l2.next
            print(sum)
        elif l1 and not l2:
    
            sum = l1.val + carry 
            carry= 0 
            if sum >= 10:
                carry= 1
                sum -= 10 
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            print(sum)
        elif l2 and not l1:
        
            sum = l2.val + carry
            carry = 0 
            if sum >= 10:
                carry= 1
                sum -= 10 
            cur.next = ListNode(sum)
            cur = cur.next
            l2 = l2.next
            print(sum)
    if carry > 0:
        cur.next = ListNode(1)
        cur = cur.next
    return dummy.next





















# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def addTwoNumbers(l1, l2):
    
#     dummy = ListNode()
#     cur = dummy
#     carry = 0 
  
    
#     while l1 or l2:
#         if l1 != None and l2 != None:
          
#             sum = l1.val + l2.val + carry
       
 
#             carry = 0 
#             if sum >= 10:
#                 carry = 1
#                 sum -= 10 
#             cur.next = ListNode(sum)
#             cur = cur.next
#             #print(l1.val,l2.val,sum)
#             l1 = l1.next
#             l2 = l2.next
        
#         elif( l1 != None) and ( l2 == None):
      
#             sum = l1.val + carry 
#             carry= 0 
#             if sum >= 10:
#                 carry= 1
#                 sum -= 10 
#             cur.next = ListNode(sum)
#             cur = cur.next
#             l1 = l1.next
          
#         elif (l2 != None) and (l1 == None):
        
#             sum = l2.val + carry
#             carry = 0 
#             if sum >= 10:
#                 carry= 1
#                 sum -= 10 
#             cur.next = ListNode(sum)
#             cur = cur.next
#             l2 = l2.next
            
#     if carry > 0 :
#         cur.next = ListNode(1)
#         cur = cur.next

#     return dummy.next
            
    
   

# l1 = ListNode(5,ListNode(6,ListNode(7,ListNode(8))))
# l2 = ListNode(2,ListNode(4,ListNode(3)))


# l1 = ListNode(1,ListNode(2,ListNode(3)))
# l2 = ListNode(9,ListNode(9,ListNode(3,ListNode(4))))
# addTwoNumbers(l1,l2)
# print()