import Problem
import Search

timeToLive = 100
numOfEmployedBees = 50
maxIteration = 1000

print("Bee Colony!")

problem = Problem.Problem(timeToLive)

abc = Search.Search()

abc.algorithm(problem, numOfEmployedBees, maxIteration)
