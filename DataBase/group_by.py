import psycopg2


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


    cursor = connection.cursor()

    cursor.execute("SELECT name, SUM(age) as total_age FROM details GROUP BY name")
    category_sales = cursor.fetchall()
    print("Total age per name Category:")
    for row in category_sales:
        category, total_sales = row
        print(f"{category}: {total_sales}")

    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)