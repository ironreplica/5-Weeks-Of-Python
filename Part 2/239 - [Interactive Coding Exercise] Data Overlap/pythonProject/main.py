f = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')

file1Numbers = [int(num) for num in f.readlines()]
file2Numbers = [int(num) for num in f2.readlines()]

result = [num for num in file1Numbers if num in file2Numbers]
# Write your code above 👆
print(result)
