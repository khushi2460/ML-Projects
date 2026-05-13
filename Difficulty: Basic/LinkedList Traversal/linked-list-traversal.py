"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def printList(self, head):
        # code here
        current=head
        while current:
            print(current.data,end=" ")
            current=current.next
        
        