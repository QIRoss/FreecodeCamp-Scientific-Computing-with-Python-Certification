import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        if kwargs is not None:
            for key,value in kwargs.items():
                for i in range(value):
                    self.contents.append(key)
    
    def draw(self,numToDraw):
        res = []
        if numToDraw >= len(self.contents):
            return self.contents
        for i in range(numToDraw):
            sorted = random.randrange(0,len(self.contents))
            res.append(self.contents[sorted])
            del self.contents[sorted]
        return res
#----------------------------------------------------------------------
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        testHat = copy.deepcopy(hat)
        individualTestResult = testHat.draw(num_balls_drawn)
        def isTestSuccessful(sampleList, sampleObject):
            for key,value in sampleObject.items():
                if sampleList.count(key) < value:
                    return False
            return True
        if isTestSuccessful(individualTestResult, expected_balls) == True:
            M += 1

    return M / num_experiments
#----------------------------------------------------------------------