import turtle 
from figures import drawRectangle_wh

def mean(aList):
	"""returns a mean (average) value for a list of items"""
	return sum(aList)/(len(aList) * 1.0) 


def frequencyChart(aList):
	countDict = {}
	
	## forming the dictionary
	for item in aList:
		if item in countDict:
			countDict[item] += 1
		else:
			countDict[item] = 1

	itemList = list(countDict.keys())
	minItem = min(itemList)
	maxItem = max(itemList)

	countList = list(countDict.values())
	maxCount = max(countList)
	
	#itemList = list(countDict.items())
	#itemList = sorted(itemList, key = lambda x: x[1], reverse = True)		#sorted on the basis of frequency
	#print itemList

	## initialising
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	avg = mean(aList)
	if maxCount + 2 > avg:
		yLarge = maxCount + 2
	else:
		yLarge = avg + 1
	wn.setworldcoordinates(-1, -1, maxItem + 2, yLarge)
	#chartT.hideturtle()

	## drawing axes
	#x-axis
	chartT.up()
	chartT.goto(minItem, 0)
	chartT.down()
	chartT.goto(maxItem + 1, 0)
	#y-axis
	chartT.up()
	chartT.goto(minItem, 0)
	chartT.down()
	chartT.goto(minItem, yLarge - 1)
	chartT.up()

	## labelling the axes
	#y-axis
	for i in range(maxCount + 2):
		chartT.goto(minItem, i)
		chartT.dot()
		chartT.goto(minItem -0.5, i)
		chartT.write(str(i), font = ('Verdana', 10))
	#x-axis 
	for i in range(minItem, maxItem + 2):
		chartT.goto(i, 0)
		chartT.dot()
		chartT.goto(i, -0.5)		
		chartT.write(str(i), font = ('Verdana', 10))

	##representing the mean value
	chartT.up()
	chartT.goto(minItem, avg)
	chartT.down()
	chartT.dot()
	chartT.color('Red')
	chartT.goto(maxItem, avg)
	chartT.up()
	chartT.color('Blue')
	## drawing the chart
	chartT.fillcolor('blue')
	for i in itemList:
		chartT.goto(i - .125, 0)
		chartT.down()
		chartT.begin_fill()
		drawRectangle_wh(chartT, 0.25, countDict[i])
		chartT.end_fill()
		chartT.up()

	wn.exitonclick()


aList = [3, 3, 5, 7, 5, 3, 14, 14, 14, 4, 6, 3, 4, 6, 3, 4, 5, 6, 6]
frequencyChart(aList)

