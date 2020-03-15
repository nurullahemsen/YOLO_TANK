from parser import FeatureObject


def move(obj):
	left = obj.left
	right = obj.right
	
	if (left + right) // 2 < 416 // 3:
		moveLeft()
		
	elif (416 * 2) // 3 > (left + right) // 2 > 416 // 3:
		moveForward()
			
	else:
		moveRight()






def moveForward():
	print("MOVE FORWARD!!!")
	
	
	
	
def moveLeft():
	print("MOVE LEFT!!!")
	
	
	
	
	
def moveRight():
	print("MOVE RIGHT!!!")
