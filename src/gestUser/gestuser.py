from ..database.handler import Handler
class User:

    def __init__(self, **info) -> None:
        print(info)
        print('\n\n\n\n')
        self.status   = info['status']
        self.login    = info['login']
        self.password = info['password']
        self.name     = info['name']
        self.lastName = info['lastName']
        self.mail     = info['mail']
        self.right    = info['right']
        self.city     = info['city']
    
    def setStatus(self, new : str) -> None:
        self.status = new

    def setChange(self) -> None:
        if (self.status == 'created'):
            print("changing the created user")
            Handler().createUser(
                    login    = self.login,
                    name     = self.name,
                    lastName = self.lastName,
                    password = self.password,
                    mail     = self.mail,
                    right    = self.right,
                    city     = self.city
            )
        elif (self.status == 'modified'):
            Handler().modifyUser(
                    login    = self.login,
                    name     = self.name,
                    lastName = self.lastName,
                    password = self.password,
                    mail     = self.mail,
                    right    = self.right,
                    city     = self.city
            )
        self.setStatus('stable')

    def setNewPassword(self,new) -> None:
        self.password = new
        self.setStatus('modified')

