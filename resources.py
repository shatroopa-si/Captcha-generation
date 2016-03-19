import os

#generate string from these characters
alphabet = {'lchars': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
'uchars': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
'digits': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
'schars': ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/', '|', '\\', '~', '`']
}

#choose backgrounds from here
backgrounds = [x for x in os.walk(os.getcwd() + '\\backgrounds' )][0][2]	

nImages = len(backgrounds)


#store every file name as a list: [name, extension]
for fname in backgrounds:
	if type(fname) is str:
		backgrounds.append(fname.split('.'))

#splice out the file names in string format
backgrounds = backgrounds[nImages:]


#choose distortions from here
setOfDistortions = {0: 'blur',
1: 'contour',
2: 'emboss',
3: 'smooth'
}

nDist = len(setOfDistortions)


#location of font files
fontLoc = 'C:\Windows\Fonts\\'


#choose from these fonts
fonts = {0: 'ITCBLKAD',		#Blackadder ITC
1: 'BRUSHSCI',				#Brush Script MT
2: 'CHILLER',				#Chiller
3: 'CURLZ___',				#Curlz MT
4: 'ITCEDSCR',				#Edwardian Script ITC
5: 'FREESCPT',				#Freestyle Script
6: 'FRSCRIPT',				#French Script MT
7: 'GIGI',					#Gigi
8: 'JOKERMAN',				#Jokerman
9: 'KUNSTLER',				#Kunstler Script
10: 'MATURASC',				#Matura MT Script Capitals
11: 'MISTRAL',				#Mistral
12: 'OLDENGL',				#Old English Text MT
13: 'PALSCRI',				#Palace Script MT
14: 'PARCHM',				#Parchment
15: 'PRISTINA',				#Pristina
16: 'RAGE',					#Rage Italic
17: 'VIVALDII',				#Vivaldi
18: 'VLADIMIR'				#Vladimir Script
}

nFonts = len(fonts)