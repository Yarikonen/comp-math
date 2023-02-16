from IOHandler import inputFromCMD,greeting,answ, inputInfo,notConverges
from logic import isSolutionConverge,solution
greeting()
inp = inputInfo()
matrix=inp[0]
epsillon=inp[1]

if(isSolutionConverge(matrix)):
        sol = solution(matrix,[1.2,1.3,1.4],epsillon,0)
        answ(sol)
else:
        notConverges()

        
