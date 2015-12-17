char = raw_input("Enter a string: ")
index = len(char)-1
while index >= 0:
    letter = char[index]
    print letter
    index = index - 1
