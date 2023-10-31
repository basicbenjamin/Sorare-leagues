import pandas as pd
import json


f = open('data.json','r')
file = json.loads(f.read())

#load json
data = pd.read_json('data.json')

# Normalize the nested json within the so5Scores column
df = pd.DataFrame(data)
df = df.explode('so5Scores')

# Normalize the nested json within the so5Scores column
df = pd.concat([df.drop(['so5Scores'], axis=1), df['so5Scores'].apply(pd.Series)], axis=1)


# Iterate through the nested dictionaries and extract key-value pairs
for i, row in df.iterrows():
    stats_list = row['allAroundStats']

    # Check if stats_list is a float (totalScore)
    if isinstance(stats_list, float):
        df.at[i, 'totalScore'] = stats_list
    else:
        if stats_list:  # Check if stats_list is not empty
            for stat_dict in stats_list:
                key = stat_dict['stat']
                value = stat_dict['totalScore']
                df.at[i, key] = value
    
df = df.drop(['allAroundStats'], axis=1)


# Reset the index
df = df.reset_index(drop=True)

#export to csv
df.to_csv('data.csv', index=False)

