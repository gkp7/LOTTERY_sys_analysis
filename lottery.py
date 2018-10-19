# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:47:35 2018

@author: Asus
"""

import random
import matplotlib.pyplot as plt
account=0

x=[]
y=[]

for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    #print("lucky draw:" ,lucky_draw)
    #print("bet :",bet)
    
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("amt in game account",account)
plt.plot(x,y)
plt.show()