numbers = []
print("enter 5 number")
for _ in range(5):
    num = input()
    numbers.append(int(num))


gr, sm, total = numbers[0], numbers[0], 0

for i in numbers:
    if i > gr:
        gr = i
    if i < sm:
        sm = i
    total = total + i

avg = total / len(numbers)
print("Output:")
print("Largest:", gr)
print("Smallest:", sm)
print("Sum:", total)
print("Average:", avg)
