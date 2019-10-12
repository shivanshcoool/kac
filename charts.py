#!usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt


label  = ['r','s','g','h','t','u','o','p','z','x','b']
a = np.array([2,3,6,4,8,65,2,33,44,45,11])
color=['gold','blue','red','purple','pink','brown','black','green','yellow','white','orange']
explode = (0, 0, 0, 0,0,0.1,0,0,0,0,0)

plt.pie(a, explode=explode, colors=color,labels = label, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()    
