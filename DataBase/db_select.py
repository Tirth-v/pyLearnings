import psycopg2

# Replace these values with your PostgreSQL database configuration
host = "localhost"
user = "postgres"
password = "admin123"
database = "testdb"

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Define your SELECT query
    select_query = "SELECT * FROM details"

    # Execute the query
    cursor.execute(select_query)

    # Fetch the results
    results = cursor.fetchall()
    # Process and print the results
    for row in results:
        column1_value = row[0]
        column2_value = row[1]
        column3_value = row[2]
        print(f"ID : {column1_value}, Name : {column2_value}, Age : {column3_value}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)
