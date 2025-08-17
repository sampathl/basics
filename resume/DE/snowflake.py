import snowflake.connector
import mysql.connector

# Snowflake connection parameters
snowflake_account = 'your_account_url'
snowflake_user = 'your_username'
snowflake_password = 'your_password'
snowflake_database = 'your_database'
snowflake_schema = 'your_schema'
snowflake_table = 'your_table'

# MySQL connection parameters
mysql_host = 'mysql_host'
mysql_user = 'mysql_username'
mysql_password = 'mysql_password'
mysql_database = 'mysql_database'
mysql_table = 'mysql_table'

# Establish Snowflake connection
snowflake_conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    database=snowflake_database,
    schema=snowflake_schema
)

# Establish MySQL connection
mysql_conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Retrieve data from MySQL
mysql_cursor = mysql_conn.cursor()

# Execute a SELECT query to retrieve data from MySQL
mysql_cursor.execute(f'SELECT * FROM {mysql_table}')

# Fetch all rows from the result set
mysql_data = mysql_cursor.fetchall()

# Define a temporary file to store the data
temp_file = '/path/to/temp_file.csv'

# Write the MySQL data to a temporary CSV file
with open(temp_file, 'w') as file:
    for row in mysql_data:
        file.write(','.join(map(str, row)) + '\n')

# Close the MySQL cursor and connection
mysql_cursor.close()
mysql_conn.close()

# Copy the data from the temporary CSV file to Snowflake table
snowflake_cursor = snowflake_conn.cursor()

# Execute the COPY command to load data from the CSV file into Snowflake table
snowflake_cursor.execute(f'COPY INTO {snowflake_table} FROM \'file://{temp_file}\' '
                         'FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT)')

# Commit the changes
snowflake_conn.commit()

# Close the Snowflake cursor and connection
snowflake_cursor.close()
snowflake_conn.close()

print("Data loaded from MySQL to Snowflake successfully.")


# Insert data into Snowflake
snowflake_cursor = snowflake_conn.cursor()
for row in mysql_data:
    snowflake_cursor.execute(f'INSERT INTO {snowflake_table} VALUES (%s, %s, %s)', row)

# Commit changes and close connections
snowflake_conn.commit()
snowflake_conn.close()