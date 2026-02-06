#Question 5
import pandas as pd
import numpy as np

with (open(file='student.csv', mode='r') as file):
    df = pd.read_csv('student.csv')    #converting the file to a dataframe

    df['grade_band'] = np.select(
        [df['grade'] >= 15, (df['grade'] >= 10) & (df['grade'] <= 14), df['grade'] <= 9],
        ['High', 'Medium', 'Low'],
        default='N/A')     #creating the new grande_band column based on the grade criteria


    summary = (
        df.groupby("grade_band")   #creating the new dataframe where the data is grouped by grade_band
        .agg(
            numberOfstudents=("grade_band", "count"),  #counting the number of student per band
            average_absences=("absences", "mean"),     #computing the average of absences per band
            internet_access_pct=("internet", "mean")    #computing the proportion of student with internet access
        )
        .assign(internet_access_pct=lambda x: x["internet_access_pct"] * 100)   #making that percentages
        .reset_index()
    )
    print(summary)

    summary.to_csv("student_bands.csv", index=False)   #creating the csv file
