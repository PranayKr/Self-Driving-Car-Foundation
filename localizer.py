import pdb
from helpers import normalize, blur

import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    #
    # TODO - implement this in part 2
    #
     
    # loop through all grid cells    
    for i in range(len(beliefs)):
        for j in range(len(beliefs[i])):
            hit = (color == grid[i][j])
            if(hit==False):
                new_beliefs.append(float(beliefs[i][j]) * (0.0*p_hit + (1-0.0) * p_miss))
            elif(hit==True):
                new_beliefs.append(float(beliefs[i][j]) * (1.0*p_hit + (1-1.0) * p_miss))
                
                              
    # sum up all the components
    summatn = sum(new_beliefs)
    new_beliefs = reshape(new_beliefs,3,3)
    
     # divide all elements of q by the sum to normalize    
    #for i in range(len(beliefs)):
        #for jf in range(len(beliefs[i])):
    for i in range(len(new_beliefs)):
        for jf in range(len(new_beliefs[i])):    
            #print(jf)
            #print(len(beliefs[i]))
            #print(len(beliefs))
            #print(len(new_beliefs))
            #pdb.set_trace()
            new_beliefs[i][jf] = new_beliefs[i][jf]/summatn
            #pdb.set_trace()
          
    #print(new_beliefs)
    return new_beliefs


def reshape(thelist, rows,cols):  
    parent_list = []
    count = 0
    for j in range(rows):
        new_list = []
        for i in range(cols):
            new_list.append(thelist[count])
            count+=1
        parent_list.append(new_list)
    return parent_list

def move(dy, dx, beliefs, blurring):
    #height = len(beliefs)
    #width = len(beliefs[0])
    height = len(beliefs[0])
    width = len(beliefs)
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            #pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)