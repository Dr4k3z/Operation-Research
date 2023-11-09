import numpy as np
import time
from src.LinearProblem import LinearProblem

'''
            What's next??

1)  Not sure the program works where no admissible basis 
    can be found. Implement Phase I simplex

2)  The algo does not manage the case of an illimitate 
    problem. Add limitation clause in the j = argmin section

3)  Test the script for performance in terms of execution 
    time and memomary management, I bet there's still a lot 
    of room for improvement. Develop an actual benchmark, 
    not the one currently implemented

4)  Adapt the optimum outcome to the actual scope, wether a 
    maximization or minimization
    
5)  Implement other methods to solve a linear programming 
    problem. 
'''
def main():
    A = np.array([[1,2,3,1],
                  [2,1,1,2]])
    b = np.array([3,4])
    c = np.array([-1,-3,-5,-2]) 
    prob = LinearProblem(A,b,c)
    sol = prob.solve("simplex")
    print("Variables in base:", sol[0], "\nCorrispective values:", sol[1])
    print("Optimum:", prob.optimum())

    #Illimitate Problem example:
    print()
    A = np.array([[1,-2,1,0],
                  [-2,-1,0,1]])
    b = np.array([3,4])
    c = np.array([-1,3,5,-2]) 
    prob = LinearProblem(A,b,c)
    sol = prob.solve("simplex")
    print("Variables in base:", sol[0], "\nCorrispective values:", sol[1])
    print("Optimum:", prob.optimum())

if __name__=="__main__":
    begin = time.time()
    main()
    end = time.time()
    delta = 1000*(end-begin)
    print("time elapsed: ",delta)
