#US Population Challenge - www.101computing.net/us-population/
def main():
    #Open text file in read mode
    file = open("Homework folder/US Pop/USStates.txt","r")
    total = 0
    lowest_pop = -1
    highest_pop = -1
    count = 0
    #Loop through the text file, line by line.
    for line in file:
        stateFields = line.split(",")
        population=int(stateFields[2][:-1])
        total += population
        if lowest_pop == -1 or lowest_pop > population:
            lowest_pop = population
        if highest_pop == -1 or highest_pop < population:
            highest_pop = population
        count += 1
    file.close()
    print(f"""Total Population = {total},
    Average Population = {total/count},
    Lowest Population = {lowest_pop},
    Highest Population = {highest_pop}""")
    file = open("Homework folder/US Pop/USStates.txt", "r")
    for line in file:
        stateFields = line.split(",")
        state=stateFields[0]
        code=stateFields[1]
        #For the last field we remove the last character (carriage return) and cast to an integer
        population=int(stateFields[2][:-1])
        pop_percent = (population/total)*100
        print(state + " (" + code + "): " + str(population) + ", percentage of full population: "+ str(round(pop_percent, 2))+ "%")
    file.close()


main()