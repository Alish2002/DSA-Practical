class cQueue:
    def __init__(self, size1):
        self.items=[0]*size1    
        self.size=size1
        self.front=-1
        self.rear=-1   
    def insert(self,item):
        if(self.front==-1):
            self.front=0
            self.rear=0
        elif((self.rear==self.size-1 and self.front==0) or( self.front==self.rear+1)):
            print("Overflow")
            return
        elif(self.rear==self.size-1):
            self.rear=0
        else:
            self.rear=self.rear+1
        self.items[self.rear]=item 
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        else:
            print("Elements in Queue are: ")
            if(self.rear>=self.front):
                i=self.front
                while(i<=self.rear):
                    print(self.items[i],end=" ")
                    i=i+1
                print()
            else:
                i=self.front
                while(i<self.size):
                    print(self.items[i],end=" ")
                    i=i+1
                j=0
                while(j<=self.rear):
                    print(self.items[j],end=" ")
                    j=j+1
                print()
    def delete(self):
        if(self.front==-1):
            print("UnderFlow")
            return
        if(self.front==self.rear):
            self.front=-1
            self.rear=-1
        elif(self.front==self.size-1):
            self.front=0
        else:
            self.front=self.front+1

cQueue=cQueue(5)
cQueue.insert(2)
cQueue.insert(4)
cQueue.insert(6)
cQueue.insert(8)
cQueue.insert(10)
cQueue.display()
cQueue.insert(9)
cQueue.insert(5)
cQueue.delete()
cQueue.display()
cQueue.insert(3)
cQueue.display()  


                     