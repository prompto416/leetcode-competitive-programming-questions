class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    prev = None
    while head:
        next_node = head.next
        head.next = prev 
        prev = head 
        head = next_node 
    return head 
        

    

a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
reverseList(a)
