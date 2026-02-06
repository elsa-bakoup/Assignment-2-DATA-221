#Question 6
import pandas as pd
import numpy as np

with (open(file= 'crime.csv', mode = 'r') as file):
    df = pd.read_csv('crime.csv')          #creating a dataframe with the file

    df['Risk'] = np.where(df['ViolentCrimesPerPop'] >= 0.5, 'High-Crime', 'LowCrime')   #creating a new column with specific conditions

    #creating a new data frame with the data grouped depending on the criminality
    grouped_data = (
        df.groupby("Risk")
        .agg(
            Unemployement=("PctUnemployed", "mean"),   #computing the average of PctUnemployed and adding the values to the data frame
        )
    )

    print(grouped_data)