from ..lib.mysql.connector import connection
class Connector:

    def __init__(self, user : str, password : str, host : str, dbName : str):
        self.user = user
        self.password = password
        self.host = host
        self.dbName = dbName

    def connect(self):
        self.dbc = connection.MySQLConnection(
                                            user=self.user, 
                                            password=self.password,
                                            host=self.host,
                                            database=self.dbName)

    def commitQuery(self, query : str):
        print(query)
        cursor = self.dbc.cursor()
        cursor.execute(query)
        self.dbc.commit()
        cursor.close()

    def select(self, table : str, data : str, condition : str = '1 = 1'):
        cursor = self.dbc.cursor()
        cursor.execute(f'SELECT {data} FROM {table} WHERE {condition}')
        return cursor



    def insert(self, table : str, column : str, data : str):
        self.commitQuery(f'INSERT INTO {table} ({column}) VALUES ({data})')

    def modify(self, table : str, update : str, condition : str = '1 = 1'):
        self.commitQuery(f'UPDATE {table} SET {update} WHERE {condition}')
