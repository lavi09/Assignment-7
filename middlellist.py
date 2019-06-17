# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:43:22 2019

@author: Lavi
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def middle(self):
        fast=slow=self.head
        if(self.head is not None):
            while(fast is not None and fast.next is not None):
                fast=fast.next.next
                slow=slow.next
            print("middle element is ",slow.data)
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
llist=LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()
llist.middle()

        
        
        