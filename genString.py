from random import randrange

import resources

def setLength():
	"""decides length for the CAPTCHA string randomly"""
	minLength = 6
	maxLength = 10
	length = randrange(minLength, maxLength + 1)
	return length


def setAlphabet():
	"""Assigns the alphabet from which the upcoming character is to be taken"""
	sa = randrange(100, 10000)	#sa => set alphabet
	sa %= 4 					#now 0<= sa <= 3
	#mapper
	if sa == 0:
		sa = 'lchars'
	elif sa == 1:
		sa = 'uchars'
	elif sa == 2:
		sa = 'digits'
	else:
		sa = 'schars'
		
	return sa


def setChar(chosenSet):
	"""returns a character randomly from the chosen set."""
	
	if chosenSet == 'digits':
		limit = 10
	else:
		limit = 26
	
	#randomly choosing a character
	indexChar = randrange(0, limit)
	return str(resources.alphabet[chosenSet][indexChar])
	

def stringGenerator():
	"""generates a random string for the CAPTCHA"""
	
	captchaString = ''

	length = setLength()
	
	for i in range(length):
		chSet = setAlphabet() 		#chose a set from which character is to de derived.
		captchaString += setChar(chSet)
	
	return captchaString
	
