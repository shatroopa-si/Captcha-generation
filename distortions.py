from random import randrange

from PIL import Image, ImageFilter

import resources

def chooseBackground():
	"""chooses a background randomly for CAPTCHA and returns the image object"""
	
	id = randrange(1, 100001) % (resources.nImages + 1)
	
	#no file exists with the name 0
	if id == 0:
		id = 1
	
	fname = filter(lambda x: x[0] == str(id), resources.backgrounds)[0]		#cz this would return a list of list lyk:[['1', 'dgd']]
	fname = 'backgrounds\\' + fname[0] + '.' + fname[1]										#generating a string
	
	try:
		captchaImage = Image.open(fname)
	except:
		print 'Background file not found, creating a new Image...'
		captchaImage = Image.new('RGB', (500, 100), 'white')
		
	return captchaImage	
	

def chooseDistortion():
	"""chooses any 2 distortions randomly to be applied on the image"""
	
	id1 = randrange(1, 100001) % resources.nDist
	id2 = randrange(1, 100001) % resources.nDist
	
	return resources.setOfDistortions[id1], resources.setOfDistortions[id2]
	

def blur(imageFile):
	"""blurs an image file and returns it."""
	
	imageFile = imageFile.filter(ImageFilter.BLUR)
	return imageFile

def contour(imageFile):
	"""applies contour effect on an image file and returns it"""
	
	imageFile = imageFile.filter(ImageFilter.CONTOUR)
	return imageFile

def emboss(imageFile):
	"""applies emboss effect on an image file & returns it"""
	
	imageFile = imageFile.filter(ImageFilter.EMBOSS)
	return imageFile
	
def smooth(imageFile):
	"""smooths an image file & returns it"""
	
	imageFile = imageFile.filter(ImageFilter.SMOOTH)
	return imageFile
	
def mapDistortion(distortion):
	"""maps a distortion to it's function"""
	
	if distortion == 'blur':
		method = blur
	
	elif distortion == 'contour':
		method = contour
		
	elif distortion == 'emboss':
		method = emboss
		
	elif distortion == 'smooth':
		method = smooth
		
	return method
#blur(Image.open('backgrounds\\1.jpg'))