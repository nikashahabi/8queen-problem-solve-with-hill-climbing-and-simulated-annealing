def C2n(n):
    return n * (n-1) / 2


class checkeredPageState:
    def __init__(self, checkeredPage):
        self.checkeredPage = checkeredPage
    def heuristic(self):
        rows = len(self.checkeredPage)
        columns = len(self.checkeredPage[0])
        dicRows = {}
        dicColumns = {}
        dicDiagnal = {}
        for i in range(rows):
            for j in range(columns):
                if self.checkeredPage[i][j]:
                    if i in dicRows:
                        dicRows[i] = dicRows[i] + 1
                    else:
                        dicRows[i] = 1
                    if j in dicColumns:
                        dicColumns[j] = dicColumns[j] + 1
                    else:
                        dicColumns[j] = 1
                    k = i - j
                    if k in dicDiagnal:
                        dicDiagnal[k] = dicDiagnal[k] + 1
                    else:
                        dicDiagnal[k] = 1
        h = 0
        for key in dicRows:
            h = h + C2n(dicRows[key])
        for key in dicColumns:
            h = h + C2n(dicColumns[key])
        for key in dicDiagnal:
            h = h + C2n(dicDiagnal[key])
        return h





def HillCLimbingSteepestAscent(checkeredPage):
    while 1:
        
