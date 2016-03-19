import turtle

from random import random
from random import randrange
from PIL import Image, ImageFont, ImageDraw

import resources
import genString
import distortions
	
def writeString(imageFile, cString):
	"""writes the string onto the image file"""
	
	rx = 10
	ry = 10
		
	#write each character separately
	for ch in cString:
		write = ImageDraw.Draw(imageFile)
	
		#choose font-family randomly
		rIndex = randrange(1, 10000001) % resources.nFonts
		size = 60
		fontFile = resources.fontLoc + resources.fonts[rIndex] + '.ttf'
		font = ImageFont.truetype(fontFile, size)
	
		#choose where to write and in what color randomly but choose dark colors
		rr = randrange(1, 10000001) % 57
		rg = randrange(1, 10000001) % 57
		rb = randrange(1, 10000001) % 57
		
		write.text((rx, ry), ch, (rr, rg, rb), font = font)
		
		#change positions for next character
		rx = rx + 30
		ry = randrange(1, 10000001) % 41
	
	return imageFile
	
def captcha():
	"""generates a CAPTCHA image and displays it"""
	
	#generate an empty image
	imageFile = distortions.chooseBackground()
	
	#distort background
	
	#select distortions
	dist1, dist2 = distortions.chooseDistortion()
	
	#apply distortions onto the image randomly (2 distortions on 1 image)
	i = randrange(1, 10000001) % 2
	if i == 0:
		imageFile = distortions.mapDistortion(dist1)(imageFile)
		imageFile = distortions.mapDistortion(dist2)(imageFile)
	else:
		imageFile = distortions.mapDistortion(dist2)(imageFile)
		imageFile = distortions.mapDistortion(dist1)(imageFile)
		
	#generate a string
	cString = genString.stringGenerator()
	
	#write string to the image
	imageFile = writeString(imageFile, cString)
	
	#view CAPTCHA
	imageFile.show()
	
	#CAPTCHA check
	usrInput = raw_input('What did you see? ')
	if usrInput == cString:
		print 'Welcome aboard'
	else:
		print 'Access denied! that\'s a robot'
		print cString
	
captcha()
	
	
