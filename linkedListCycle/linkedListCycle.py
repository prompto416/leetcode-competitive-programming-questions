class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle( head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head 
        fast = head.next 
        if fast == None:
            return False
       

        while fast != slow:
            if (fast == None) or (fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next


        return True
            

print(hasCycle(ListNode(1,ListNode(2))))
