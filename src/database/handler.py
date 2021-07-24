from ..database.connector import Connector
class Handler:

    def __init__(self):
        self.db = Connector('root','R00tsur8@00','127.0.0.1','NetWay')
    
    def getData(self,param):
        pass