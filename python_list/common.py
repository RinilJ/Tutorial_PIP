list1=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    list1.append(ele)
print(list1,"\n")
list2=[]
n=int(input("Enter the number of elements in the seccond list:"))

for i in range(0,n):
    ele=int(input("Enter the element:"))
    list2.append(ele)
print(list2,"\n")
common = list(filter(lambda x: x in list2, list1))
print("The common list is ",common)

