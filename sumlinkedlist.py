# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:18:28 2019

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
    
    def add(self,a,b,carry=0):
        if (not a and not b and not carry ):
            return None
        a_val=a.data if a else 0
        b_val=b.data if b else 0
        total=a_val+b_val+carry
        
        a_next=a.next if a else None
        b_next=b.next if b else None
        carry_next=1 if total >=10 else 0 
        print (total%10)
        return Node(total%10,add(a_next,b_next,carry_next))
        
                
    
            
    
firstlist=LinkedList()
firstlist.push(3)
firstlist.push(6)
firstlist.push(5)
print("First List is :")
firstlist.printlist()
secondlist=LinkedList()
secondlist.push(2)
secondlist.push(4)
secondlist.push(8)
print("second list is:")
secondlist.printlist()
print("Sum of the list:")
resultlist=LinkedList()
resultlist.add(firstlist.head,secondlist.head)
resultlist.printlist()