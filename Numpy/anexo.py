import numpy as np
import matplotlib.pyplot as plt
y=np.random.normal(5, 5, size=(1000)) #(media, desviación estándar, dimensión)
b=np.linspace(min(y),max(y))
m=[]
count=0
for x in xrange(0,len(b)-1):
    m.append([])
    for k in y:
        if b[x]<=k and b[x+1]>=k:
            m[count].append(y)
    count+=1
m=[len(x) for x in m]
plt.scatter(range(len(m)),m)
plt.show()
