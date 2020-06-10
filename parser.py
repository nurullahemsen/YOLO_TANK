def clearFile(file):
    open(file, "w").close()

def parseObject(file="deneme.txt"):
    f = open(file, "r")
    contents = f.read()

    print(contents)

    lineContents = contents.split("\n")
    # print(lineContents)

    for i in range(len(lineContents)):
        if(lineContents[i] != ""):
            lineContents[i] = lineContents[i].strip().split(" ")
        else:
             lineContents.pop()
    f.close()
    clearFile(file)

    return lineContents


class FeatureObject:
    def __init__(self, contentsList):
        self.type = contentsList[0]
        self.confidence = int(contentsList[1].split("%")[0])
        self.left = int(contentsList[2].split("=")[-1][:-1])
        self.right = int(contentsList[4].split("=")[-1][:-1])
        self.top = int(contentsList[3].split("=")[-1][:-1])
        self.bottom = int(contentsList[5].split("=")[-1])

def mainObject(file):
	list = parseObject(file)
	#print(list)

	personObject = None;
	confidence = 0;
	for item in list:
		obj = FeatureObject(item)
		if obj.confidence > confidence and obj.type == "person":
			personObject = obj
			confidence = obj.confidence

	try:
		print(personObject.confidence)
		return personObject
	except AttributeError:
		print("No FeatureObject")
		return None
	
	
if __name__ == '__main__':
	mainObject("/home/pi/Desktop/deneme.txt")
