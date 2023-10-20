
someText = input("Enter the some text: ")

def CountWords(text):
    count = 1 # By default the "text" will have one word or more

    for i in range(0, len(text), 1):
        if text[i] == " ":
            count += 1

    return count


print(f"Number words at some text: {CountWords(someText)}")