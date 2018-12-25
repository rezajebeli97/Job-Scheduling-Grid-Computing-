import Problem
import Search

print("Tabu Search!")
problem = Problem.Problem()
search = Search.Search()
search.algorithm(problem, 5, 100, 0.01)