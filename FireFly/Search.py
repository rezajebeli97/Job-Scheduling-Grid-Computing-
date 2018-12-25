class Search:

    def algorithm(self, problem, numOfFireFlies, maxIteration):
        bestCost = -10000000
        bestState = None

        fireFlies = problem.initialStates(numOfFireFlies)
        for state in fireFlies:
            cost = problem.f(state)
            if (cost > bestCost):
                bestCost = cost
                bestState = state

        for k in range(maxIteration):
            for i in range(len(fireFlies)):
                for j in range(i):
                    if problem.f(fireFlies[j]) > problem.f(fireFlies[i]):
                        s = fireFlies[i].movefireFly(fireFlies[j], problem)
                        fireFlies[i] = s

            for state in fireFlies:
                cost = problem.f(state)
                if (cost > bestCost):
                    bestCost = cost
                    bestState = state

        print(bestCost)
        print(bestState.print())