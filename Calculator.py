

operation = input("Enter the your operation: ") # For example "21+21*2/4"
operatorList = ["+", "-", "*", "/"]


def getSymbolsListInOrder(string, symbols):
    symbolsList = []
    for i in range(len(string)):
        for j in range(len(symbols)):
            if string[i] == symbols[j]:
                symbolsList.append(string[i]);

    return symbolsList


def isHaveOperatorInString(string, operator):
    if operator in string: return True
    
    return False


def deleteSymbolFromString(string, symbol):
    return string.replace(symbol, " ")


def deleteOperatorSymbolsFromString(string, operator):
    stringBuff = string

    for i in range(len(operatorList)):
        if isHaveOperatorInString(string, operatorList[i]):
            stringBuff = deleteSymbolFromString(stringBuff, operatorList[i])
    

    return stringBuff


def transformTypeToInt(stringOfValue):
    transformedTypesList = []

    for number in stringOfValue.split():
        transformedTypesList.append(int(number))


    return transformedTypesList


def calculateByList2D(valueList, operatorList):
    counter = valueList[0]
    for i in range(1, len(valueList)):
        if operatorList[i-1] == "+":
            counter += valueList[i]
        if operatorList[i-1] == "-":
            counter -= valueList[i]
        if operatorList[i-1] == "*":
            counter *= valueList[i]
        if operatorList[i-1] == "/":
            counter /= valueList[i]

    return counter


print(getSymbolsListInOrder(operation, operatorList)); # Getting operator symbol list in order.
print(transformTypeToInt(deleteOperatorSymbolsFromString(operation, operatorList))) # Transform string values to int values. 

print(f"Result: {calculateByList2D(transformTypeToInt(deleteOperatorSymbolsFromString(operation, operatorList)), getSymbolsListInOrder(operation, operatorList))}") # Calculate by data on up.



