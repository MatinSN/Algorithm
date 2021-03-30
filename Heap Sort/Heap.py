# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:44:53 2021

@author: MatinSN
"""


class Heap:
    
    
    def buildTree(self,maxSize):
        self.heap = [-1] * maxSize
        self.n = -1
        
    
    def addNode(self,val):
        
        self.n += 1
        self.heap[self.n] = val
        i = self.n
        
        while  i  >= 1:
            
            if self.heap[i] > self.heap[i//2]:
                self.heap[i] , self.heap[i//2] =self.heap[i//2] , self.heap[i]
                
            i = i//2
        print(self.heap)
            
    def deleteNode(self):
        self.heap[0], self.heap[self.n] = self.heap[self.n], -1
        self.n -= 1
        
        i = 1
        nodeTarget = self.heap[0]
        
        while 2 * i - 1 <= self.n:
            
                if nodeTarget < self.heap[2*i-1] and self.heap[2*i -1] > self.heap[2*i]:
                    self.heap[i-1], self.heap[2*i - 1] = self.heap[2*i - 1], self.heap[i-1]
                    i = 2*i
                elif  2 * i <= self.n and nodeTarget < self.heap[2*i] and self.heap[2*i] > self.heap[2*i -1]:
                    self.heap[i-1], self.heap[2*i] = self.heap[2*i], self.heap[i-1]
                    i = 2*i + 1
        print(self.heap)
            
        
        
        
h = Heap()
h.buildTree(10)
h.addNode(5)
h.addNode(3)
h.addNode(4)
h.deleteNode()


            
        
        
        
        
        