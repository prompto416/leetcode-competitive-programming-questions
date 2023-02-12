
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    l1 = list1
    l2 = list2
    dummy = ListNode()
    cur = dummy
    
   
    
    while l1 or l2:
        if l1 and l2:
            print(l1.val,l2.val)
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next 
            #bug sensitive code 
            elif l1.val == l2.val:
                cur.next = ListNode(l1.val,(ListNode(l2.val)))
                cur = cur.next.next
                l1 = l1.next
                l2 = l2.next
            #not using else to make bug easier to detect when unhandled case is catched
            elif  l1 > l2.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
                
            # #base code not used
            # cur.next = ListNode(l1.val)
            # cur = cur.next
            # l1 = l1.next 
            # l2 = l2.next
        elif l1 and (not l2):
            print(l1.val)
            cur.next = ListNode(l1.val)
            cur = cur.next
            l1 = l1.next
        elif l2 and (not l1):
            print(l2.val)
            cur.next = ListNode(l2.val)
            cur = cur.next
            l2 = l2.next
            
    #for debugging
   
    res = dummy.next
    #for dobule checking
    # while res:
    #     print(res.val)
    #     res = res.next
    return res
        
    
    
    
l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
l2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,))))

print(mergeTwoLists(l1,l2))