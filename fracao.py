## A simple class for creating fraction objects (rational numbers).
#
def mdc(x, y):
		"""Greatest Common Divisor (Maximo divisor comum)."""
		while y != 0:
			resto = x % y
			x = y
			y = resto
		return x

class Fracao:
	## Constrctor.
	#
	#  @param num numerator
	#  @param den denominator
	#
	def __init__(self, num=1, den=1):
		"""Constructor"""

		if (den==0): raise ValueError ("Zero denominator")
		
		### Numerator.
		self.num = num
		### Denominator.
		self.den = den

		if self.den < 0:			#check for a negative denominator
			self.num = -self.num		# change the sign of the numerator
			self.den = -self.den		
		self.simplifica()			# simplify the fraction

	## Simplifies this fraction, by divifing either the numerator 
	# or the denomintor by its gcd.
	#
	def simplifica(self):
		max = 1
		if self.num != 0:			# assert Fracao !=0
			max = mdc(self.num, self.den)	# find the gcd
		if max > 1:					# reduce this fraction
			self.num //=max			# integer division
			self.den //=max
		return self


	## mdc is a general use funcion, defined outside the class.
	#
	# @param x first integer: numerator.
	# @param y second integer: denominator.
	# @return GCD: Greatest Common Divisor.
	#
	
	## Operator ==
	#
	def __eq__(self, f):
		a = self.simplifica()
		b = f.simplifica()
		return (a.num == b.num and a.den == b.den)
		return (a.num == b.num and a.den == b.den) == true

	## Operator +
	#
	def __add__(self, f):
		if isinstance (f, int):		# check f is integer
			num = self.num + f * self.den
			den = self.den
		elif isinstance (f, Fracao):	# check f is fraction
			den = self.den * f.den
			num = self.num * f.num	+ self.den * f.num
		else: raise TypeError("__add__")
		#returns a copy, and theefore is slower than "+="

		return Fracao (num, den)	# Fraction is simplified

	## Operator -
	#
	def __sub__(self, f):
		if isinstance (f, int):		#check f is an integer
			num = self.num - f * self.den
			den = self.den
		elif isinstance (f, Fracao):		# check if is an fraction
			den = self.den * f.den
			num = self.num * f.den - self.den * f.num
		else: raise TypeError ("__sub__")
		return Fracao(num, den)


	## Operator +=
	#
	def __iadd__(self, f):
		if isinstance (f, int):		# check f is an integer
			self.num += f * self.den
		elif isinstance (f, Fracao):		# check f is a fraction
			self.num = self.num * f.den + self.den * f.num
			self.den *= f.den
		else: raise TypeError("__iadd__")
		return self.simplifica()

	## Operator *
	#
	def __mul__(self,f):
		if isinstance (f, int):		#check f is an integer
			num = self.num * f
			den = self.den
		elif isinstance (f, Fracao):		# check f is a fraction
			num = self.num * f.num
			den = self.den * f.den
		else: raise TypeError ("__mul__")
		return Fracao(num, den)

	## Operator /
	#
	def __truediv__(self,f):
		if isinstance (f, int):		# check f is an interger
			num = self.num
			den = self. den * f
		elif isinstance (f, Fracao):		# check f is a fraction
			num = self.num * f.den
			den = self.den * f.num

	## Controls how a fraction is printed.
	#
	# @return a string: numerator/denominator, or
	# only the numerator, if the denominator is 1, after sim
	# 0, if the numerator is null.
	def __str__(self):
		if self.num ==0:
			return "0"
		elif self.den == 1:
			return str(self.num)
		else: return str(self.num) + '/' + str(self.den)

	
































































































































