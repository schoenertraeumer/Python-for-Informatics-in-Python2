def count(s,l):
    count = 0
    for i in s:
        if i == l:
            count += 1
    return count

string = raw_input("Enter a string: ")
letter = raw_input("Enter a letter: ")
c = count(string,letter)
print c
