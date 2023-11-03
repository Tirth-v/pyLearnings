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

    # Example 1: Using CONCAT() to concatenate strings
    cursor.execute("SELECT CONCAT('Hello', ' ', 'World')")
    concatenated_string = cursor.fetchone()[0]
    print(f"Concatenated String: {concatenated_string}")

    # Example 2: Using LENGTH() to get the length of a string
    cursor.execute("SELECT LENGTH('PostgreSQL')")
    string_length = cursor.fetchone()[0]
    print(f"String Length: {string_length}")

    # Example 3: Using UPPER() to convert a string to uppercase
    cursor.execute("SELECT UPPER('postgresql')")
    uppercase_string = cursor.fetchone()[0]
    print(f"Uppercase String: {uppercase_string}")

    # Example 4: Using LOWER() to convert a string to lowercase
    cursor.execute("SELECT LOWER('POSTGRESQL')")
    lowercase_string = cursor.fetchone()[0]
    print(f"Lowercase String: {lowercase_string}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)