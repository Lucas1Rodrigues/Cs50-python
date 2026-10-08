def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1,2,3))
print(my_function(2,3,4,5,2,9))

def maximum(*numbers):
    if len(numbers) == 0:
        return None
    maxNum  = numbers[0]
    for num in numbers:
        if num > maxNum:
            maxNum = num
        return maxNum

print("O maior numero é ",maximum(2,3,4,5,6,7,8,89,3))
