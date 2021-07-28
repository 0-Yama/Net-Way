from typing import Dict
from ..database.connector import Connector
class Handler:

    def __init__(self):
        self.db = Connector('root','R00tsur8@00','127.0.0.1','NetWay')
        self.db.connect()

    def createUser(self,**info):
        column = ''
        data   = ''
        for columnGet in info:
            column += '`' + columnGet + '`, '
            data   += '\'' + info[columnGet] + '\', '
        column = column[:len(column)-2]
        data = data[:len(data)-2]   
        self.db.insert('user',column,data)

    def modifyUser(self,**info):
        update = ''
        for column in info:
            update += '`' + column + '` = \'' + info[column] + '\', '
        update = update[:len(update)-2]
        print(update)
        self.db.modify('user', update , 'login = \'' + info['login'] + '\'')

    def getUser(self,login):
        cursor =  self.db.select('user','`login`, `name`, `lastName`, `password`, `mail`, `right`, `city`','`login` = \'' + login + '\'')
        returnTab = ['login', 'name', 'lastName', 'password', 'mail', 'right', 'city']
        for login, name, lastName, password, mail, right, city in cursor:
            print(login, name, lastName, password, mail, right, city)
            returnTab = [login, name, lastName, password, mail, right, city]
        return returnTab