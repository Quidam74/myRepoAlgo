 ##
#
# @author Florian BELLANGER, Fyne DC, Annecy, FRANCE
# @brief a set of generic functions for data management

import numpy as np

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

