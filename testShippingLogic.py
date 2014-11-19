#!/usr/bin/python3
#############################################################
# File Name:	testTTTPlayer.py
# Author:	   	Ben Seaton
# Date:		 	10/29/14
# Class:		CS360
# Assignment:   Python Tic Tac Toe
# Purpose:	  	unit test for TTTcomputerPlayer module
#############################################################
import unittest
from ShippingLogic import *

class testShippingLogic(unittest.TestCase):
	
	def setUp(self):
		self._shippingLogic = ShippingLogic()
		
	def test_getName(self):
		testName = self._shippingLogic.getName()
		self.assertTrue(testName == 'Standard')

