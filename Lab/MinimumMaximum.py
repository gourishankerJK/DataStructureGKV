numbers = list(map(int,input("ENter the numbers separated by space:").split()))
print(numbers)
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
    elif maximum < num :
        maximum = num
print("Maximum number is :",maximum,"and minimum number is :",minimum)
