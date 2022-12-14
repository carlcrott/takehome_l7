import pandas as pd
import json


def parse(filename):
    """
    Example valid data:

    State   Town    7_2009  3   4   8.40188
    Alabama Abbeville   2930    3   10  3.94383
    Alabama Adamsville  4782    3   11  7.83099
    """

    ## Not generalized -- get it working first. Then genralize.
    df = pd.read_csv(filename, sep='\t')
    df[["State", "Town", "7_2009"]]

    output = df[["State", "Town", "7_2009"]].to_dict()

    return json.dumps(output)






