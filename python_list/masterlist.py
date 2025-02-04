list1=[]
n=int(input("Enter the number of elements in the list:"))

for i in range(0,n):
    ele=int(input("Enter the element:"))
    list1.append(ele)
print(list1)

list2=[]
num=int(input('Enter a number:'))
for i in range(0,n):
    if(list1[i]<num):
        list2.append(list1[i])
print(list2)