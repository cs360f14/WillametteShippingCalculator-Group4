#!/usr/bin/python3
################################
# File Name: 	SaleItemUnitTest.py
# Author: 		Alex Shinsel
# Date: 		11/17/2014
# Class: 		CS 360
# Assignment: 	Lecture Examples
# Purpose: 		Unittest for SaleItem
################################

import unittest
from SaleItem import SaleItem

class TestSaleItem(unittest.TestCase):
	
	def setUp(self):
		self.Item1 = SaleItem(['42', '.5', 'Small Item'])
		self.Item2 = SaleItem(['32', '3', 'Medium Item', 'FS'])
		
	def tearDown(self):
		pass
	
	def test_getCost(self):
		self.assertEqual(self.Item1.getCost(), 42)
		self.assertEqual(self.Item2.getCost(), 32)
		
	def test_getWeight(self):
		self.assertEqual(self.Item1.getWeight(), .5)
		self.assertEqual(self.Item2.getWeight(), 3)
		
	def test_getTitle(self):
		self.assertEqual(self.Item1.getTitle(), 'Small Item')
		self.assertEqual(self.Item2.getTitle(), 'Medium Item')

	def test_getFreeShipping(self):
		self.assertEqual(self.Item1.getFreeShipping(), False)
		self.assertEqual(self.Item2.getFreeShipping(), True)
		
	def test_getDetailsAsString(self):
		self.assertEqual(self.Item1.getDetailsAsString(), 'Small Item $42.00')
		self.assertEqual(self.Item2.getDetailsAsString(), 'Medium Item $32.00')
