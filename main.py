import random
import copy
import math

def C2n(n):
    return n * (n-1) / 2


class CheckeredPageState:

    def __init__(self, checkeredPage):
        self.checkeredPage = checkeredPage
        self.dimension = len(self.checkeredPage)
        self.setDic()
        self.setHeuristic()

    def setDic(self):
        dicRows = {}
        dicDiagonal1 = {}
        dicDiagonal2 = {}
        for i in range(self.dimension):
            dicRows[i] = 0
            for j in range(self.dimension):
                dicDiagonal1[i-j] = 0
                dicDiagonal2[i+j] = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.checkeredPage[i][j]:
                    dicRows[i] += 1
                    dicDiagonal1[i-j] += 1
                    dicDiagonal2[j+i] += 1
        self.dicRows = dicRows
        self.dicDiagonal1 = dicDiagonal1
        self.dicDiagonal2 = dicDiagonal2

    def setHeuristic(self):
        h = 0
        for key in self.dicRows:
            if self.dicRows[key] > 1:
                h += C2n(self.dicRows[key])
        for key in self.dicDiagonal1:
            if self.dicDiagonal1[key] > 1:
                h += C2n(self.dicDiagonal1[key])
        for key in self.dicDiagonal2:
            if self.dicDiagonal2[key] > 1:
                h += C2n(self.dicDiagonal2[key])
        self.h = h

    def getRandomSteepestAscent(self):
        neighbors = []
        huristic = float("inf")
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 1:
                    ikeep = i
                    break
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 0:
                    newCheck = copy.deepcopy(self.checkeredPage)
                    newCheck[i][j] = 1
                    newCheck[ikeep][j] = 0
                    neighbor = CheckeredPageState(newCheck)
                    if neighbor.h < huristic:
                        neighbors[:] = []
                        huristic = neighbor.h
                    if neighbor.h == huristic:
                        neighbors.append(neighbor)
        return(random.choice(neighbors))

    def getFirstChoice(self):
        test = [[False for i in range(self.dimension)] for j in range(self.dimension)]
        while 1:
            i = random.randrange(0, self.dimension)
            j = random.randrange(0, self.dimension)
            test[i][j] = True
            newCheck = copy.deepcopy(self.checkeredPage)
            newCheck[i][j] = 1
            for k in range(self.dimension):
                if self.checkeredPage[k][j]:
                    ikeep = k
                    break
            newCheck[ikeep][j] = 0
            newCheck[i][j] = 1
            neighbor = CheckeredPageState(newCheck)
            if neighbor.h < self.h:
                return neighbor
            flag = True
            'checks if we have randomly generated all the successors'
            for x in test:
                for y in x:
                    if y is False:
                        flag = False
                        break
                if flag is False:
                    break
            if flag is True:
                return None

    def printPage(self):
        for xs in self.checkeredPage:
            print(" ".join(map(str, xs)))

    def getMove(self, neighbor):
        test = False
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] != neighbor.checkeredPage[i][j]:
                    if self.checkeredPage[i][j] == 1:
                        istart = i
                    else:
                        iend = i
                    if test is False:
                        test = True
                    else:
                        print("move in column "+ str(j+1) + " from row " + str(istart+1) + " to " + str(iend+1))
                        break

    def randomSuccessor(self):
        j = random.randrange(0, self.dimension)
        while 1:
            i = random.randrange(0, self.dimension)
            if self.checkeredPage[i][j] != 1:
                break
        for k in range(self.dimension):
            if self.checkeredPage[k][j]:
                break
        newCheckeredPage = copy.deepcopy(self.checkeredPage)
        newCheckeredPage[i][j] = 1
        newCheckeredPage[k][j] = 0
        return CheckeredPageState(newCheckeredPage)


def HillCLimbingSteepestAscent(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    while 1:
        print("current state checkered page:")
        current.printPage()
        print("current state h:", current.h)
        neighbor = current.getRandomSteepestAscent()
        if neighbor.h >= current.h:
            if current.h == 0:
                print("the hill climbing algorithm steepest ascent variant found a solution")
                return True, current
            else:
                print("the hill climbing algorithm steepest ascent variant got stuck in local minimum")
                return False, current
        current.getMove(neighbor)
        current = neighbor

def HillCLimbingFirstChoice(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    while 1:
        print("current state checkered page:")
        current.printPage()
        print("current state h:", current.h)
        neighbor = current.getFirstChoice()
        if neighbor is None:
            if current.h == 0:
                print("the hill climbing algorithm first choice variant found a solution")
                return True, current
            else:
                print("the hill climbing algorithm first choice variant got stuck in local minimum")
                return False, current
        current.getMove(neighbor)
        current = neighbor


def getRandomCheckeredPage(dimension):
    checkeredPage = [[0 for i in range(dimension)] for j in range(dimension)]
    randNumbers = random.sample(range(0, dimension), dimension)
    for j in range(dimension):
        checkeredPage[randNumbers[j]][j] = 1
    return checkeredPage

def HillClimbingRandomRestart(dimension):
    while 1:
        print("-----------------------------------")
        print("new start of hill climbing algorithm with random restart")
        checkeredPage = getRandomCheckeredPage(dimension)
        boolean, state = HillCLimbingSteepestAscent(checkeredPage)
        if boolean:
            print("the hill climbing algorithm with random restart ended")
            return state

def SimulatedAnnealing(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    T = 4000
    while 1:
        T *= 0.99
        if T < 0.0001:
            print("final state checkered page:")
            current.printPage()
            print("final state h:", current.h)
            if current.h == 0:
                print("the simulated annealing found a solution")
                return True, current
            else:
                print("the simulated annealing could not find the solution")
                return False, current
        next = current.randomSuccessor()
        deltaE = current.h - next.h
        if deltaE > 0:
            current = next
        else:
            rand = random.uniform(0, 1)
            probability = math.exp(deltaE / T)
            if rand <= probability:
                current = next


check = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,0],
         [1,0,0,0,1,0,0,0],
         [0,1,0,0,0,1,0,1],
         [0,0,1,0,0,0,1,0],
         [0,0,0,0,0,0,0,0]]

SimulatedAnnealing(check)



