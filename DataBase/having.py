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


    # Example: Using HAVING to filter groups by average age
    cursor.execute("SELECT name, AVG(age) as avg_age FROM details GROUP BY name HAVING age > 22")
    departments_with_high_avg_age = cursor.fetchall()
    print("Names with Average Age > 22:")
    for row in departments_with_high_avg_age:
        department, avg_age = row
        print(f"{department}: {avg_age} years")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)
