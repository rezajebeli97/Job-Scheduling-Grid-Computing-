class Ant:

    solution = []

    def __init__(self, numOfJobs , numOfClusters):
        self.solution = [numOfClusters] * numOfJobs

    def canAssign(self, jobIndex , job, cluster , jobs):
        freeCore = cluster.core
        for i in range(0, jobIndex):
            if self.solution[i] == cluster.id:
                freeCore -= jobs[i].core

        freeRam = cluster.ram
        for i in range(0, jobIndex):
            if self.solution[i] == cluster.id:
                freeRam -= jobs[i].ram

        if freeCore >= job.core and freeRam >= job.ram:
            return True
        return False