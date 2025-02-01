#Jude Brooks
#Lab 2, Data Structures
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    list1 = []
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            list1.append(True)
        else:
            list1.append(False)
    for j in list1:
        if j == False:
            return 'This list is not monotonic'
        else:
            return 'This list is monotonic, ascending'
    #for k in range(len(lst)-1):
    #    if lst[k] >= lst[k+1]: #List B works with this one :)
    #        print('h')
    #    else:
    #        print('i')
    #for l in range(len(lst)-1):
    #    if lst[l] == lst[l+1]:
    #        print('h')
    #    else:
    #        print('i')


lstA = [1, 1, 3, 100] #This is ascending, monotonic
lstB = [11, 1, -9, -10] #This is descending, monotonic
lstC = [2, 3, 2, 3] #This is neither, non-monotonic

x = monotonic(lstA)
print(x)

