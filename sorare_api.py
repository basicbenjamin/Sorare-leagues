import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

# Define the GraphQL query 
#slug names for leagues (la liga: laliga-es, epl: premier-league-gb-eng)
query = '''
query ($first: Int, $after: String) {
  football{
  	competition(slug:"bundesliga-de"){ 
      playersByLastFiveAverage(first: $first, after: $after){
        nodes{
          displayName, 
          so5Scores(last:1){
            allAroundStats{
              stat,totalScore
            },
          	positionTyped,
            score
          }
          },pageInfo{endCursor,hasNextPage}
          }
        }
      }
    }
   
'''

# Define the Sorare API endpoint
url = 'https://api.sorare.com/graphql'


# Load the environment variables
load_dotenv()

# Call api key from environment variable
headers = {
    'Content-Type': 'application/json',
    'APIKEY': os.environ.get('APIKEY')
}

# Initialize variables for pagination
first = 10  # Number of items per page
end_cursor = None  # Start with no cursor
data_list = []  # Initialize an empty list to store the data

# Loop through the pages
while True:
    # Set the query variables
    variables = {"first": first, "after": end_cursor}

    # Send the GraphQL request to the Sorare API
    response = requests.post(url, headers=headers, json={'query': query, 'variables': variables})
    
    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break

    try:
        # Convert the response JSON to a dictionary
        response_json = response.json()
        
        # Check if the 'data' key exists in the response
        if 'data' in response_json:
            data = response_json['data']
            football = data.get('football', {})
            competition = football.get('competition', {})
            players_data = competition.get('playersByLastFiveAverage', {})
            players = players_data.get('nodes', [])

            # Append data to the list
            data_list.extend(players)

            # Check if there are more pages to retrieve
            page_info = players_data.get('pageInfo', {})
            if page_info.get('hasNextPage'):
                end_cursor = page_info.get('endCursor')
            else:
                break
        else:
            print("No 'data' key in the response.")
            break
    except Exception as e:
        print(f"Error processing response: {str(e)}")
        break

# Save the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(data_list, f)









    
























