# code written in Python 3.6 by Naseem Amjad


def solution(S, C):
    MyInitialList=ConvertFromNewLine(S)

    l = []#list
    
    for item in MyInitialList:
        subl = []
        for val in item.split(' '):
            subl.append(val)
            
        l.append(subl)
        
    l2=[]#2 dimensional list
    
    for i in range(len(l)):
        for j in range(len(l[i])):
            temp1=l[i][j]
            l2.append(ConvertFromComma(temp1))
            
    myCindex=find2(l2[0],C)
    
    maxValue=-9999
    
    for k in range(1,len(l2)):
        tempValue=(l2[k][myCindex])
        
        myValue=int(tempValue)
        if (myValue>maxValue):
            maxValue=myValue
            myMaxIndex=k
            
    print(l2)#final list
    print("Maximum Value of Column \'"+C+"\' is "+str(maxValue))
        


def find2(a, C):
    x = [x for x in a if C == x][0]
    return (a.index(x))
    
def ConvertFromNewLine(string):
    li = list(string.split("\n"))
    return li
    
def ConvertFromComma(string):
    li = list(string.split(","))
    return li
    
    
solution('area,land\n3722,CN\n6612,RU\n3855,CA\n3797,USA', 'area')


solution('city,temp2,temp\nParis,7,-3\nKarachi,4,-4\nLahore,-1,-2', 'temp')
