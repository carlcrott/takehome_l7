import json
import csv

DEBUG = False

def state_build(state, data):
    """
    DESIRED OUTPUT will be
    benfords_densities['Alabama'] = [100, 30, 24, 20, 15, 12, 10, 9, 7, 6]
    Corresponding to leading number [  1   2   3  4    5   6   7  8  9  0] 
    """

    ## build out the dataset with everything indexed to zero
    temp = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "0":0}

    print("############# "+ state)

    row_iter = 0

    # ['Alabama', 'Abbeville ', '2930', '3', '10', '3.94383']
    for row in data:
        if row[0] == state:
            popped_leading_int = str(row[2])[0]
            # print(popped_leading_int)
            # Increment the count for whatever the popped lead is
            temp[popped_leading_int] += 1

        if DEBUG:
            row_iter +=1
            if row_iter >= 50:
                return temp

    # print (temp)
    return temp


def map_state_to_integer_index(benfords_densities, list_of_states):
    ## Finally we need to rotate the data into the final format expected by highcharts.
    # Top level list -- will be 9 items long, corresponding to integers 1-9 and 0
    # within each theyll have a dict:
    # {name: 'Integer 1', data: [4, 4, 2, 4, 4, ... ]}, 
    # which is FIFTY items long
    # Ordered from Alabama to Wyoming
    # 'Wisconsin': {'1': 178,'2': 100,'3': 71,'4': 62,'5': 44,'6': 42,'7': 35,'8': 39,'9': 22,'0': 0},
    # 'Wyoming': {'1': 28,'2': 21,'3': 10,'4': 8,'5': 12,'6': 6,'7': 3,'8': 5,'9': 6,'0': 0},

    benfords_list = []

    for state in list_of_states:
        # print(benfords_densities[state])
        temp = []
        for x in range(10):
            temp.append(benfords_densities[state][str(x)])
        # pull the first value and stick at the end.
        # first_to_last = temp.pop(0)
        # temp.append(first_to_last)
        benfords_list.append(temp)


    # [76, 52, 33, 25, 22, 27, 13, 14, 19, 0],
    # [71, 41, 32, 20, 18, 18, 12, 9, 11, 0],
    # [178, 100, 71, 62, 44, 42, 35, 39, 22, 0],
    # [28, 21, 10, 8, 12, 6, 3, 5, 6, 0]]

    ## Start with the Alamaba  to Wyoming dataset for each of the benfords list
    # Integer zero starts with benfords_list[0] aka Alambama and ends with benfords_list[50] Wyoming
    leading_integer_sorted = [[0 for i in range(50)] for j in range(10)]
    # leading_integer_sorted[0] = [0..50]
    # leading_integer_sorted[1] = [0..50]

    # iterate BY integer
    for x in range(10):
        leading_integer_sorted[x] = []
        # THEN populate each state
        for state in benfords_list:
            leading_integer_sorted[x].append(state[x])


    
    # Final data format for highcharts
    highcharts_ingest_data = []
    for x in range(10):
        temp_dict = {}
        temp_dict['name'] = 'Integer '+str(x)
        temp_dict['data'] = leading_integer_sorted[x]

        highcharts_ingest_data.append(temp_dict)

    return highcharts_ingest_data






def parse(filename):
    """
    Example valid data:

    State   Town    7_2009  3   4   8.40188
    Alabama Abbeville   2930    3   10  3.94383
    Alabama Adamsville  4782    3   11  7.83099
    """

    ## Preprocessing Im just throwing out anything thats not 6 column.
    preprocessed_data = []
    census_raw = open(filename,'r')
    reader = csv.reader(census_raw, delimiter='\t')

    for row in reader:
        if len(row) == 6:
            preprocessed_data.append(row)

    data_cols = preprocessed_data.pop(0)
    

    list_of_states = []

    benfords_densities = {}
    malformed_count = 0
    ## ~~~~ NON ALGORITHMICALLY OPTIMIZED ~~~~
    # Prototyping > Performance
    for row in preprocessed_data:
        print(row)

        ## If its malformed, ignore it.
        if len(row) != 6:
            malformed_count += 1
            continue

        if row[0] not in list_of_states:
            list_of_states.append(row[0])

    for state in list_of_states:
        benfords_densities[state] = state_build(state, preprocessed_data)


    highcharts_ingest_data = map_state_to_integer_index(benfords_densities, list_of_states)


    return list_of_states, highcharts_ingest_data



# parse(filename)

## quick sanity check
# benfords_densities['Alabama']
# benfords_densities['Texas']
# benfords_densities['Wyoming']








