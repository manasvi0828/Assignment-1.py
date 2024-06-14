list= [1,2,3,4,5]
min=1
max=0

for i in range(0,len(list)):
    if list[i]>max:
        max= list[i]

    if list[i]<min:
        min= list[i]

print("minimum element is: ", min)
print("maximum element is: ", max)

