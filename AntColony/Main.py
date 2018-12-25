import AntColony

def main():

    print("Ant Colony!")
    antAssignment = AntColony.AntColony()
    antAssignment.initial()
    i = 0
    while i < 3:
        antAssignment.solve()
        i += 1

main()