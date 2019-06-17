# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:54:33 2019

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
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
    def swappair(self):
        if(self.head is not None and self.head.next is not None):
            self.head.data,self.head.next.data=self.head.next.data,self.head.data
      swappair(self.head.next.next)
            
            
llist=LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()
