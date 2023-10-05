# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:56:28 2023

@author: Chelsea Apawti
"""


import unittest
import mgate
import tableau
import verify_gen_mgate as vg
import tableau_to_gen as tg

class testMeasurementGate(unittest.TestCase):

    def setUp(self):
        self.tab = tableau.Tableau(2)
        self.qubit = 0
        
        # Use verification
        self.check = vg.verify_gen_mgate(tg.tableau_to_gen(self.tab),self.qubit)
        print(" ")
        print("Verification gives:")
        print(self.check)
        
        # Test tableau algorithm
        print("Algorithm gives:")
        self.test=mgate.updateMeasurement(self.tab,1)
        self.result = tg.tableau_to_gen(self.test)
        self.result = self.result[self.qubit]
        print(self.result)
        print(" ")
        print(self.test.tableau)
        
        
    def test_measurement(self):
        self.assertEqual(self.result, self.check, "Measurement gate tested incorrectly")
        

if __name__ == '__main__':
    unittest.main()