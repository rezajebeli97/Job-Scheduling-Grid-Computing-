

class Search:

    def algorithm(self, problem, numOfEmployedBees, maxIteration):
        bestCost = -10000000
        bestState = None
        employedBees = problem.initialStates(numOfEmployedBees)

        for state in employedBees:
            cost = problem.f(state)
            if (cost > bestCost):
                bestCost = cost
                bestState = state

        for i in range(maxIteration):
            empBeeNumBefore = len(employedBees)
            employedBees = problem.nextStates(employedBees)
            empBeeNumAfter = len(employedBees)
            scoutBees = empBeeNumAfter - empBeeNumBefore
            for j in range(scoutBees):
                employedBees.add(problem.randomState())

            for state in employedBees:
                cost = problem.f(state)
                if (cost > bestCost):
                    bestCost = cost
                    bestState = state

        print(bestCost)
        print(bestState.print())