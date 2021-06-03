from matplotlib import pyplot as plt
from statistics import mean
import copy
import numpy
def linearregression(data):
    data = [list( map(float,i) ) for i in data]
    listx = [row[0] for row in data]
    
    listy = [row[1] for row in data]
    n = len(listy)
    
    sumx = sum(listx)
    sumy = sum(listy)
    sumxy = sum([a*b for a,b in zip(listx,listy)])
    sumx2 = sum([a*b for a,b in zip(listx,listx)])
    xbar = mean(listx)
    ybar = mean(listy)
    a1 = (n*sumxy - sumx*sumy) / (n*sumx2 - (sumx)**2)
    a0 = ybar - a1*xbar
   
    xplot = numpy.linspace(0,max(listy), len(listx))
   
    yplot = [0] * len(listy)

    for i in range(len(xplot)):
        yplot[i] = a0 + a1*xplot[i]
        
    plt.scatter(listx,listy)
    plt.plot(xplot, yplot)
    plt.show()
    
    yrt = copy.deepcopy(listy)
    for i in range(len(yrt)):
        yrt[i] = yrt[i] - ybar
    st = sum([a*b for a,b in zip(yrt,yrt)])
    
    yrr = copy.deepcopy(listy)
    for i in range(len(yrr)):
        yrr[i] = yrr[i] - (a0 + a1*listx[i])
    sr = sum([a*b for a,b in zip(yrr,yrr)])
    
    r2 = (st-sr)/st
    return r2
    
import csv
def main():
    data1 = list(csv.reader(open("mydata.csv")))
    r = linearregression(data1) 
    print("Correlation coefficient for noisy data is: %0.5f" % r) 
    
    data2 = list(csv.reader(open("Workbook1.csv")))
    r = linearregression(data2) 
    print("Correlation coefficient for y=2x+5 is: %0.5f" % r) 

    
    
main()
    
