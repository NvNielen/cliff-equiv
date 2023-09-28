# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:25:12 2023

@author: Wiggert
"""
from Hgate import applyHadamard as H
from CNOT import updateCNOT as CN
from phase import Phasegate as S
from verify_gen import verify_gen as vg
from Tableau_to_gen import tableau_to_gen as tg
import tableau

n=2

tab=tableau.Tableau(n)

CN(tab,1,0)
H(tab, 0)
S(tab,0)
print(tab.getTableau())
print(tg(tab))
vg(tg(tab))

