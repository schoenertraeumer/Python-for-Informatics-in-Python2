def chop(t):
    del t[0]
    del t[-1]
    return None
def middle(t):
    t=t[1:-1]
    return t

lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]


chop(lst1)
print lst1
newlst = middle(lst2)
print newlst
