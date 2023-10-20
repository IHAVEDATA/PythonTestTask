
firstNum = int(input("Write first number: "))
secondNum = int(input("Write second number: "))
thirdNum = int(input("Write third number: "))

isMultiply = bool(input("Is multiply (if didn't multiplying the numbers press 'enter')"))

if isMultiply: print(firstNum * secondNum * thirdNum)
else: print(firstNum + secondNum + thirdNum)