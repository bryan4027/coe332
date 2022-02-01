import numpy as np
allvals  = list(range(3,100))
checkiffirst = 0
checkiffirst2 = 0
for i in range(len(allvals)):
    check = 0
    for j in range(2,allvals[i]):
        
        divided = allvals[i] % j
        
        if ((divided == 0) and (allvals[i] != j)):
            check = 1
            break
    if ((check == 0) and (checkiffirst == 0)):
        arrayprimes = np.array([allvals[i]])
        checkiffirst = 1
        
    if (check == 0 and checkiffirst2 == 1):
        arrayprimes = np.append(arrayprimes, allvals[i])
    if (checkiffirst == 1):
        checkiffirst2 = 1

print('primes: ')
print(*arrayprimes)
        
        
