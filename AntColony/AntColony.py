import Cluster
import Job
import Ant
import random

class AntColony:
    pheremoneInitialVal = 2
    maxIterations = 100
    currentJob = 0
    numOfAnts = 4
    ants = []
    bestSolution = []
    bestTourCost = 0
    clusters = []
    jobs = []
    heuristic = []
    pheromone = []

    def initial(self):

        job0 = Job.Job(0, 120, 1)
        job1 = Job.Job(1, 120, 1)
        job2 = Job.Job(2, 120, 1)
        job3 = Job.Job(3, 120, 1)
        job4 = Job.Job(4, 120, 1)
        job5 = Job.Job(5, 120, 1)
        job6 = Job.Job(6, 120, 1)
        job7 = Job.Job(7, 120, 1)
        job8 = Job.Job(8, 120, 1)
        job9 = Job.Job(9, 120, 1)

        job10 = Job.Job(10, 150, 1)
        job11 = Job.Job(11, 150, 1)
        job12 = Job.Job(12, 150, 1)
        job13 = Job.Job(13, 150, 1)
        job14 = Job.Job(14, 150, 1)
        job15 = Job.Job(15, 150, 1)
        job16 = Job.Job(16, 150, 1)
        job17 = Job.Job(17, 150, 1)
        job18 = Job.Job(18, 150, 1)
        job19 = Job.Job(19, 150, 1)

        job20 = Job.Job(20, 170, 1)
        job21 = Job.Job(21, 170, 1)
        job22 = Job.Job(22, 170, 1)
        job23 = Job.Job(23, 170, 1)
        job24 = Job.Job(24, 170, 1)
        job25 = Job.Job(25, 170, 1)
        job26 = Job.Job(26, 170, 1)
        job27 = Job.Job(27, 170, 1)
        job28 = Job.Job(28, 170, 1)
        job29 = Job.Job(29, 170, 1)

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


        cluster0 = Cluster.Cluster(0, 1000, 64)
        cluster1 = Cluster.Cluster(1, 1000, 64)
        cluster2 = Cluster.Cluster(2, 1000, 64)
        cluster3 = Cluster.Cluster(3, 1000, 64)
        cluster4 = Cluster.Cluster(4, 1000, 64)

        self.clusters.append(cluster0)
        self.clusters.append(cluster1)
        self.clusters.append(cluster2)
        self.clusters.append(cluster3)
        self.clusters.append(cluster4)

        self.n =  len(self.jobs)
        self.m = len(self.clusters)

        self.bestSolution = [None] * self.n

        self.heuristic = [[None] * (self.m+1)] * self.n
        for i in range(self.n):
            for j in range(self.m):
                self.heuristic[i][j] = 2

        for i in range(self.n):
            self.heuristic[i][self.m] = 0.1

        self.pheromone = [[None] * (self.m+1)] * self.n
        for i in range(self.n):
            for j in range(self.m+1):
                self.pheromone[i][j] = self.pheremoneInitialVal

        for i in range(self.numOfAnts):
            self.ants.append(Ant.Ant(self.n, self.m))


    def solve(self):
        for i in range(self.n):
            for j in range(self.m+1):
                self.pheromone[i][j] = self.pheremoneInitialVal

        iteration = 0

        while iteration < self.maxIterations:
            self.setupAnts()
            self.moveAnts()
            self.updateTrails()
            iteration += 1

        print( "Best Solution Cost: " + str(self.bestTourCost) )
        print( "Best Solution: " + self.tourToString(self.bestSolution) + "\n" )

    def setupAnts(self):
        self.currentJob = -1
        for i in range(self.numOfAnts):
            index = int(random.random() * (len(self.clusters) + 1))		#clusters.length shows that job doesn't assign to any cluster
            while index < len(self.clusters) and not(self.ants[i].canAssign(0, self.jobs[0], self.clusters[index], self.jobs)):
                index += 1
                if index >= len(self.clusters):
                    index -= len(self.clusters)
                    index -= 1

            self.ants[i].solution[0] = index
        self.currentJob += 1

    def moveAnts(self):
        for self.currentJob in range(1, len(self.jobs)):
            for a in self.ants:
                clusterIndex = self.assignJob(a)     #check kon bbin mishe hamishe assign kard in job ro ya momkene gheyre ghabele ghabool ham bede va inke momkene -1 ham khorooji bede?
                a.solution[self.currentJob] = clusterIndex

    def assignJob(self , ant):
        pr = 0.2
        # sometimes just randomly select
        if (random.random() < pr):
            clusterIndex = int(random.random() * (len(self.clusters) + 1));
            while (clusterIndex < len(self.clusters) and not(ant.canAssign( self.currentJob, self.jobs[self.currentJob], self.clusters[clusterIndex], self.jobs))):
                clusterIndex+=1
            return clusterIndex

        # randomly select according to probs
        probs = self.probTo(ant)
        r = random.random()
        tot = 0

        for i in range(len(self.clusters) + 1):
            tot += probs[i]
            if (tot >= r):
                return i

        print("Not supposed to get here.")

    def probTo(self, ant):
        probs = [None] * (len(self.clusters) + 1)

        alpha = 3
        beta = 1

        denom = 0.0

        for i in range(len(self.clusters) + 1):
            if i == len(self.clusters) or ant.canAssign(self.currentJob, self.jobs[self.currentJob], self.clusters[i], self.jobs):
                denom += (self.pheromone[self.currentJob][i]**alpha) * (self.heuristic[self.currentJob][i]**beta)

        for i in range(len(self.clusters) + 1):
            if i < len(self.clusters) and not(ant.canAssign( self.currentJob, self.jobs[self.currentJob], self.clusters[i], self.jobs)):
                probs[i] = 0.0
            else:
                numerator = (self.pheromone[self.currentJob][i]**alpha) * (self.heuristic[self.currentJob][i]**beta)
                probs[i] = numerator / denom        #probs[j] means propability of assign jobs[currentJob] to cluster j

        return probs

    def updateTrails(self):
        #divided by 2 each path
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone[0])):
                self.pheromone[i][j] /= 2

        for ant in self.ants:
            cost = self.cost(ant)
            for jobIndex in range(len(ant.solution)):
                clusterIndex = ant.solution[jobIndex]
                self.pheromone[jobIndex][clusterIndex] += cost
            if (cost > self.bestTourCost):
                self.bestTourCost = cost
                for i in range(len(ant.solution)):
                    self.bestSolution[i] = ant.solution[i]

    def cost(self, ant):
        solution = ant.solution
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


    def tourToString(self, array):
        s = "";
        for i in range(len(array)):
            s += "job[" + str(i) + "] -> " + str(array[i]) + "\t"
        return s