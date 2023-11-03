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


    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM details")
    name_count = cursor.fetchone()[0]
    print(f"Total Employees: {name_count}")

    cursor.execute("SELECT SUM(age) FROM details")
    total_age = cursor.fetchone()[0]
    print(f"total age{total_age}")

    cursor.execute("SELECT MAX(age) FROM details")
    max_age = cursor.fetchone()[0]
    print(f"max age{max_age}")

    cursor.execute("SELECT MIN(age) FROM details")
    min_age = cursor.fetchone()[0]
    print(f"Lowest age{min_age}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)