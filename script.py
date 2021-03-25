import mysql.connector

def prompt():
    print("Select the option that you would like to use")
    print("1) Insert into table")
    print("2) Retrieve table")
    print()

def main():
    MyPassword = "r3d570n3"
    MyUser = "root"  # usually 'root'
    # e.g., IP address of a MySQL instance in Google Cloud Platform, or 'localhost' for a local MySQL database
    MyHost = "34.66.172.145"
    MyDatabase = "jain322"
    # cnx = mysql.connector.connect(user='root', password=pwd.MyPassword,
    #                               host='localhost',
    #                               database='pricelist')
    while(1):
        prompt()
        input_number = input()
        if (input_number == "1"):
            print("1")
            # do something
        if (input_number == "2"):
            print("2")
            # do something

if __name__ == "__main__":
    main()
