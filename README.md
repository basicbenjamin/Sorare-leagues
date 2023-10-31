# Sorare-leagues

DISCLAIMER: This project was soley done using chat-GPT

# Sorare API Data Retrieval Documentation

## Introduction

This Python script is designed to fetch data from the Sorare API using GraphQL queries. Sorare is a fantasy football platform that provides statistics about football players in various leagues. This example script retrieves player data for the Bundesliga league and stores it in a JSON file, however you can use it to fetch data from any league available on sorare.

## Prerequisites

Before running this script, ensure you have the following prerequisites:

- Python installed on your system.
- The `requests`, `json`, `os`, `dotenv`, and `pandas` Python libraries installed. You can install these libraries using pip:

 

## Code Overview

The script performs the following tasks:

1. Imports required libraries, such as `requests`, `json`, `os`, `dotenv`, and `pandas`.
2. Defines a GraphQL query to retrieve player data from the Sorare API.
3. Loads environment variables using `dotenv` to securely store sensitive information like the API key.
4. Initializes variables for pagination and an empty list to store the retrieved data.
5. Loops through the API pages, sending GraphQL requests with pagination variables to retrieve player data.
6. Checks for errors in the API response, ensuring a status code of 200.
7. Processes the API response JSON, extracting player data and checking for pagination information.
8. Stores the retrieved player data in a JSON file named `data.json`.
9. Imports the `pandas` and `json` libraries.
10. Reads a JSON file named `data.json` containing nested data, assumed to be retrieved from the Sorare API.
11. Normalizes the nested data within the 'so5Scores' column and expands it into separate columns.
12. Iterates through the nested dictionaries, extracting key-value pairs from the 'allAroundStats' field.
13. Checks if 'allAroundStats' is a float (indicating 'totalScore') and handles it accordingly.
14. Drops the 'allAroundStats' column after extraction.
15. Resets the index to ensure proper indexing for the DataFrame.
16. Exports the normalized data to a CSV file named 'data.csv'.

## Usage

1. Ensure that you have the required libraries installed and the Python environment set up.
2. Create a `.env` file in the same directory as the script and add your Sorare API key.
3. Run the script 'sorare_api.py' using a Python interpreter.
4. The script will fetch player data from the Sorare API, process it, and store it in a JSON file named `data.json`.
5. Ensure that you have the `pandas` library installed and the Python environment set up.
6. Run the script 'create_csv.py' using a Python interpreter.
7. The script will read the JSON file, normalize the data, and export it to a CSV file named `data.csv`.


## Error Handling

The script performs basic error handling to ensure that it processes the API responses correctly. It checks for:

- A valid HTTP status code (status code 200 indicates a successful response).
- The presence of the 'data' key in the API response.
- The presence of player data in the response.

Any errors encountered during the execution of the script will be printed to the console.

## Data Storage

The retrieved player data is stored in a JSON file named `data.json` in the same directory as the script. Once the JSON is normalized, the data is then stored in 'data.csv'. This file can be imported into google sheets or any other workbook for futher analysis.

## Notes

- The script is designed to retrieve player data from the Bundesliga league. To retrieve data from other leagues, you can modify the GraphQL query accordingly.

- Make sure to follow Sorare's terms of service and API usage policies when using this script.

- This script is intended as a starting point for data retrieval and may require customization for your specific use case.

- Ensure that you have proper authentication and authorization to access the Sorare API.

- The script is designed for data specifically retrieved from the Sorare API. Make sure the JSON file structure matches the assumptions made by the script.

  



