 ##
#
# @author Florian BELLANGER, Fyne DC, Annecy, FRANCE
# @brief a set of generic functions for data management

import numpy as np
from random import randrange


def average_above_zero(table):
    """
    make average from a table of non-null positiv value
    Arg:
        table : a list of numeric values
    return:
        he computed average
    raise :
        check if there is no positive value in table
    """
    if not(isinstance(table, list)):
        raise ValueError('expeced a list as input')
    
    average = -1
    sum=0.0
    positifValueNumber=0
    for val in table:
        if val>0:
            sum=sum+val
            positifValueNumber=positifValueNumber+1
    if positifValueNumber <= 0:
        raise ValueError('any positiv numbre in tab in function average_above_zero')
    
    
    average = sum/positifValueNumber
    return average

"""
mesNotes =[5,12,18,-1]#give 11.66666666
print('moyenne : '+str(average_above_zero(mesNotes)))
mesNotes =[5,12,12,-1]#give 9.66666666
print('moyenne : '+str(average_above_zero(mesNotes)))
"""


def reverse_table(table):
    """
    reverse a table without the use of any other table
    Arg:
        table : a list of thing
    return:
        the reveersed table
    """
    
    numberOfElement = len(table)
    currentIndex = 0
    #temporal value for reverse
    
    for index in range(0,numberOfElement):
        if currentIndex >= numberOfElement/2:
            return table
        temp =table[currentIndex]
        table[currentIndex] = table[numberOfElement-1-currentIndex]
        table[numberOfElement-1-currentIndex]=temp
        currentIndex = currentIndex+1
        
    return "error"
        
"""
tableToReverse =[5,12,13,-1,16]
print(reverse_table(tableToReverse))
tableToReverse =[5,12,13,-6]
print(reverse_table(tableToReverse))
"""    
    


def roi_bbox(input_image):
    """
        give the bounding box coordinates of the object where the object is all the "1" point
    Arg:
        input_image : a array[X,Y]
    return:
        the bounding box value where the point (0,0) is on the top left corner
    """
    position =np.array([[ -1, -1],
                      [ -1, -1],
                      [ -1, -1],
                      [ -1, -1]])
    listOfObjectComponent = np.zeros([2,2],dtype=int)
 
    bouncingXmin=-1
    bouncingXmax=-1
    bouncingYmin=-1
    bouncingYmax=-1
    
    """
    variables above are the equation on an X/Y plan of the border's bounding box. bouncing_Alpha_minOrMan where we can write alpha = ax+b (or just alpha = b here)
    """
    
    imageX = 0
    imageY = 0
    iFoundNothing = True
    """
    iFoundNothing  = useful, permit to end loops faster
    """
    while imageX < len(input_image) and iFoundNothing:
        while (imageY < len(input_image[imageX])) and iFoundNothing:
            if input_image[imageX][imageY]==1 :
                bouncingXmin=imageX
                iFoundNothing = False
            imageY+=1
        imageY = 0
        imageX+=1
        
        
    iFoundNothing = True
    imageX = len(input_image)-1
    imageY = len(input_image[imageX])-1 
    
    while imageX > 0 and iFoundNothing:
        while imageY > 0 and iFoundNothing:
            if input_image[imageX][imageY]==1 :
                bouncingXmax=imageX 
                iFoundNothing = False
            imageY-=1
        imageY =  len(input_image[imageX])-1
        imageX-=1
               
    iFoundNothing = True    
    imageX = 0
    imageY = 0
    
    while imageY < len(input_image) and iFoundNothing:
        while imageX < len(input_image[imageY]) and iFoundNothing:
            if input_image[imageX][imageY]==1 :
                bouncingYmin=imageY
                iFoundNothing = False
            imageX+=1
        imageX = 0
        imageY+=1
    
    
    iFoundNothing = True
    imageX = len(input_image)-1
    imageY = len(input_image[imageX])-1 
    
    
    while imageY > 0 and iFoundNothing:
        while imageX > 0 and iFoundNothing:
            if input_image[imageX][imageY]==1 :
                bouncingYmax=imageY
                iFoundNothing = False
            imageX-=1
        imageX = len(input_image)-1
        imageY-=1
        
        
        
    print(bouncingYmin)
    print(bouncingYmax)
    print(bouncingXmin)
    print(bouncingXmax)
    return position

"""
image = np.array([[  0, 0, 0, 0, 0, 0],
               [  0, 1, 0, 0, 0, 0],
               [  0, 0, 0, 0, 0, 0],
               [  0, 0, 0, 0, 0, 0],
               [  0, 0, 0, 0, 0, 0],
               [  0, 0, 0, 0, 0, 0]])

roi_bbox(image)
"""

def give_back_array_full_of_empty_string(table):
    """
    give_back_array_full_of_empty_string
    """
    for posX in range(0,len(table)):
        for posY in range(0,len(table[posX])):
            table[posX][posY]=''
    
    
    return table


def random_fill_sparse(table, K):
    """
        fill K random cells position with the 'X' value of a numpy array N*N 
    Arg:
        table : a array[N,N]
        K : the number of cells the function shoul fill with 'X'
    error:
        raise error if N*N < K
    return:
        the bounding box value where the point (0,0) is on the top left corner
    """
    
    if len(table) * len(table)<K:
        raise ValueError('not enough cells in table')
        
        
    table = give_back_array_full_of_empty_string(table)
    numberOfX = 0
    fillWith = 'X'
    """
    we must be sure to have K cells fill with X, just do
    for range(0,K)
        posX = randrange(0,len(table))
        posY = randrange(0,len(table))
        table[posX][posY] = fillWith
    don't permit to be sure
    """
    while numberOfX < K:
        numberOfX = 0
        posX = randrange(0,len(table))
        posY = randrange(0,len(table))
        """
        randrange can't return the seconde value in parametter
        """
        table[posX][posY] = fillWith
        for posX in range(0,len(table)):
            for posY in range(0,len(table[posX])):
                if table[posX][posY] == fillWith:
                    numberOfX +=1
    

    return table

"""
size = 5
myArray = np.empty([size,size], dtype=str)
myArray = random_fill_sparse(myArray,6)
print(myArray)
"""
def remove_whitespace(table):
    """
        remove whitespace of a string
    Arg:
        table : a string
    return:
        the string without whitespace
    """
    index = 0
    while index < len(table):
        if(table[index]==' '):
            table =table[0:index]  +table[index+1:len(table)-1]
        index+=1
    return table


"""
myString = 'The coconut nut is a giant nut'
myString = remove_whitespace(myString)
print(myString)
"""

def shuffle(list_in):
    """
        shuffle a list  efficiently
    Arg:
        list_in : a list
    return:
        the shuffle list
    """
    randomizeList =[None] * len(list_in)

    while len(list_in)>0:
        theChoosenOne = randrange(0,len(list_in))
        randomizeList[len(list_in)-1] = list_in[theChoosenOne]
        del list_in[theChoosenOne]
    
    
    return randomizeList


tableToShuffle =[5,12,13,-1,16]
tableToShuffle =shuffle(tableToShuffle)
print(tableToShuffle)


"""
# a variable
a=1 # default type : int

# an empty list
mylist = []

#a filled list
mylist2=[1,2,3]

#append to a list
mylist.append(10)

# a buggy list
mybuggylist=[1,'a', "Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""


"""
def average_above_zero(input_list):
    ##
    # compute the average of positive values
    # @input_list : the list of values to process
    # @return the average value of all the positive elements

    #init critical variable
    positive_values_sum=0
    positive_values_count=0

    first_item=input_list[0] #just a line to generate a code smell with an unused value

    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is null:'+str(item))
        else:
            print('This value is negative:'+str(item))
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count)
    print('Positive elements average is '+str(average))
    return float(average)

    
    
    
"""#testing average_above_zero function:
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
                                                                          res=result)
print(message)
"""

def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init max_value and its index
    max_val=input_list[0]
    max_idx=0
    #compute the average of positive elements of a list
    """for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item
    """
    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        #select only positive items
        if max_val<input_list[idx]:
            max_val=input_list[idx]
            max_idx=idx


    #generic style : iterate over the range of list indexes
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx

    return max_val, max_idx

def average_above_zero(tab):
        """
        Calcule la moyenne
        Args:
            tab is a list of numeric value

        return:
            the computed average

        raise:
            Value error if no positive value is found
            Value error if input tab is not a list
        """
        
        if not(isinstance(tab , list)):
            raise ValueError('Expected a list as input')
        
        average =.99

        valSum =0.0
        nPositiveValue = 0
        NMAX = len(tab)

        for val in range(0,NMAX):
            if val > 0:
                valSum = valSum + float(val)
                nPositiveValue = nPositiveValue+1

        if nPositiveValue <= 0:
            raise ValueError('No positif value found')

        average = valSum/nPositiveValue

        return average


test_tab = [1,7,8,-5 , 5]
<<<<<<< HEAD
moy = average_above_zero(test_tab)
=======
moy = average_above_zero(testTab)
>>>>>>> 3727b2a18e3e2302f838bca50faf188cddfdbc3c
print(moy)

def max_value(tabValue)
     """
        Calcule la valeur max du tableau
        Args:
            tab is a list of numeric value

        return:
            the max value

        raise:
        """
        maxTab = max(testTab)
        return maxTab


tab = [1,7,8,-5 , 5]
maxTab


tab = [1,2,3,4]
tabMax = max(tab)
print(tabMax)





"""
#test max_value function
#1 basic test, expected answer=2
mylist=[-1,2,-20]
mymax, mymaxidx=max_value(mylist)
mymax_tuple=max_value(mylist)
mymax=mymax_tuple[0]
print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
#==> message : "Max value of [-1, 2, -20] is (2, 1)"

#2 error test : Exception expected
max_value([])
"""

"""
# hints to solve the roi_bbox function exercise: numpy basics

#matrix processing lib
import numpy

#create a numpy matrix with specific dimensions
size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows, size_cols], dtype=int)
#set a value in a specific cell
myMat[1,3]=1

#fil something in the matrix, the basic way (a very slow python way...)
for row in range(5,8):
    for col in range(7,9):
        myMat[row,col]=1

#get time to measure processing speed
import time
init_time=time.time()

#filling something in the matrix, a nicer way
myMat[2:4,5:9]=1 #assign a scalar to each cell of a subarray
myMat[4:7,7:9]=numpy.ones([3,2]) #copy an array in a subarray
print(myMat)

#get ellapsed time
filling_time=time.time() -init_time
print('data prefecting time='+str(filling_time))

#fake bounding box coordinates matrix
xmin=0
xmax=100
ymin=0
ymax=200
#how to fill the 4x2 bbox coordinates matrix, method 1 using 1D numpy arrays (ugly?)
bbox_coords=numpy.zeros([4, 2], dtype=int)
bbox_coords[0,:]=numpy.array([ymin, xmin])
bbox_coords[1,:]=numpy.array([ymin, xmax])
bbox_coords[2,:]=numpy.array([ymax, xmin])
bbox_coords[3,:]=numpy.array([ymax, xmax])
#how to fill the 4x2 bbox coordinates matrix, method 2 using lists (shorter way)
#->create a list of lists
coordsList=[[ymin, xmin],[ymin, xmax],[ymax, xmin],[ymax, xmax]]
#->convert to an array
coords_array=numpy.array(coordsList)
"""
=======

