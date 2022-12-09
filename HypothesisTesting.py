import numpy as np
from matplotlib import pyplot as plt

def readFile():                          #It reads the "titanic_data.txt" named file and it puts the data according to their classes and returns them
    file = open("titanic_data.txt")
    
    crewData = []
    firstClassData = []
    secondClassData = []
    thirdClassData = []
    bigData = []
    
    fileData = [[]]                                 #It holds the whole data
    stripped = [line.strip() for line in file]      #Strips the \n
    for i in stripped:
        split_line = i.split("\t")
        fileData.append(split_line)
    file.close()
    
    
    for i in range(2, len(fileData)):    #It starts at 2 because fileData[0] = [] and fileData[1] = [Class, Survive]
        class_ = fileData[i][0]
        data = fileData[i][1]
        if class_ == '1':
            firstClassData.append(data)
        elif class_ == '2':
            secondClassData.append(data)
        elif class_ == '3':
            thirdClassData.append(data)
        elif class_ == '0':
            crewData.append(data)
        bigData.append(data)
        
    return crewData,firstClassData,secondClassData,thirdClassData,bigData    #It returns all the information that we need from the file

def calculateMean(data):
    mean = 0
    for i in data:
        mean += int(i)
    mean /= len(data)
    return mean

def calculateMeans(data1,data2,data3,data4,data5):
    data1Mean = calculateMean(data1)
    data2Mean = calculateMean(data2)
    data3Mean = calculateMean(data3)
    data4Mean = calculateMean(data4)
    data5Mean = calculateMean(data5)
    return data1Mean,data2Mean,data3Mean,data4Mean,data5Mean
    
def testing(data1,data2,number):                     #number 1 and 2 is option numbers. I added it just because I can combine options in the assignment into one function
    N = 10000
    combineList = []                                 #The combinations of 2 data list are stored in here
    tempData1 = []                                   #After shuffling the combineList put the random datas in there. (same size as data1)
    tempData2 = []                                   #After shuffling the combineList put the random datas in there. (same size as data2)
    differenceBetweenMeans = []                      #We used this for appending the new randomized datas differences.
    
    for k in range(N):               
        for i in data1:
            combineList.append(i)
        for j in data2:
            combineList.append(j)
        np.random.shuffle(combineList)                #Shuffling the combining list for guarantee the randomization
        for l in range(len(data1)):
            tempData1.append(combineList[l])          #Separating the randomized list into 2 again
        for m in range(len(data1), len(combineList)):
            tempData2.append(combineList[m])          #Separating the randomized list into 2 again
            
        meanData1 = calculateMean(tempData1)    #Mean of new randomized data1
        meanData2 = calculateMean(tempData2)    #Mean of new randomized data2
        
        sampleMeanDifference = meanData2 - meanData1                  #Mean difference of the 2 datas
        differenceBetweenMeans.append(sampleMeanDifference)           #Appending the list in each for cycle
        
        tempData1.clear()
        tempData2.clear()
        combineList.clear()
        
    plt.figure(figsize=(12,6))
    count,bins,ignore = plt.hist(differenceBetweenMeans,bins=100, density=False)         #Pdf histogram
    plt.show()
    
    CDF = np.cumsum(count) / sum(count)         #CDF function
    bins = bins[1:]
    plt.figure(figsize=(12,6))
    plt.plot(bins,CDF)    #CDF graph
    
    meanData1 = calculateMean(data1)      
    meanData2 = calculateMean(data2)
    x = meanData1- meanData2      #The x value calculated by subtracting data2's mean from data1's.
    index = 0
    lenBins = len(bins)
    
    for j in range(lenBins):      #Finds the corresponding index
        if bins[j] >= x:
            index = j
            break
        
    pValue = CDF[index]         #Find the pValue
    pValueArray = [0,pValue]    #For graph
    xValueArray = [x,x]         #For graph
    plt.plot(xValueArray,pValueArray)        #CDF
    plt.show()
    
    if (number == 1):
        print("The p-value for "+ str(round(meanData1-meanData2,2))+" difference and less between means for crew and 3rd class is " + str(round(CDF[index],2)))
    elif (number ==2):
        print("The p-value for " + str(round(meanData1-meanData2,2)) + " difference and more in means for 1st class and the rest is " + str(round(CDF[index],2)))


def main():
    crewData,firstClassData,secondClassData,thirdClassData,bigData = readFile()
    bigDataMean,crewDataMean,firstClassMean,secondClassMean,thirdClassMean = calculateMeans(bigData,crewData,firstClassData,secondClassData,thirdClassData)
    
    print("The averages for the whole data, crew data, first class, second class and third class data are " +
          str(round(bigDataMean, 2)) + ", " + str(round(crewDataMean, 2)) + ", " + str(round(firstClassMean, 2)) +
          ", " + str(round(secondClassMean, 2)) + " and " + str(round(thirdClassMean, 2)) + " respectively.")
    
    rest = []     #It combines the datas (crewData,secondClassData,thirdClassData) for using in the second option.
    for i in range(len(crewData)):
        rest.append(crewData[i])
    for i in range(len(secondClassData)):
        rest.append(secondClassData[i])
    for i in range(len(thirdClassData)):
        rest.append(thirdClassData[i])
    
    
    testing(crewData, thirdClassData,1)
    testing(firstClassData,rest,2)


main()