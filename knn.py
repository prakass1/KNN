import random
import csv
import math
import operator
import time
data = []

def nominalToNumeric(data):
    dic={}
    k=1
    for items in data:
        for val in ((items)):
            if val not in dic:
                dic[val]=k
                k=k+1

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=dic.get(data[i][j])
    myfile = open('car1.csv','w')
    with myfile:
        writer=csv.writer(myfile)
        writer.writerows(data)

    print("hello")
    #print(data)
    print(dic)

def loadCsv(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row)
    nominalToNumeric(data)
    return data
def splitData(dataset, splitRatio):
    random.shuffle(dataset)
    trainSet = dataset[:(int)(len(dataset) * splitRatio)]
    testSet = dataset[(int)(len(trainSet)):]
    return (trainSet, testSet)


def euclideanDistance(one,two,length):
    distance=0

    for x in range(length):
        distance += pow((int(one[x]) - int(two[x])),2)
#    print("fknjkfjf{1}",{math.sqrt(distance)})
    return ((distance))

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def nearNeighbors(trainingData,testData,k):
    distances=[]
    length=len(testData)-1

    for x in range(len(trainingData)):


        dist=euclideanDistance(trainingData[x],testData,length)

        distances.append((trainingData[x],dist))

    distances.sort(key=operator.itemgetter(1))

    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors




def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
def getErrorRate(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return 1.0 - (correct/float(len(testSet)))


def iterartion(k,dataset,splitRatio):

    trainingData,testData=splitData(dataset,splitRatio)
    prediction=[]

    for x in range(len(testData)):
        neighbors=nearNeighbors(trainingData,testData[x],k)
        results=getResponse(neighbors)
        prediction.append(results)

    accuracy=getAccuracy(testData,prediction)
    erate=getErrorRate(testData, prediction)

    return erate


def main():
    filename = 'car1.csv'
    splitRatio = float(2/3)

    dataset = loadCsv(filename)

    print("enter the no of K")
    k=int(input())
    er=0
    start_time = time.time()
    for i in range(1):
        er+=iterartion(k,dataset,splitRatio)
    print("the total erate"+str(er/1))
    print((time.time()-start_time))







main()
