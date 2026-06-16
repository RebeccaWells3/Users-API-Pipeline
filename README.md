<h1 align="center">Users API Pipeline</h1>

This project retrieves user data from an API, flattens nested API data, and places the results 
into a Pandas DataFrame. It then loads the DataFrame into a SQLite database where the data can be 
queried with SQL.

## Technologies Used

- Python
- Requests
- Pandas
- SQLite

## Data Flow

1. Retrieve user data from a REST API.
2. Flatten nested JSON fields into a tabular structure.
3. Create a Pandas DataFrame from the flattened data.
4. Use Pandas to load the DataFrame into a SQLite database.
5. Query the database using SQL.

## Analysis Questions

The project answers the following questions:

1. How many users are stored in the table?
2. Do any users work at the same company?

## Project Structure

- [`api.py`](https://github.com/RebeccaWells3/Users-API-Pipeline/blob/main/api.py) – Retrieves and parses data from the API.
- [`flatten_api_data.py`](https://github.com/RebeccaWells3/Users-API-Pipeline/blob/main/flatten_api_data.py) – Flattens nested API data into a tabular structure.
- [`dataframe.py`](https://github.com/RebeccaWells3/Users-API-Pipeline/blob/main/dataframe.py) – Creates a Pandas DataFrame and loads the DataFrame into SQLite.
- [`users_sqlite_table.py`](https://github.com/RebeccaWells3/Users-API-Pipeline/blob/main/users_sqlite_table.py) – Creates the SQLite database and users table.
- [`main.py`](https://github.com/RebeccaWells3/Users-API-Pipeline/blob/main/main.py) – Runs the pipeline and executes SQL queries.

## How to Run

1. Install the required packages:

```bash
pip install pandas requests
```

2. Run the project:

```bash
python main.py
```
