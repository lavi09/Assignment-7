# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:06:15 2019

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
            
    def loop(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if (slow==fast):
                print("There is a loop")
                return
        return     
                
llist=LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()
"""llist.head.next.next.next.next = llist.head """

llist.loop()