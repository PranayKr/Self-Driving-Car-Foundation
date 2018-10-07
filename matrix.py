import math
from math import sqrt
import numbers
#import numpy as np
from copy import deepcopy

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def minor(matrix,r=0,c=0): 
    minor = deepcopy(matrix)
    del minor[r]
    #delete row r
    for b in range(len(minor)):
        #Delete column c
        del minor[b][c]
    return minor

def recursive_det(matrix):
    if len(matrix) == 1:
          return matrix[0][0]
    else:
        determinant = 0
        for i in list(range(len(matrix))): #finding comatrixes of first row elements of the given matrix
            determinant += matrix[0][i] * (-1)**(2+i) * recursive_det(minor(matrix,0,i))
        return determinant    

def adjoint_matrix(matrix):
    minor_mx = minor_matrix(matrix)
    cofactor_mx = cofactor_matrix(minor_mx)
    transpose_mx = transpose(cofactor_mx)
    return transpose_mx    

def minor_matrix(matrix):
    minor_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            minor_det = []
            minor_det = recursive_det(minor(matrix, i,j))
            row.append(minor_det)
        minor_matrix.append(row)
    return minor_matrix

def cofactor_matrix(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[i][j]*(-1)**(2+i+j))
        cofactor_matrix.append(row)
    return cofactor_matrix  

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        #return Matrix(np.linalg.det(self.g))
        return recursive_det(self.g)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        trace = 0
        
        for i in range(self.h):
            trace += self.g[i][i]
            
        return trace


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        #return Matrix(np.linalg.inv(self.g))
        inverse = []
        adjoint = adjoint_matrix(self.g)
        for i in range(len(adjoint)):
            row=[]
            for j in range(len(adjoint[i])):
                row.append(adjoint[i][j]*(1/recursive_det(self.g)))
            inverse.append(row)
        
        return Matrix(inverse)
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        return Matrix([[self[j][i] for j in range(len(self.g))] for i in range(len(self.g[0]))])

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # initialize matrix to hold the results
              
        matrixSum = []
        
        for i in range(self.h):
            row = []
            for t in range(self.w):
            #for t in range(len(self.g[0])):    
                row.append(self.g[i][t]+other[i][t])
                #row.append(self[i][t]+other[i][t])
            
            matrixSum.append(row)
        
        return Matrix(matrixSum)
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
            
        neg_matrix = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]*-1)
                #neg_matrix.append(-self[i][j])
            neg_matrix.append(row)   
        
        return Matrix(neg_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        # initialize matrix to hold the results
        matrixSubtract = []
    
        for i in range(self.h):          
            row = []
            for t in range(self.w):
                row.append(self.g[i][t]-other[i][t])
            
            matrixSubtract.append(row)
        
        return Matrix(matrixSubtract)
    
    def get_column(matrix, column_number):
        column = []
    
        for i in range(len(matrix.g)):
            for j in range(len(matrix.g[i])):
                if(j==column_number):
                    column.append(matrix[i][j])
    
        # print(column)
        return column
    
    def get_row(matrix, row):
        
        return matrix[row]
    
    def dot_product(vector_one, vector_two):
    
        dotsum=0
    
        for i in range(len(vector_one)):
            dotsum+=vector_one[i]*vector_two[i]
                                
        #print(dotsum)
        return dotsum

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        m_rows  = len(self.g)
    
        p_columns =  0
    
        for i in range(len(other.g)):
            for j in range(len(other.g[i])):
                if(i==0):
                    p_columns += 1
                elif(i>0):
                    break;
                    
        result = []
        
        row_result = []
        
        for i in range(m_rows):
            row_result = []
            for j in range(p_columns):
                row_result.append(Matrix.dot_product(Matrix.get_row(self,i),Matrix.get_column(other,j)))
            
            result.append(row_result)
            
        return Matrix(result)    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
        
            #   
            # TODO - your code here
            #
                    
            result = []
        
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.g[i][j]*other)
                    #neg_matrix.append(-self[i][j])
                result.append(row) 
            
            return Matrix(result)
            
            