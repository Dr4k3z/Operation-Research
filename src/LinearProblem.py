import numpy as np

def firstNeg(vec):
    n = len(vec)
    for i in range(n):
        if vec[i]<0:
            return i
    return -1

def illimitateOpt(A):
    if np.any(A[0,:]<0):
        m,n = A.shape
        for i in range(n):
            if A[0,:][i]<0:
                for j in range(m):
                    if A[j][i] > 0:
                        return False
        return True

class LinearProblem:
    #Private Methods
    def __inbase(self):
        n = len(self.T[0])
        base = []
        for i in range(n-1):
            if self.T[0,i] == 0:
                #print("Variabile x",i," in base")
                base.append(i)
        return base


    def __simplex(self):
        m,n = self.T.shape
        while np.any(self.T[0,:]<0) and not illimitateOpt(self.T):
            A = self.T
            idx = firstNeg(self.T[0,:])
            quotient = 10000*np.ones(m)
            for j in range(m):
                if self.T[j,idx] > 0:
                    quotient[j] = self.T[j,n-1]/self.T[j,idx]
            j = int(np.argwhere(quotient==np.min(quotient))[0]) #for Bland's rule, we shall take the first
            p,q = j,idx #pivot
            #print("pivot: ",p,",",q)
        
            A[p,:] = self.T[p,:]/self.T[p,q]
            for j in range(m):
                if j!=p:
                    A[j,:] = self.T[j,:] - (self.T[p,:]/self.T[p,q])*self.T[j,q]
            self.T = A
            #print(self.T)


    def __solution(self):
        xb = self.__inbase()
        sol = []
        for b in xb:
            idx = int(np.argwhere(self.T[:,b]==1))
            #print("x",b," = ",self.T[idx,-1])
            sol.append(self.T[idx,-1])
        return sol
    

    #Constructors
    def __init__(self,A,b,c):
        m,n = A.shape
        #variables
        self.vars = {}
        for i in range(n):
            self.vars[i] = "x"+str(i)
        #build tableau
        self.T = np.zeros([m+1,n+1])
        self.T[0,:n] = c
        self.T[1:m+1,n] = b
        self.T[1:m+1,0:n] = A
        

    #Public methods
    def optimum(self):
        #Check if Simplex stopped cause of Illimitate Optimun:
        if illimitateOpt(self.T):
            #print(self.T)
            return "inf, Illimitate Optimum!"
        return self.T[0,-1]


    def solve(self,method):
        if method=="simplex":
            self.__simplex()
            m = len(self.T[:]) - 1
            base = ""
            for i in range(m-1):
                base += ("x" + str(self.__inbase()[i] + 1) + ", ")
            base += ("x" + str(self.__inbase()[m-1] + 1))
            if illimitateOpt(self.T):
                return base, np.ones(m) * np.inf
            return base, self.__solution()
