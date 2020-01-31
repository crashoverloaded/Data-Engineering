#!/usr/bin/python3

import numpy as np


dataset=[11,10,12,14,15,13,15,102,12,14,107,10,10,13,12,14,108,12,11,12,15,15,11,10,12,14,15,13,15,14,12,13,20,12,25]

sorted(dataset)
''' 
Steps are:-
1. Arrange data in increasing order  
2. Calculate first(q1)(25%) and 3rd q3(75%)
3. Find IQR (q3-q1)
4. Find Lower Bound q1 - (1.5*iqr)
5. Find Upper BOund q3 + (1.5*iqr)

Anything that lies outside of lower or upper bound is an outlier

'''

# Step 2 
q1 ,q3 = np.percentile(dataset,[25,75]) # After Dataset We are Specifying The Values i.e. q1-> 25 % and q3 -> 75%

# step 3 Find IQR

iqr_value = q3 - q1
print("IQR Value:- "+str(iqr_value))

# Step 4 and 5 , Find Lower Bound and Upper Bound
lower_bound_val = q1 - (1.5 * iqr_value)
upper_bound_val = q3 + (1.5 * iqr_value)

print("lower_bound_val:- "+str(lower_bound_val))
print("upper_bound_val:- "+str(upper_bound_val))
