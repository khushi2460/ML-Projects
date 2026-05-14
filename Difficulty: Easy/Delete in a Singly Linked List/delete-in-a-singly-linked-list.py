'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        
        if not head:
            return None
        if x == 1:
            return head.next

        prev = head
        curr = head.next
        pos = 2

        while curr:
            if pos == x:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            pos += 1

        return head
                

