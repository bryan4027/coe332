import numpy as np
allvals  = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
firsteven = 0
firstodd = 0
for i in range(len(allvals)):
    if (allvals[i] % 2 == 0):
        if (firsteven == 0):
            arrayevens = np.array([allvals[i]])
            firsteven = 1
        else:
            arrayevens = np.append(arrayevens, allvals[i])

    else:
        if (firstodd == 0):
            arrayodds = np.array([allvals[i]])
            firstodd = 1
        else:
            arrayodds = np.append(arrayodds, allvals[i])
print('evens: ')
print(*arrayevens)

print('odds: ')
print(*arrayodds)
        
        
