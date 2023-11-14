list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
list2=[]
count = 0
x = len(list1)
for index in range(0,x-1):
    if 80<=list1[index]<=100:
        count+=1
print("num of integers range 80-100",count)

for index in range(0,x-1):
    if 80<=list1[index]<=100:
        item = list1[index]
        list2.append(item)
        x = len(list1)
print(list2)
