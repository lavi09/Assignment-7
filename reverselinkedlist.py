# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:32:55 2019

@author: Lavi
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node    
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next     
               
    def reverse(self): 
        current,prev=self.head,None
        while(current is not None):
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev
    
  
llist = LinkedList() 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1)   

print("Before reversing")
llist.printlist()            
print("After reversing")
llist.reverse()
llist.printlist()