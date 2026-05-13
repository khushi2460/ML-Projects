'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
      # code here
      newnode = Node(val)
      current=head
      count=0
      if pos==1:
          newnode.next=head
          head = newnode
      elif pos>1:
          while current:
              count+=1
              if count==(pos-1):
                  newnode.next = current.next
                  current.next = newnode
              current =current.next
      return head
            
              
              
          
      
      