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
        if val>=0:
            sum=sum+val
            positifValueNumber=positifValueNumber+1
    if positifValueNumber <= 0:
        raise ValueError('any positiv numbre in tab in function average_above_zero')
    
    
    average = sum/positifValueNumber
    return average


mesNotes =[5,12,18,0]#give 11.66666666
print('moyenne : '+str(average_above_zero(mesNotes)))
mesNotes =[5,12,12,0]#give 9.66666666
print('moyenne : '+str(average_above_zero(mesNotes)))
"""
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

