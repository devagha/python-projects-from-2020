#Lab #7
#Due Date: 04/24/2020, 11:59PM
########################################
#                                      
# Name:devan ghai
# Collaboration Statement:             
#  
########################################

class MaxPriorityQueue:
    '''
        >>> h = MaxPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
        >>> x = MaxPriorityQueue()
        >>> x.insert(2)
        >>> x.insert(7)
        >>> x.deleteMax()
        7
        >>> x.insert(10)
        >>> x.insert(8)
        >>> x.insert(12)
        >>> x.deleteMax()
        12
        >>> x.insert(5)
        >>> x.insert(18)
        >>> x.heap
        [18, 10, 8, 2, 5]
    '''

    def __init__(self):
        self.heap=[]

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        # YOUR CODE STARTS HERE
        return len(self.heap)


    def parent(self,index):
        # YOUR CODE STARTS HERE
        d_=(index-1)//2
        if d_>=0 and d_< len(self.heap):
            return self.heap[d_]
        return None 
    def leftChild(self,index):
        # YOUR CODE STARTS HERE
        lefti=2*index
        if (lefti-1)>0 and (lefti-1)<len(self.heap):
            return self.heap[lefti-1]
        return None
    def rightChild(self,index):
        # YOUR CODE STARTS HERE
        righty=2*index + 1
        if (righty-1)>0 and (righty-1)<len(self.heap):
            return self.heap[righty-1]
        return None
        

    def insert(self,x):
        # YOUR CODE STARTS HERE
        self.heap.append(x)
        d__=len(self.heap)-1
        while((d__!=0) and (self.parent(d__)<self.heap[d__])):
            dx=(d__-1)//2
            self.heap[d__], self.heap[dx] = self.heap[dx], self.heap[d__]
            d__=dx
            

    def deleteMax(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            outMax=self.heap[0]
            self.heap=[]
            return outMax

        # YOUR CODE STARTS HERE
        else:
            outMax = self.heap[0]
            self.heap[0]=self.heap[-1]
            self.heap.pop()
            self.maxHeapishly(0)
            return outMax
        

    def maxHeapishly(self, index):
        lefti=2*index+1
        righty=2*index+2
        indexMax=index
        if(lefti < len(self) and self.heap[lefti] > self.heap[indexMax]):
            indexMax=lefti
        if(righty < len(self) and self.heap[righty] > self.heap[indexMax]):
            indexMax=righty
        if (indexMax!=index):
            self.heap[indexMax], self.heap[index] = self.heap[index], self.heap[indexMax]
            self.maxHeapishly(indexMax)
