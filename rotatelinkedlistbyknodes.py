# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:44:20 2019

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
    
    def rotatebyk(self,k):
        if k==0:
            return
        
        current=self.head
        count=1
        while(count<k and current is not None):
            current=current.next
            count+=1
        
        if current is None:
            return
        
        temp=current
        
        
        while(current.next is not None):
            current=current.next
        
        current.next=self.head
        self.head=temp.next
        temp.next=None
        
        
           
           
    def printlist(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next
        
llist=LinkedList()
llist.push(60)
llist.push(50)
llist.push(40)
llist.push(30)
llist.push(20)
llist.push(10)
llist.rotatebyk(4)
llist.printlist()


        
        
        
        