# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:45:18 2023

@author: Wiggert
"""
import tableau

def tableau_to_gen(tab):
    n = tab.getTableauSize()
    tableau = tab.getTableau()
    generators=[]
    for i in range(n):
        r=tableau[n+i,2*n]
        
        if r==1:
            gen="-"
        elif r==0:
            gen="+"
        else:
            print("Error, r is not 0 or 1")
        for j in range(n):
            x = tableau[n+i,j]
            z = tableau[n+i,n+j]
            if x==0 and z==0:
                gen=gen+"I"
            elif x==0 and z==1:
                gen=gen+"Z"
            elif x==1 and z==0:
                gen=gen+"X"
            elif x==1 and z==1:
                gen=gen+"Y"
        generators+=[gen]
    return generators
    
#tab=tableau.Tableau(2)
#generators=tableau_to_gen(tab)