#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:32:57 2018

@author: sntr
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:30:47 2018

@author: sntr
Köşegen matrisi oluşturma
"""

n=10
x=list()
for i in range(n):
    y=list()
    for j in range(n):
        y.append(1) if (i+j)==n-1 or (i==j) else y.append(0)  # if-else satır içi kullanımı
    x.append(y)
    
for i in x:
    print i