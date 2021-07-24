from typing import NoReturn
from ..lib.mysql.connector import (connection)
class Connector:

    def __init__(self, user : str, password : str, host : str, dbName : str) -> NoReturn:
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
        cursor = self.dbc.cursor()
        cursor.execute(query)
        cursor.close()

    def select(self, table : str, data : str, condition : str = '1 = 1'):
        self.commitQuery(f'SELECT {data} FROM {table} WHERE {condition}')

    def insert(self, table : str, column : str, data : str = '1 = 1'):
        self.commitQuery(f'INSERT INTO {table}({column}) VALUES ({data})')
