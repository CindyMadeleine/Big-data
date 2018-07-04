#bBar 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# set a seed for replicability
np.random.seed(19680801)

min = 150
max = 340

tree_sizes = np.array(np.random.randint(min, max, size=10))
print( tree_sizes)

intervalls = [x for x in range(0, max, 50)]
counter = np.zeros(len(intervalls))
print (intervalls, counter)

print(intervalls, counter)

for i in range(0, len(tree_sizes)):
    for j in range(0, len(intervalls)):
        if(intervalls[j] > tree_sizes[i]):
            counter[j] += 1
            break
    
print(intervalls, counter)

#plot data
plt.bar(intervalls, counter, align='center')
plt.ylabel('amount of trees')
plt.xlabel('height of trees')
plt.show()
    
        
#Histogram:

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# set a seed for replicability
np.random.seed(19680801)

min = 0
max = 340

tree_sizes = np.array(np.random.randint(min, max, size=10))
print( tree_sizes)

bars = [x for x in range(0, max, 50)]

plt.title('amount vs. height')
plt.hist(tree_sizes, bars, histtype='bar', rwidth=0.8)
plt.ylabel('amount of trees')
plt.xlabel('height of trees')
plt.show()
