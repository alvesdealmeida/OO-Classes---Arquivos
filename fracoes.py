#!/usr/bin/env python
# coding: UTF-8
#
## @package _01e_fracoes
#
# Reads a file with a series of fractions, and prints their sum
# and products.
#
# @autor: sebastiao
# @since 27/09/2021

import sys
from fracao import Fracao


# Process fractions on a given file.
class Fracoes:
	##
	# Constructor.
	# Opens filename and calls Reader for inputting the fraction readings.
	# Raises an exception if filename does not exist.
	#
	# @param filename fraction file name.
	#
	def __init__(self, filename):
		### lfracoes - a list of objects of type Fracao.

		self.lfracoes = []

		try:
			f = open(filename, "r")
		except IOError:
			print("Fracoes: Cannot open file %s for reading" %filename)
			raise
		self.Reader(f)

	##
	# Reads a file with a numerator and denominator per line.
	# Creates a Fracao object for each line and inserts it in lfracoes.
	#
	# @param f fraction file object.
	#

	def Reader(self, f):
		for line in f:
			temp = line.split(None)
			if len(temp) == 2:
				try:
					self.lfracoes.append(Fracao(int(temp[0]), int(temp[1])))
				except:
					print("Fracao Invalida: %s\n" % temp)
					continue
		f.close()

	##
	# Returns the sum and product of all entries of "lfracoes".
	#
	# @return a string: sum and product of all fractions.
	#

	def __str__(self):
		sb = ""
		f = Fracao(0,1)
		g = Fracao(1,1)

		for i in range(0, len(self.lfracoes)):
			f += self.lfracoes[i]
			g *= self.lfracoes[i]
		sb += "Soma: %s\nProduto: %s\n" % (f,g)
		return sb

	##
	# Returns each fraction in list "lfracoes".
	#
	# @return a string: a seires of fractions, one per line
	#
	
	def __repr__(self):
		sb = ""
		for i in range(0, len(self.lfracoes)):
			sb += "Fracao %d: %s\n" % (i, self.lfracoes[i])
		return sb

	# Reads a series of pairs and prints the sum and product of all fractions.
	#
	