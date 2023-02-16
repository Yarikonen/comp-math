from IOHandler import greeting,answ, inputInfo,notConverges
from logic import isSolutionConverge,solution
greeting()
inp = inputInfo()
matrix=inp[0]
epsillon=inp[1]

if(isSolutionConverge(matrix)):
        sol = solution(matrix,[matrix[i][len(matrix)]/matrix[i][i] for i in range(len(matrix))],epsillon,1)
        answ(sol)
else:
        notConverges()

        
