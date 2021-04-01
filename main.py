import random

def C2n(n):
    return n * (n-1) / 2


class CheckeredPageState:
    def __init__(self, checkeredPage):
        self.checkeredPage = checkeredPage
        self.rows = len(self.checkeredPage)
        self.columns = len(self.checkeredPage[0])
        self.setDic()
        self.setHeuristic()

    def setDic(self):
        dicRows = {}
        dicDiagonal1 = {}
        dicDiagonal2 = {}
        for i in range(self.rows):
            dicRows[i] = 0
            for j in range(self.columns):
                dicDiagonal1[i-j] = 0
                dicDiagonal2[i+j] = 0
        for i in range(self.rows):
            for j in range(self.columns):
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
        delta = float("inf")
        neighbors = []
        # for j in range(self.columns):
        #     for i in range(self.rows):
        #         if self.checkeredPage[i][j] == 1:
        #             deltaneg = self.dicRows[i]-1 + self.dicDiagonal1[i-j]-1 + self.dicDiagonal2[i+j]-1
        #             ikeep = i
        #             print(i)
        #             break
        #     for i in range(self.rows):
        #         if self.checkeredPage[i][j] == 0:
        #             deltaCurrent = self.dicRows[i] + self.dicDiagonal1[i-j] + self.dicDiagonal2[i+j] - deltaneg
        #             if deltaCurrent <= delta:
        #                 newCheckPage = self.checkeredPage.copy()
        #                 newCheckPage[i][j] = 1
        #                 newCheckPage[ikeep][j] = 0
        #                 newDicRows = self.dicRows
        #                 newDicRows[ikeep] -= 1
        #                 newDicRows[i] += 1
        #                 newDicDiagonal1 = self.dicDiagonal1
        #                 newDicDiagonal1[ikeep-j] -= 1
        #                 newDicDiagonal1[i-j] += 1
        #                 newDicDiagonal2 = self.dicDiagonal2
        #                 newDicDiagonal2[ikeep + j] -= 1
        #                 newDicDiagonal2[i + j] += 1
        #                 newNeighbor = CheckeredPageState(newCheckPage, newDicRows, newDicDiagonal1, newDicDiagonal2, self.h + deltaCurrent)
        #                 if deltaCurrent == delta:
        #                     neighbors.append(newNeighbor)
        #                 else:
        #                     delta = deltaCurrent
        #                     neighbors[:] = []
        #                     neighbors.append(newNeighbor)
        huristic = float("inf")
        for j in range(self.columns):
            for i in range(self.rows):
                if self.checkeredPage[i][j] == 1:
                    ikeep = i
                    break
            for i in range(self.rows):
                if self.checkeredPage[i][j] == 0:
                    newCheck = self.checkeredPage.copy()
                    newCheck[i][j] = 1
                    newCheck[ikeep][j] = 0
                    neighbor = CheckeredPageState(newCheck)
                    if neighbor.h < huristic:
                        neighbors[:] = []
                        huristic = neighbor.h
                    elif neighbor.h == huristic:
                        neighbors.append(neighbor)
        return(random.choice(neighbors))

    def getFirstChoice(self):
        for i in range(self.rows):
            for j in range(self.columns):
                'ji'


def HillCLimbingSteepestAscent(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    current.setDic()
    current.setHeuristic()
    print(current.dicRows)
    print(current.dicDiagonal1)
    print(current.dicDiagonal2)
    print(current.h)
    while 1:
        neighbor = current.getRandomSteepestAscent()
        print(neighbor.h)
        if neighbor.h >= current.h:
            if current.h == 0:
                print("the hill climbing algorithm found a solution")
            else:
                print("the hill climbing algorithm got stuck in local minimum")
            print(current.checkeredPage)
            return current
        print(neighbor.checkeredPage)
        current = neighbor

def HillCLimbingFirstChoice(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    while 1:
        neighbor = current.getFirstChoice()
        if neighbor is None:
            if current.h == 0:
                print("the hill climbing algorithm found a solution")
            else:
                print("the hill climbing algorithm got stuck in local minimum")
            print(current.checkeredPage)
            return current
        current = neighbor


check = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,0],
         [1,0,0,0,1,0,0,0],
         [0,1,0,0,0,1,0,1],
         [0,0,1,0,0,0,1,0],
         [0,0,0,0,0,0,0,0]]
HillCLimbingSteepestAscent(check)



