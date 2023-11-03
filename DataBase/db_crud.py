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


    def insert():
        id = input("Enter an id: ")
        name = input("Enter a name:")
        age = int(input("Enter a age: "))
        insert_query = "INSERT INTO details (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (id, name, age))
        print("Data inserted successfully")


    def select():
        select_query = "SELECT * FROM details"
        cursor.execute(select_query)
        results = cursor.fetchall()
        for row in results:
            column1_value = row[0]
            column2_value = row[1]
            column3_value = row[2]
            print(f"ID : {column1_value}, Name : {column2_value}, Age : {column3_value}")


    def update():
        id = input("Enter id that you want to update: ")
        input_1 = input("Do you want to update name? y/n")
        if input_1 == "y":
            name = input("Enter new name :")
            update_query = f"UPDATE details SET name = {name} WHERE ID = {id}"
        else:
            age = int(input("Enter new age: "))
            update_query = f"UPDATE details SET age = {age} WHERE ID = {id}"
        cursor.execute(update_query)


    def delete():
        input_1 = input("""Enter your choice :
        1. id
        2. name
        3. age""")
        if input_1 == "1":
            id = input("Enter id that you want to delete: ")
            delete_query = f"DELETE FROM details WHERE id = {id}"
            cursor.execute(delete_query)
        elif input_1 == "2":
            name = input("Enter name : ")
            delete_query = f"DELETE FROM details WHERE name = {name}"
            cursor.execute(delete_query)
        elif input_1 == "3":
            age = int(input("Enter age : "))
            delete_query = f"DELETE FROM details WHERE age = {age}"
            cursor.execute(delete_query)

    choice = int(input("""What operation would you like to perform?
    1. INSERT
    2. SELECT
    3. UPDATE
    4. DELETE\n"""))

    if choice == 1:
        insert()
    elif choice == 2:
        select()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()

    connection.commit()
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)