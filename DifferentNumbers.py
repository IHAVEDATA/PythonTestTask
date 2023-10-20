count = 0

for num in range(100, 10000):
    digits = set(str(num))
    if len(digits) == 4:
        count += 1

print("Numbers with unique symbols:", count)