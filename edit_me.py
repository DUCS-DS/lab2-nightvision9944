#Jude Brooks
#Lab 2, Data Structures
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    len_lst = len(lst)
    intA = lst[0]
    intB = lst[1]
    intC = lst[2]
    if intA - intB >= 0 and intA != intC:
        return True
    else:
        return False


lstA = [1, 1, 3, 100] #This is ascending, monotonic
lstB = [11, 1, -9, -10] #This is descending, monotonic
lstC = [2, 3, 2, 3] #This is neither, non-monotonic

print(monotonic(lstA))
print(monotonic(lstB))
print(monotonic(lstC))