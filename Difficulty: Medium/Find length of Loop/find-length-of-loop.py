'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''


class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.countNodes(slow)
        return 0
    def countNodes(self, ptr):
        count = 1
        temp = ptr
        while temp.next != ptr:
            count += 1
            temp = temp.next
            
        return count

        