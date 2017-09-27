################################################################
#                                                              #
#   This Python Script uses Genetic Algorithm to generarte a   #
#   string which is choosen by the user.                       #
#                                                              #
#   The Result is also plotted using the Matplotlib library    #
#   pyplot class                                               #
#                                                              #
#   Still Working on few more things such as incorporating     #
#   any character. Stay Tuned.                                 #
#   Version v1.0                                               #
#   Made by Ishaan Kohli                                       #
################################################################

################################################################
##################ImportingLibraries############################
################################################################

import random
import string
from copy import deepcopy
import matplotlib.pyplot as plt


################################################################
########################INPUTSTRING#############################
inp_str="Inputyourstringhere"
######################ChromosomeArraySize#######################
D=len(inp_str)

################################################################

######################MutationRate##############################
MR=0.5
######################CrossoverRate#############################
CR=0.5


###################SavingGlobalbestfitness######################
bestfitness=-1
beststring=""

#######################PopulationParameters#####################
popsize=10
pop=[]

##################AllBestFitnessForGraph########################
best_fit=[]
best_fitind=[]




class searchstring:
    def __init__(self,s,f):
        self.s=s
        self.f=f
        

def fitnessfunction(s):
    fit=0
    for i in range(D):
        if s[i]==inp_str[i]:
            fit=fit+1
    return fit

def crossover():
    for i in range(popsize):
        if random.random()<=CR:
            i1,i2=random.sample(range(0,popsize-1),2)
            
            p1=deepcopy(pop[i1].s)
            p2=deepcopy(pop[i2].s)
            
            pt=random.randint(1,D-2)
            
            c1=p1[:pt]+p2[pt:]
            c2=p2[:pt]+p1[pt:]
            
            c1fitness=fitnessfunction(c1)
            c2fitness=fitnessfunction(c2)
            
            if c1fitness>pop[i1].f:
                pop[i1].s=c1
                pop[i1].f=c1fitness
                
            if c2fitness>pop[i2].f:
                pop[i2].s=c2
                pop[i2].f=c2fitness
                
def mutation():
    for i in range(popsize):
        if random.random()<=MR:
            r=random.randint(0,popsize-1)
            p1=deepcopy(pop[r])
            
            i1=random.randint(0,D-1)
            c1=deepcopy(p1.s)
            c1=c1[:i1]+"".join(random.sample(string.ascii_letters,1))+c1[i1+1:]
            
            c1fitness=fitnessfunction(c1)
            
            if c1fitness>p1.f:
                pop[r].s=c1
                pop[r].f=c1fitness
            
            
                
def globalbest():
    global bestfitness, beststring
    for i in range(popsize):
        if pop[i].f>bestfitness:
            bestfitness=pop[i].f
            beststring=pop[i].s
        
            
            
def init():
    for i in range(popsize):
        strg="".join(random.sample(string.ascii_letters,D))
        fitness=fitnessfunction(strg)
        obj=searchstring(strg,fitness)
        pop.append(obj)
    


init()

globalbest()

print(beststring)

best_fit.append(bestfitness/D)
best_fitind.append(0)
count=0

for i in range(10000):
    crossover()
    mutation()
    globalbest()
    
    best_fit.append(bestfitness/D)
    best_fitind.append(i+1)
    if bestfitness==D:
        print(beststring,count)
        break
    print(beststring,bestfitness/D)
    count=count+1
    
print()


#print(best_fit)
#print(best_fitind)



plt.scatter(best_fitind,best_fit,color="red")
plt.plot(best_fitind,best_fit, color = 'blue')
plt.show()   