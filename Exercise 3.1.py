hour = raw_input("Enter Hours : ")
rate = raw_input("Enter Rate : ")
if hour > 40:
    hour = float(hour)
    rate = float(rate)
    pay = ((rate * 1.5) * (hour-40)) + (40*rate)
else:
    pay = rate * hour
print pay
