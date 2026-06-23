print("Enter numbers continuously.")
inpt = ""
numbers = []
while True:
    inpt = input()
    if inpt == "done":
        break
    numbers.append(int(inpt))

if len(numbers) == 0:
    print("No numbers entered")

else:
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
