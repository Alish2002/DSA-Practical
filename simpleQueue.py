class queue():
    def __init__(self, size1):
        self.items=[]
        self.size=size1
        self.front=-1
        self.rear=-1
    def insert(self,item):
        if(self.front==-1):
            self.front=0
            self.rear=0
        elif(self.rear==self.size-1):
            print("Overflow")
        else:
            self.rear=self.rear+1
        self.items.append(item)
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        else:
            i=self.front
            while(i<=self.rear):
                print(self.items[i],end=" ")
                i=i+1
            print()
    def delete(self):
        if(self.front==-1):
            print("Underflow")
        elif(self.front==0 and self.rear==0):
            self.front=self.rear=-1
        else:
            self.front=self.front+1
    
       

queue =queue(5)
queue.insert(2)
queue.insert(5)
queue.insert(6)
queue.display()
queue.delete()
queue.display()
queue.insert(3)
queue.display()