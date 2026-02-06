#Question 4
import pandas as pd

with (open(file='student.csv', mode='r') as file):
    df = pd.read_csv('student.csv')    #putting the data from the csv file in a dataframe

    #creating a new dataframe with only the rows (students) that correspond to certain criteria
    filtered_df = df[
        (df['absences'] <= 5) &
        (df['studytime'] >= 3) &
        (df['internet'] == 1)
        ]


    # saving everything to a csv file
    filtered_df.to_csv('high_engagement.csv', index=False)

    # printing everything in the required format
    print(f"Number of students : {len(filtered_df)}")
    print(f"Average grade: {filtered_df['grade'].mean():.2f}")