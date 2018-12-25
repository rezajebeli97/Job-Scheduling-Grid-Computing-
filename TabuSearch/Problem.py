import Action
import random
import State


class Problem:
    clusters = []
    jobs = []

    def __init__(self):

        job0 = Job(0, 120, 1)
        job1 = Job(1, 120, 1)
        job2 = Job(2, 120, 1)
        job3 = Job(3, 120, 1)
        job4 = Job(4, 120, 1)
        job5 = Job(5, 120, 1)
        job6 = Job(6, 120, 1)
        job7 = Job(7, 120, 1)
        job8 = Job(8, 120, 1)
        job9 = Job(9, 120, 1)

        job10 = Job(10, 150, 1)
        job11 = Job(11, 150, 1)
        job12 = Job(12, 150, 1)
        job13 = Job(13, 150, 1)
        job14 = Job(14, 150, 1)
        job15 = Job(15, 150, 1)
        job16 = Job(16, 150, 1)
        job17 = Job(17, 150, 1)
        job18 = Job(18, 150, 1)
        job19 = Job(19, 150, 1)

        job20 = Job(20, 170, 1)
        job21 = Job(21, 170, 1)
        job22 = Job(22, 170, 1)
        job23 = Job(23, 170, 1)
        job24 = Job(24, 170, 1)
        job25 = Job(25, 170, 1)
        job26 = Job(26, 170, 1)
        job27 = Job(27, 170, 1)
        job28 = Job(28, 170, 1)
        job29 = Job(29, 170, 1)

        self.jobs.append(job0)
        self.jobs.append(job1)
        self.jobs.append(job2)
        self.jobs.append(job3)
        self.jobs.append(job4)
        self.jobs.append(job5)
        self.jobs.append(job6)
        self.jobs.append(job7)
        self.jobs.append(job8)
        self.jobs.append(job9)
        self.jobs.append(job10)
        self.jobs.append(job11)
        self.jobs.append(job12)
        self.jobs.append(job13)
        self.jobs.append(job14)
        self.jobs.append(job15)
        self.jobs.append(job16)
        self.jobs.append(job17)
        self.jobs.append(job18)
        self.jobs.append(job19)
        self.jobs.append(job20)
        self.jobs.append(job21)
        self.jobs.append(job22)
        self.jobs.append(job23)
        self.jobs.append(job24)
        self.jobs.append(job25)
        self.jobs.append(job26)
        self.jobs.append(job27)
        self.jobs.append(job28)
        self.jobs.append(job29)

        cluster0 = Cluster(0, 1000, 64)
        cluster1 = Cluster(1, 1000, 64)
        cluster2 = Cluster(2, 1000, 64)
        cluster3 = Cluster(3, 1000, 64)
        cluster4 = Cluster(4, 1000, 64)

        self.clusters.append(cluster0)
        self.clusters.append(cluster1)
        self.clusters.append(cluster2)
        self.clusters.append(cluster3)
        self.clusters.append(cluster4)

    def f(self, state):
        solution = state.solution
        clustersUtil_core = [0] * len(self.clusters)
        clustersUtil_ram = [0] * len(self.clusters)

        for i in range(len(solution)):
            clusterIndex = solution[i]
            if (clusterIndex == len(self.clusters)):
                continue
            clustersUtil_core[clusterIndex] += self.jobs[i].core
            clustersUtil_ram[clusterIndex] += self.jobs[i].ram

        for i in range(len(self.clusters)):
            clustersUtil_core[i] /= self.clusters[i].core
            clustersUtil_ram[i] /= self.clusters[i].ram

        cost_core = 0
        for i in range(len(self.clusters)):
            cost_core += clustersUtil_core[i] ** 2

        cost_ram = 0
        for i in range(len(self.clusters)):
            cost_ram += clustersUtil_ram[i] ** 2

        return cost_core

    def equal(self, s1, s2):
        solution1 = s1.solution
        solution2 = s2.solution
        for i in range(len(solution1)):
            if (solution1[i] != solution2[i]):
                return False
        return True

    def actions(self, state):
        actions = []
        for i in range(len(self.jobs)):
            for j in range(len(self.clusters)):
                if state.solution[i] == j:
                    continue
                remainedCore = self.clusters[j].core
                remainedRam = self.clusters[j].ram
                for k in range(len(self.jobs)):
                    if state.solution[k] == j:
                        remainedCore -= self.jobs[k].core
                        remainedRam -= self.jobs[k].ram

                if remainedCore >= self.jobs[i].core and remainedRam >= self.jobs[i].ram:
                    actions.append(Action.Action(i, j, 1))
        return actions

    def result(self, state, action):
        solution = [0] * len(self.jobs)
        for i in range(len(solution)):
            solution[i] = state.solution[i]
        solution[action.jobIndex] = action.clusterIndex
        return State.State(solution)

    def contains(self, myPath, neighbour):
        for state in myPath:
            if (self.equal(state, neighbour)):
                return True
        return False

    def initialState(self):
        solution = [0] * len(self.jobs)
        i = 0
        while i < len(solution):
            clusterIndex = (int)(random.random() * len(self.clusters))
            remainedCore = self.clusters[clusterIndex].core
            remainedRam = self.clusters[clusterIndex].ram
            for j in range(i):
                if (solution[j] == clusterIndex):
                    remainedCore -= self.jobs[j].core
                    remainedRam -= self.jobs[j].ram
            if (remainedCore >= self.jobs[i].core and remainedRam >= self.jobs[i].ram):
                solution[i] = clusterIndex
            else:
                i -= 1
            i += 1
        return State.State(solution)


class Cluster:
    def __init__(self,id, core, ram):
        self.id = id
        self.core = core
        self.ram = ram


class Job:
    def __init__(self,id, core, ram):
        self.id = id
        self.core = core
        self.ram = ram
