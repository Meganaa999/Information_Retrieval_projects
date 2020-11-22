import numpy
import pandas
import os
import cmath
import math

#from .config import dataset
from scipy.linalg import svd

dataset_dir="data"
binary_dir="binaries"
package_dir="svd"

dataset=os.path.join(os.path.abspath('./'),dataset_dir)

users_dataset=os.path.join(dataset,"u.user")
rating_dataset=os.path.join(dataset,"ratings.dat")
movies_dataset=os.path.join(dataset,"u.item")

binary=os.path.join(package_dir,binary_dir)

utility_matrix_bin_path=os.path.join(binary,"utility_matrix.pickle")



def load(filepath,column):
    '''
    '''
    with open(filepath,'r',encoding='ISO-8859-1') as f:
        text=str(f.read()).strip().split('\n')
        return pandas.DataFrame.from_records(
            [sentence.split('\t') for sentence in text],columns=column
        )
        
        
def assign_missing_values(input_matrix):
    '''
    '''
    matrix=numpy.asarray(input_matrix,dtype=numpy.float32)
    mean=matrix.mean()
    
    row_count,col_count=[],[]
    
    for x in range(len(input_matrix)):
        row_count.append(numpy.count_nonzero(matrix[x,:]))
    for x in range(len(matrix[0])):
        col_count.append(numpy.count_nonzero(matrix[:,x]))
        
    row_means,col_means = [],[]
    
    for x in range(len(matrix)):
        row_means.append(
            (numpy.sum(matrix[x,:])-(mean*row_count[x]))/(row_count[x]*row_count[x])
        )
    for x in range(len(matrix[0])):
        col_means.append(
            (numpy.sum(matrix[:,x])-(mean*col_count[x]))/(col_count[x]*col_count[x])
        )
    #Replace NA values
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y]==0:
                matrix[x][y]= mean + row_means[x] + col_means[y]
                
            if matrix[x][y]>5:
                matrix[x][y]=5
                
            if matrix[x][y]<1:
                matrix[x][y]=1
    return matrix


        
def preprocess():
    '''
    '''
    dataset=load(rating_dataset,column=['uid','mid','rating','time'])
    dataset.drop(labels=["time"],axis=1,inplace=True)
    dataset=dataset.astype(int)
    
    num_users=list(dataset['uid'].unique())
    num_users.sort()
    
    num_movies=list(dataset['mid'].unique())
    num_movies.sort()
    
    utility_matrix=numpy.full((len(num_users),len(num_movies)),0)
    
    for iter in dataset.index:
        user_index=num_users.index(dataset['uid'][iter])
        movie_index=num_movies.index(dataset['mid'][iter])
        utility_matrix[user_index][movie_index]=dataset['rating'][iter]
        
    #print(utility_matrix)  
    return assign_missing_values(utility_matrix)


#x=preprocess()
#print(x)

def calculate_svd(input_matrix):
    '''
    '''
    input_matrix=numpy.asarray(input_matrix,dtype=numpy.float32)
    
    u,s,vt=svd(input_matrix)
    
    idx_1_1=s.argsort()[::-1]
    s=s[idx_1_1]
    u=u[:,idx_1_1]
    
    idx_1_1=s.argsort()[::-1]
    s=s[idx_1_1]
    vt=vt[:,idx_1_1]
    
    return u,numpy.diag(s),vt

def calculate_svd_90(input_matrix):
    '''
    '''
    
    input_matrix = numpy.asarray(input_matrix, dtype=numpy.float32)

    U, s, Vt = svd(input_matrix)
    sigma = numpy.zeros((input_matrix.shape[0],  input_matrix.shape[1]))
    sigma[:input_matrix.shape[1], :input_matrix.shape[1]] = numpy.diag(s)

    total = 0
    for x in range(min(len(sigma), len(sigma[0]))):
        total = total + (sigma[x][x] * sigma[x][x])

    temp = 0
    temp_total = 0
    for x in range(min(len(sigma), len(sigma[0]))):
        temp_total = temp_total + (sigma[x][x] * sigma[x][x])
        temp = temp + 1
        if (temp_total / total) > 0.9:
            break

    new_U = U[:temp, :temp]
    new_sigma = sigma[:temp, :temp]
    new_Vt = Vt[:temp, :temp]

    #print(new_U, new_sigma, new_Vt)
    return new_U,new_sigma,new_Vt

def cal_spearmann_rank_correlation(d,n):
    diff=6*d/(n(n*n-1))
    return 1-diff

import os
import cmath
import math
import pandas
import numpy



class SVD:
    
    def __init__(self,matrix,k=3):
        self.hidden_factor=k
        self.utility_matrix=matrix
        
    def decompose(self):
        w_1_1 = self.utility_matrix.dot(self.utility_matrix.T)
        e_value_1_1,e_vector_1_1=numpy.linalg.eigh(w_1_1)
        
        w_1_2 = self.utility_matrix.T.dot(self.utility_matrix)
        e_value_1_2,e_vector_1_2=numpy.linalg.eigh(w_1_2)
        
        idx_1_1=e_value_1_1.argsort()[::-1]
        e_value_1_1=e_value_1_1[idx_1_1]
        e_vector_1_1=e_vector_1_1[:,idx_1_1]
        
        idx_1_2=e_value_1_2.argsort()[::-1]
        e_value_1_2=e_value_1_2[idx_1_2]
        e_vector_1_2=e_vector_1_2[:,idx_1_2]
        
        
        self.U=e_vector_1_1
        temp=numpy.diag(numpy.array(
            [cmath.sqrt(x).real for x in e_value_1_2]
        ))
        self.S=numpy.zeros_like(self.utility_matrix).astype(numpy.float64)
        self.S[:temp.shape[0],:temp.shape[1]]=temp
        self.V=e_vector_1_2.T
        
    def reconstruct(self):
        self.reconstructed_matrix=numpy.matmul(
            numpy.matmul(self.U,self.S),self.V
        )
        
    def get_rms_error(self):
        error=0
        N=len(self.reconstructed_matrix)
        M=len(self.reconstructed_matrix[0])
        for i in range(len(self.reconstructed_matrix)):
            for j in range(len(self.utility_matrix[i])):
                error += math.pow(
                    self.reconstructed_matrix[i,j]-self.utility_matrix[i,j],2
                )
        return math.sqrt(error)/(N*M)
    
    def get_mean_abs_error(self):
        """Returns the Mean Absolute Error of the model"""
        error = 0
        N=len(self.reconstructed_matrix)
        M=len(self.reconstructed_matrix[0])
        for i in range(len(self.reconstructed_matrix)):
            for j in range(len(self.utility_matrix[i])):
                error += abs(
                    self.reconstructed_matrix[i,j]-self.utility_matrix[i,j]
                )
        return error/(N*M)
    def get_size_of_matrix(self):
        N=len(self.reconstructed_matrix)
        M=len(self.reconstructed_matrix[0])
        
        return N*M
    
    def cal_spearmann_rank_correlation(self,d,n):
        diff= 6*d/(n*(n*n-1))
        return 1-diff

#import numpy
import pickle
#import svd

if __name__ == "__main__":
    input_matrix = numpy.array([
        [1, 1, 1, 0, 0],
        [3, 3, 3, 0, 0],
        [4, 4, 4, 0, 0],
        [5, 5, 5, 0, 0],
        [0, 2, 0, 4, 4],
        [0, 0, 0, 5, 5],
        [0, 1, 0, 2, 2]])
    a = SVD(input_matrix)
    a.decompose()
    a.reconstruct()
    
    print("the rmse error for svd")
    d1=a.get_rms_error()
    n1=a.get_size_of_matrix()
    print(d1)
    #print("the size of the matrix")
    #print(n1)
    print("spearmann rank correlation for svd")
    s1=a.cal_spearmann_rank_correlation(d1,n1)
    print(s1)
    
    #print("the mean absolute error is")
    #print(a.get_mean_abs_error())
    #print("matrix after assigning missing values")
    #print(assign_missing_values(input_matrix))
    
    U,sigma,Vt=calculate_svd_90(input_matrix)
    svd_90_utility_test_matrix=numpy.matmul(
            numpy.matmul(U,sigma),Vt
        )
    b=SVD(svd_90_utility_test_matrix)
    b.decompose()
    b.reconstruct()
    print("the rmse error for svd with 90 percent energy")
    d2=b.get_rms_error()
    print(d2)
    n2=b.get_size_of_matrix()
    print("spearmann rank correlation for svd with 90% energy")
    s2=b.cal_spearmann_rank_correlation(d2,n2)
    print(s2)
    #print(n2)
    #print(U)
    #print(sigma)
    #print(Vt)
    #calculate_svd_90(x)
