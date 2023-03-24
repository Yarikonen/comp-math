def isSolutionConverge(matrix):
        count = 0
        for i in range(len(matrix)):
                
                if(2*abs(matrix[i][i])<sum(map(abs,matrix[i]))-abs(matrix[i][len(matrix)])):
                        if (i==len(matrix)):
                                return False
                        maxx = 0
                        k=-1
                        for j in range(i+1,len(matrix)):
                                
                                if(2*abs(matrix[j][i])>=sum(map(abs,matrix[j]))-abs(matrix[i][len(matrix)]) and abs(matrix[i][j])>=maxx):
                                        max=matrix[j][i]
                                        k=j
                        if(k==-1):
                                return False
                        if(2*abs(matrix[k][i])>sum(map(abs,matrix[k]))-abs(matrix[i][len(matrix)])):
                                count+=1;
                        matrix[i],matrix[k]=matrix[k],matrix[i]
        return count>0
def solution(matrix,x,epsillon,i):
        x_next=[0]*len(matrix)
        for i in range(len(matrix)):
                a = (matrix[i][len(matrix)]/matrix[i][i])-scalarMult(list(map(lambda x: x/matrix[i][i],matrix[i]))[:i],x_next[:i])-scalarMult(list(map(lambda x: x/matrix[i][i],matrix[i]))[i+1:-1],x[i+1:])
                x_next[i]=a
        if(findError(x_next,x)<epsillon):
                return (x_next,i,list(abs(x_next[i]-x[i]) for i in range(len(x))))
        return(solution(matrix,x_next,epsillon,i+1))
        

def findError(x_next,x):
       return max(list(abs(x_next[i]-x[i]) for i in range(len(x))))

def scalarMult(x,y):
        summ=0
        for i in range(len(x)):
                summ+=x[i]*y[i]
        return summ
def findCMatrix(matrix):
        c=[]
        for i in range(len(matrix)):
                tmp=[]
                for j in range(len(matrix)-1):
                        if(i==j):
                                c.append(0)
                        else:
                                c.append(-matrix[i][j]/matrix[i][i])
        return(c)
