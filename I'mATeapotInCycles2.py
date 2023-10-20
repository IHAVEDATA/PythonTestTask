
# Variables, lists

cycleState = True
arr = []


# Functions

def CountNumberSumOfArray(array):
    arraySum = 0
    for i in range(0, len(array), 1):
        arraySum += array[i]

    return arraySum

def GetMaxNumberOfArray(array):
    lastMaxNumber = 0
    for i in range(0, len(array), 1):
        if lastMaxNumber < array[i]:
            lastMaxNumber = array[i]

    return lastMaxNumber

def GetMinNumberOfArray(array):
    lastMinNumber = array[0];
    for i in range(0, len(array), 1):
        if array[i] < lastMinNumber:
            lastMinNumber = array[i]

    return lastMinNumber


# The main cycle

while cycleState:
     newNumber = int(input("Enter a new number: "))
     if newNumber == 7: cycleState = False # Bug
     arr.append(newNumber)

     print(f"Sum array numbers: {CountNumberSumOfArray(arr)}, Max member of array: {GetMaxNumberOfArray(arr)}, Min member of array: {GetMinNumberOfArray(arr)}")

print("Goodbye!")