# Insertion
arr=[1,2,3,4,5]
def insert(arr,k,item):
    arr.append(0)
    n=len(arr)
    i=n-2
    while(i>=k):
        arr[i+1]=arr[i]
        i=i-1
    arr[k]=item
      
insert(arr,2,6)
print(arr)

# Deletion
arr1=[1,2,3,4,5,6]
def delete(arr1,k):
    n=len(arr1)
    i=k
    while(i<=n-2):
        arr1[i]=arr1[i+1]
        i=i+1
    arr1.pop()
    print(arr1)
delete(arr1,2)