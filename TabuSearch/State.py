class State:
    solution = []

    def __init__(self, solution):
        self.solution = solution

    def print(self):
        s = "( "
        for i in self.solution:
            s += str(i) + "  "
        return s + ")"