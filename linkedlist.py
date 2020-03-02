# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:12:11 2020

@author: CN261
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        self.endval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    #Inserting at the Beginning of the Linked List
    def add_parent_node(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    #Inserting at the end of the Linked List
    def add_end_node(self,newdata):
        EndNode = Node(newdata)
        EndNode.nextval = self.endval
        self.endval = EndNode
        return        

list_ = SLinkedList()
list_.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list_.headval.nextval = e2
e2.nextval = e3
e3.nextval = Node("Thurs")
list_.listprint()

list_.add_parent_node("Sunday")
list_.add_end_node("Saturday")

