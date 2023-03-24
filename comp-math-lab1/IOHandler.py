from validator import *
n=0
epsilon=0
matrix=[]

def inputInfo():
        gap()
        
        while(True):
                print("Do you want to read input data from file? yes/no")
                answ=input()
                if(answ=="yes"):
                        print("Please enter your file name")
                        answ = inputFromFile(input())
                elif(answ=="no"):
                        answ = inputFromCMD();
                else:
                        errorPrint("yes/no")
                        continue
                if (answ[2]==False):
                        errorPrint("Chage your file or type by CMD.")

                else:
                        return answ
        
def inputFromFile(file):
        try:
                with open(file) as f:
                        if(not getDim(f.readline)):
                                errorPrint("File corrupted. Dimension must be integer from 1 to 20")
                                return [matrix,epsilon,False]
                        if(not getError(f.readline)):
                                errorPrint("File corruputed. Epsilon must be float positive number")
                                return [matrix,epsilon,False]
                        return [matrix,epsilon, getMatrixFromFile(n,f)]
        except FileNotFoundError as e:
                errorPrint("File not found.")
                return [matrix,epsilon,False]
                        

def inputFromCMD():
        gap()
        print("Please, enter the number of dimensions")
        while(not  getDim(input)):
                errorPrint("Dimension must be integer from 1 to 20")
        gap()
        print("Please, enter required accuracy")
        while(not getError(input)):
                errorPrint("Epsilon must be float positive number")
        gap()
        print("Please, enter your matrix (A|B) row by row")
        getMatrix(n)
        return [matrix,epsilon,True]

def getDim(stream):
        try: 
                global n
                n =int(stream())
                return validateDim
        except: 
                return False;
def getError(stream):
        try: 
                global epsilon
                epsilon =float(stream())
                return validateEpsillon
        except: 
                return False;
def getMatrix(n):
        tmp=[]
        global matrix
        for i in range(n):
                try:
                        tmp=list(map(float,input().split()))
                        if(validateRow(tmp,n)):
                                 matrix.append(tmp)
                        else:
                               errorPrint("All coefficients must be numbers. Try again")
                               --i 

                       
                except:
                       errorPrint("All coefficients must be numbers. Try again")
                       --i
def getMatrixFromFile(n,file):
        tmp=[]
        global matrix
        for i in range(n):
                try:
                        tmp=list(map(float,file.readline().split()))
                        if(validateRow(tmp,n)):
                                 matrix.append(tmp)
                        else:
                               errorPrint("File corrupted. All coefficients must be numbers. ")
                               return False
                              

                       
                except:
                       errorPrint("File corrupted. All coefficients must be numbers. ")
                       return False
                      

        
def greeting():
        print(f"-"*20 + f"Welcome" + f"-"*20)
def gap():
        print(f"-"*47)
def answ(sol):
        gap()
        print("Here is the answer: ")
        for i in range(len(sol[0])):
                print(f"x {i} = {sol[0][i]:.3f}") 
        print(f"It was found within {sol[1]} iterations")
        gap()
        print("Mistake:")
        for i in range(len(sol[2])):
                print(f"x {sol[1]} - x {sol[1]-1} = {sol[2][i]:.3f}") 

def errorPrint(error):
        print("Smth gone wrong. %s" %(error))
def notConverges():
        print("No solutions")