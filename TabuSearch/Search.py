from builtins import print


class Search:

    def algorithm(self, problem, tabuTenure, maxIteration, k):
        p = problem.initialState()
        myPath = []
        myActions = []
        best = p
        bestWorth = problem.f(p)
        tabu = [0] * len(p.solution)
        frequency = [0] * len(p.solution)
        myPath.append(p)
        observedNodes = 1
        extendedNodes = 0
        while maxIteration > 0:
            maxIteration -= 1
            actions = problem.actions(p)
            bestNeighbour = p
            bestAction = None
            maxCostFrequency = 0
            for i in range(len(actions)):
                neighbour = problem.result(p, actions[i])
                if problem.contains(myPath, neighbour):
                    continue
                neighbourWorth = problem.f(neighbour)
                neighbourWorthFrequency = neighbourWorth - k * frequency[actions[i].jobIndex]
                observedNodes += 1
                if (tabu[actions[i].jobIndex] > 0 and neighbourWorth <= problem.f(best)):
                    continue
                if (neighbourWorthFrequency > maxCostFrequency):
                    maxCostFrequency = neighbourWorthFrequency
                    bestNeighbour = neighbour
                    bestAction = actions[i]

            if (bestNeighbour == p):
                break

            p = bestNeighbour
            tabu[bestAction.jobIndex] = tabuTenure
            for i in range(len(tabu)):
                if (tabu[i] > 0):
                    tabu[i]-= 1
            frequency[bestAction.jobIndex] += 1
            extendedNodes += 1
            if problem.f(bestNeighbour) > bestWorth:
                best = bestNeighbour
                bestWorth = problem.f(bestNeighbour)

            myPath.append(bestNeighbour)
            myActions.append(bestAction)

        self.printDetailsHillClimbing(problem, observedNodes, extendedNodes, myPath, myActions, best)

    def printDetailsHillClimbing(self, problem, observedNodes, extendedNodes, myPath, myActions, best):
        print("Number of observed nodes : " + str(observedNodes))
        print("Number of extended nodes : " + str(extendedNodes))
        cost = 0
        for action in myActions:
            cost += action.cost
        print("Path cost : " + str(cost))
        print("Final state worth : " + str(problem.f(best)))
        print("Final Answer : " + best.print())