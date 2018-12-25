import random

class State:

    solution = []

    def __init__(self, solution):
        self.solution = solution

    def print(self):
        s = "( "
        for i in self.solution:
            s += str(i) + "  "
        return s + ")"

    def movefireFly(self, state, problem):
        solution2 = state.solution
        childSolution = [0] * len(self.solution)
        for i in range(len(self.solution)):
            if (self.solution[i] == solution2[i]):
                rand = random.random()
                if (rand < 0.9):
                    childSolution = problem.assign(childSolution, i, self.solution[i])
                else:
                    childSolution = problem.assign(childSolution, i, (int) (random.random() * (len(problem.clusters) )))

            else:
                rand = random.random()
                if (rand < 0.3):
                    childSolution = problem.assign(childSolution, i, self.solution[i])

                elif (rand < 0.75):
                    childSolution = problem.assign(childSolution, i, solution2[i])

                else:
                    childSolution = problem.assign(childSolution, i, (int) (random.random() * len(problem.clusters)))

        return State(childSolution)



