start = int(input("Start cycle number: "))
end = int(input("End cycle number: "))

for start in range(start, end, 1):
    if start % 7 == 0: print(start)