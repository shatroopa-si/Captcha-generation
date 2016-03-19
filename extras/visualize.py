import turtle
import kMeansClustering

def readQuakeFile(fileName):
	""" reads a files and returns a dictionary with line numbers as keys and line as values """

	dataFile = open(fileName)
	dataDict = {}

	key = 0
	line = dataFile.readline()
	while line != '':
		key += 1
		score = list(float(x) for x in line.strip().split(' '))
		dataDict[key] = score

		line = dataFile.readline()
	
	return dataDict


def visualizeQuakes(dataFile):
	"""visualizes earthquakes onto a map"""
	
	dataDict = readQuakeFile(dataFile)
	quakeCentroids = kMeansClustering.initCentroids(6, dataDict)
	clusters = kMeansClustering.createClusters(6, quakeCentroids, dataDict, 7)
	
	#initialize turtle and window
	quakeT = turtle.Turtle()
	quakeWin = turtle.Screen()
	quakeWin.bgpic('worldmap.gif')		#set background image
	#quakeWin.screensize(456, 325)		#same as image size
	turtle.setup(456, 325)		        #same as image size
	
	#set scaling factors
	wFactor = (quakeWin.screensize()[0] / 2.0) / 180.0
	hFactor = (quakeWin.screensize()[1] / 2.0) / 90.0

	#make the turtle ready for plotting
	quakeT.hideturtle()
	quakeT.up()

	#initialize colors
	colorList = ['red', 'pink', 'blue', 'magenta', 'cyan', 'brown']

	#visualize
	for clusterIndex in range(6):
		quakeT.color(colorList[clusterIndex])
		for aKey in clusters[clusterIndex]:
			longitude = dataDict[aKey][0]
			latitude = dataDict[aKey][1]
			quakeT.goto(longitude * wFactor, latitude * hFactor)
			quakeT.dot()

	quakeWin.exitonclick()

visualizeQuakes('earthquakes.txt')
