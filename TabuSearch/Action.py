class Action:
    def __init__(self, jobIndex, clusterIndex, cost):
        self.jobIndex = jobIndex
        self.clusterIndex = clusterIndex
        self.cost = cost

    def print(self):
        return "( job[" + str(self.jobIndex) + "] -> cluster[" + str(self.clusterIndex) + "] )"