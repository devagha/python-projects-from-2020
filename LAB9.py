#LAB 9
#Due Date: 04/11/2020, 11:59PM EST
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class MaxPriorityQueue:
    ### Copy and paste your code from LAB 7 here
    def __init__(self):
        self.heap=[]

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        # return priority Qs # of elements
        return len(self.heap)


    def parent(self,index):
        # return parent
        d_=(index-1)//2 #=index of parent
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
            self.heap[0]=self.heap[-1] #swap first and last element
            self.heap.pop()
            self.maxHeapishly(0)
            return outMax
        

    def maxHeapishly(self, index):
        lefti=2*index+1 #left index
        righty=2*index+2#right index
        indexMax=index
        if(lefti < len(self) and self.heap[lefti] > self.heap[indexMax]):
            indexMax=lefti
        if(righty < len(self) and self.heap[righty] > self.heap[indexMax]):
            indexMax=righty
        if (indexMax!=index):
            self.heap[indexMax], self.heap[index] = self.heap[index], self.heap[indexMax]
            self.maxHeapishly(indexMax)




def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sortHeap = MaxPriorityQueue()
    # -- YOUR CODE STARTS HERE
    for i in range (1, len(numList)):
        pos=i
        while pos>0 and numList[pos]<numList[pos-1]:
            numList[pos-1], numList[pos]=numList[pos], numList[pos-1]
            pos-=1
    return numList
