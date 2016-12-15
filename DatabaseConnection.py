import mysql.connector as mysql


class MySqlConnection:

    def __init__(self, username, passwort, host, database):
        self.username = username
        self.passwort = passwort
        self.host = host
        self.database = database

    def database_connection(self):
        conn = mysql.connect(user=self.username, password=self.passwort, host=self.host, database=self.database)
        cursor = conn.cursor()

    def get_data(self):
        MySqlConnection.database_connection()

get_data_statement = "SELECT * FROM users"
list = ["test", "tunnel2345", "192.168.2.101", "lims"]


connection = MySqlConnection(list[0], list[1], list[2], list[3])
connection.database_connection()
