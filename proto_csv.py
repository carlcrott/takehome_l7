import pandas as pd
import json
import csv


def state_build(state, df):
    """
    DESIRED OUTPUT will be
    benfords_densities['Alabama'] = [100, 30, 24, 20, 15, 12, 10, 9, 7, 6]
    Corresponding to leading number [  1   2   3  4    5   6   7  8  9  0] 
    """

    ## build out the dataset with everything indexed to zero
    temp = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "0":0}

    print("############# "+ state)

    for index, row in df[["State", "Town", "7_2009"]].iterrows():
        if len 

        if row['State'] == state:
            popped_leading_int = str(row['7_2009'])[0]
            # print(popped_leading_int)
            # print("--------")


            # Increment the count for whatever the popped lead is
            temp[popped_leading_int] += 1


    print (temp)
    return temp



filename = 'census_2009b.csv'
filename = 'census_clean.csv'
def parse(filename):
    """
    Example valid data:

    State   Town    7_2009  3   4   8.40188
    Alabama Abbeville   2930    3   10  3.94383
    Alabama Adamsville  4782    3   11  7.83099
    """

    ## preprocessing Im just throwing out anything thats not 6 column.
    preprocessed_data = []
    census_raw = open(filename,'r')
    reader = csv.reader(census_raw, delimiter='\t')

    for row in reader:
        if len(row) == 6:
            preprocessed_data.append(row)

    df = pd.DataFrame(preprocessed_data)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    # df[["State", "Town", "7_2009"]]


    state_indexed = {}
    # Alabama Abbeville   2930    3   10  3.94383
    # Alabama Adamsville  4782    3   11  7.83099
    # state_indexed['Alabama'][town] = population


    list_of_states = []
    benfords_densities = {}

    ## ~~~~ NON ALGORITHMICALLY OPTIMIZED ~~~~
    # I do not care.  
    # Prototyping > Performance
    malformed_count = 0

    for index, row in df[["State", "Town", "7_2009"]].iterrows():
        # Build the list of states
        row = list(row)

        ## If its malformed, ignore it.
        if len(row) != 3:
            print("MALFORMED:")
            print(row)
            malformed_count += 1
            continue

        if row[0] not in list_of_states:
            list_of_states.append(row[0])

    for state in list_of_states:
        benfords_densities[state] = state_build(state, df)


    

parse(filename)

## quick sanity check
# benfords_densities['Alabama']
# benfords_densities['Texas']
# benfords_densities['Wyoming']




"""
THE INDIVIDUAL dicts in this series 
... will each be 50 items long and be Alabama through Wyoming
... and there will be 9 series of data.
*/

//     series: [{
//         name: 'Integer 1',
//         data: [4, 4, 2, 4, 4]
//     }, {
//         name: 'Integer 2',
//         data: [0, 4, 3, 2, 3]
//     }, {
//         name: 'Integer 3',
//         data: [1, 2, 2, 1, 2]
//     }]
// });

"""




        if state_indexed
        print("------")

    return json.dumps(output)






