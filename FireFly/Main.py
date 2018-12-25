import Problem
import Search

numOfFireFlies = 50
maxIteration = 100

print("FireFlies!")

problem = Problem.Problem()

abc = Search.Search()

abc.algorithm(problem, numOfFireFlies, maxIteration)
