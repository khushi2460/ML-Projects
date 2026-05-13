'''
Definition for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        return count