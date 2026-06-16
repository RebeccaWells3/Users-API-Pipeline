from api import get_api_data,url
from flatten_api_data import flatten_data
from dataframe import create_dataframe, load_to_sqlite
from users_sqlite_table import connection, cursor

api_data = get_api_data(url)

fd = flatten_data(api_data)

df = create_dataframe(fd)

table_name = 'users'
if_exists = 'replace'
load_to_sqlite(df,table_name, connection, if_exists=if_exists)

#count how many users are in table
cursor.execute('SELECT COUNT(*) FROM users')

row = cursor.fetchall()
for a in row:
    print(a[0])


#any of users work at same company?
cursor.execute('SELECT company_name FROM users GROUP BY company_name HAVING COUNT(name) > 1')

groups = cursor.fetchall()

print(groups)



