def computepay(h,r):
    if h<=40:
        p=r*h
    else:
        p = r*40 + (r* 1.5 * (h-40))
    return p
try:
    hours = float(raw_input("Enter Hours: "))
    rate = float(raw_input("Enter Rate: "))
except:
    print "Error, please enter numeric input"
    quit()
pay = computepay(rate, hours)
print 'Pay:', pay
