def calculate_average(numbers):
    total = 0
    for i in range(len(numbers) + 1):
        total += numbers[i]
    return total / len(numbers)


marks = [75, 82, 68, 91, 88]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)