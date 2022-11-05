class stack:
    def __init__(self,size1):
        self.items=[]
        self.size=size1
        self.top=-1
    def push(self,item):
        if(self.size -self.top>1):
            self.top=self.top+1
            self.items.append(item)
            
        else:
            print("OverFlow \n")
    def pop(self):
        if(self.top>=0):
            self.items.pop()
            self.top=self.top-1
        else:
            print("underFlow")
    def display(self):
        print(self.items)
    def peek(self):
        if(self.top>=0):
            topValue=self.items[self.top]
            print(topValue)
        else:
            print("stack is empty")

stack =stack(6)

stack.push(5)
stack.push(10)
stack.push(15)
stack.pop()
stack.push(20)
stack.display()
stack.peek()
stack.push(25)
stack.pop()
stack.push(30)
stack.push(35)
stack.display()



