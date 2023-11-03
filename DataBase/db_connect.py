import psycopg2

# Replace these values with your PostgreSQL database configuration
host = "localhost"
user = "postgres"
password = "admin123"
database = "testdb"

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Define the CREATE TABLE SQL query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS details (
        id serial PRIMARY KEY,
        name VARCHAR(250),
        age int
    )
    """

    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)

    # Commit the changes to the database
    connection.commit()

    print("Table created successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)
