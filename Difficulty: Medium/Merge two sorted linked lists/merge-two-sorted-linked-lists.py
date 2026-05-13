'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        tail = dummy
        c1 = head1
        c2 = head2
        while c1 and c2:
            if c1.data <= c2.data:
                tail.next = c1
                c1 = c1.next
            else:
                tail.next = c2
                c2 = c2.next
            tail = tail.next
        if c1:
            tail.next = c1
        else:
            tail.next = c2
            
        return dummy.next

                
        