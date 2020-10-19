organisms = int(input("How many organisms are there?: "))
growth = int(input("At what rate are the organisms growing?: "))
hours = int(input("How many hours will it take to achieve the growth rate?: "))
period = int(input("How many hours are you recording the growth cycle?: "))
iterations = period // hours

for eachPass in [iterations]:
    organisms = organisms * growth * iterations
    print("The population will be:", organisms, "in", period, "hours.")
