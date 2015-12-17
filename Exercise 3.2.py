try:
    hour = float(raw_input("Enter Hours : "))
    rate = float(raw_input("Enter Rate : "))
except:
    print("Error, please enter numeric input")
    exit()
if hour > 40:
    pay = ((rate * 1.5) * (hour-40)) + (40*rate)
else:
    pay = rate * hour
print pay
