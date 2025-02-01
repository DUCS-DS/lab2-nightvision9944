#Jude Brooks
#Lab 2, Data Structures
import time

def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    counter = 1
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            counter += 1
    if counter == 1:
        for j in range(len(lst)-1):
            if lst[i] >= lst[i+1]:
                counter += 1
    if counter == len(lst):
        return True
    else:
        return False



lstA = [1, 1, 3, 100] #This is ascending, monotonic
lstB = [11, 1, -9, -10] #This is descending, monotonic
lstC = [2, 3, 2, 3] #This is neither, non-monotonic
start = time.time()
x = monotonic(lstA)
end = time.time()
print(x, end-start)

