# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:45:18 2023

@author: Wiggert
"""
import tableau

# This function takes a tableau and finds the generators which it represents (both destabilizer and stabilizer)
def tableau_to_gen(tab):
    n = tab.getTableauSize()
    tableau = tab.getTableau()
    generators=[]
    for i in range(2*n): #We iterate one row at a time. Each row represents a generator
        r=tableau[i,2*n] #First generator is at the row n (n+1 in matrix indexing)
        if r==1:
            gen="-"
        elif r==0:
            gen="+"
        else:
            print("Error, r is not 0 or 1")
        for j in range(n): 
            x = tableau[i,j] 
            z = tableau[i,n+j]
            if x==0 and z==0:
                gen=gen+"I"
            elif x==0 and z==1:
                gen=gen+"Z"
            elif x==1 and z==0:
                gen=gen+"X"
            elif x==1 and z==1:
                gen=gen+"Y"
        generators += [gen] #Adding the generator to the list of generators
    return generators