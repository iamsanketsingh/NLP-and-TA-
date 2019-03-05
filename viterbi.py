# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hidden_no=int(input("enter the total number of hidden state:- "))
trans_metrix=[]
for i in range(int(hidden_no)):
    row=[]
    for j in range(int(hidden_no)):
        n=eval(input("Transactional Probability:- "))
        row.append(n)
    trans_metrix.append(row)


visible_no=int(input("enter the total number of visible state:- "))
emmision_metrix=[]
for i in range(int(hidden_no)):
    b1=[]
    for j in range(int(visible_no)):
        n=eval(input("Emission Probability:- "))
        b1.append(n)
    emmision_metrix.append(b1)

max_trans_row=[]
for i in range(int(hidden_no)):
    mx=0
    for j in range(hidden_no):
        mx =  max(trans_metrix[j][i],mx)
    max_trans_row.append(mx)

emmision_metrix_max = []    
for i in range(int(hidden_no)):
    multiple = max_trans_row[i]
    row = []
    for j in range(int(visible_no)):
        row.append(multiple*emmision_metrix[i][j])
    emmision_metrix_max.append(row)
    
max_final=[]
for i in range(visible_no):
    mx=0
    for j in range(hidden_no):
        mx = max(emmision_metrix_max[j][i],mx)
    max_final.append(mx)
    
print("The max probability is",max_final)

    

