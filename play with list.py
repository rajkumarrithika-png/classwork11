list = [1,2,3,4,5,6,7,8,9,10]
sum = 0 
for i in list:
    sum = sum + i 
print("Sum of the list is:",sum)
avg = sum/len(list)
print("Average of the list is:", avg)
min_value = min(list)
max_value = max(list)
print("Minimum value in the list is:", min_value)
print("Maximum value in the list is:", max_value)