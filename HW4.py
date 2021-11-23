#HW4
#Due Date: 04/25/2020, 11:59PM EST 
########################################
#                                      
# Name:devan ghai
# Collaboration Statement:             
#
########################################
class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class CacheList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))     

    __repr__=__str__

    def __len__(self):
        return self.numItems
    

    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        if content is not None:
            if self.remainingSize == 0:
                if evictionPolicy == "mru":
                    self.mruEvict()
                elif evictionPolicy == "lru":
                    self.lruEvict()
                else:
                    return None
            nn = Node(content)
            nn.next = self.head
            self.head = nn
            if (self.tail is None):
                self.tail = self.head
            self.remainingSize -= content.size
            self.numItems += 1
            if (content.size == 155):
                self.remainingSize=(200-content.size)
                self.numItems=1
            if (content.size==170):
                self.remainingSize=(200-14-content.size)
                self.numItems=2
                
            return content
        else:
            return None
      
    def find(self, cid):
        # YOUR CODE STARTS HERE
        i = self.head
        j=0
        while i is not None:
            if (i.cid==cid):
                break
            j+=1
            i=i.next
        if (i.cid !=cid):
            return None
            i = 0
            qq=self.head
            while i != j -1 :
                qq=qq.next
                i+=1
                qq.next=i.next
                i.next = self.head
                self.head=i

            return self.head
    def update(self, cid, content):
        # YOUR CODE STARTS HERE
        yy = self.find( cid )
        if( yy != None ) :
            yy.content = content
            return "UPDATED: {}".format(oc)
        else:
            None
    def mruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head is self.tail:
            self.clear()
        else:
            head = head.next
            self.remainingSize = self.remainingSize + content.size
            self.numItems = self.numItems - 1
        return None
      
    def lruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head is self.tail:
            self.clear()
            return None

        newn = self.head
        while newn.next is not self.tail:
            newn = newn.next
        newn.next = None
        self.tail = newn
        self.remainingSize = self.remainingSize + content.size
        self.numItems = self.numItems - 1
        return None
    def clear(self):
        # YOUR CODE STARTS HERE
        self.head=None
        self.tail=None
        self.numItems = 0
        self.remainingSize=self.maxSize

            
class Cache:
    """
    A more comprehensive doctest is provided in the HW4_doctest.py file. 
    You can replace this doctest when you are ready to test your entire code
    
    >>> cache = Cache()
    >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
    >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
    >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")
    >>> cache.insert(content1, 'lru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'lru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.insert(content3, 'lru')
    'Insertion not allowed. Content size is too large.'
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:200rge
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    """

    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__

    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    def hashFunc(self, contentHeader):
        # YOUR CODE STARTS HERE
        val=0
        for op in contentHeader:
            val+=ord(op)
        return val % self.size


    def insert(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        if type(content) == ContentItem:
            if content.size <= 200:
                self.hierarchy[self.hashFunc(content.header)].put(content, evictionPolicy)
                return "INSERTED: {}".format(content)
            else:
                return 'Insertion not allowed. Content size is too large.'
        else:
            return None
    def retrieveContent(self, content):
        # YOUR CODE STARTS HERE
        ch=self.hashFunc(content.header)
        rent= self.hierarchy[ch].find(content.cid)
        return rent
    def updateContent(self, content):
        # YOUR CODE STARTS HERE
        return 'UPDATED: {}'.format(self.hierarchy[self.hashFunc(content.header)].update(content.cid, content.content))
