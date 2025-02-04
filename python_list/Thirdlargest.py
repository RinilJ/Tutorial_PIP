list1=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    list1.append(ele)
print(list1)
list1.sort()
print(list1[-3])