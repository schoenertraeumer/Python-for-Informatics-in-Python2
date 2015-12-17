try:
    n = float(raw_input("Enter Score: "))
    if n<0.0 or n>1.0:
        print 'Bad score'
    elif n  >= 0.9:
        print 'A'
    elif n>=0.8:
        print 'B'
    elif n>=0.7:
        print 'C'
    elif n>=0.6:
        print 'D'
    elif n<0.6:
        print 'F'
except:
    print 'Bad score'
