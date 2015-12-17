def computegrade(n):

    if n<0.0 or n>1.0:
        p= 'Bad score'
    elif n  >= 0.9:
        p= 'A'
    elif n>=0.8:
        p= 'B'
    elif n>=0.7:
        p= 'C'
    elif n>=0.6:
        p= 'D'
    elif n<0.6:
        p= 'F'

    return p

try:

        num = float(raw_input("Enter score: "))
        p=computegrade(num)
        print p
except:

        print 'Bad score'




