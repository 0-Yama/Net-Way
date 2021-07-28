from hashlib import blake2b
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from ..database.handler import Handler
from ..gestUser.gestuser import User
from ..portscanner.portscanner import PortScanner

class MenuCreator(tk.Frame):

    def __init__           (self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.loginMenu()

    def createButton       (self, **info) -> tk.Button:
        
        button = tk.Button(self.master,
                        text    = info['text'],
                        font             = (info["font"], info["fontSize"], info["fontStyle"]),
                        foreground       = info["fontColor"],
                        background       = info["backgroundColor"],
                        activebackground = info['backgroundColorHover'],
                        activeforeground = info['fontColor'],
                        relief           = FLAT,
                        cursor           = 'hand2')
        try:
            button.config(command = info["action"])
                
        except:
            pass
        button.place(bordermode=OUTSIDE, x=info['xpos'], y=info['ypos'], width=info['width'], height=info['height'])
        return button

    def createLabel        (self, **info) -> tk.Label:
        text = tk.Label(
                        self.master,
                        relief = FLAT,
                        text   = info['text'],
                        font   = (info["font"], info["fontSize"], info["fontStyle"]),
                        foreground       = info["fontColor"],
                        background       = info["backgroundColor"],
                        activebackground = info['backgroundColorHover'],
                        activeforeground = info['fontColor'],
        )
        text.place(bordermode=OUTSIDE, x=info['xpos'], y=info['ypos'], width=info['width'], height=info['height'])
        return text

    def createInput        (self, **info) -> tk.Entry:
        input = tk.Entry(
                        self.master,
                        name=info['name'],
                        show=info['show'],
                        relief=FLAT,
                        )
        input.place(bordermode=OUTSIDE, x=info['xpos'], y=info['ypos'], width=info['width'], height=info['height'])
        return input

    def changeShowStatus   (self, entry : tk.Entry) -> None:
        if entry.config()['show'][4]:
            entry.configure(show='')
        else:
            entry.configure(show='*')  

    def checklogin         (self,username : Entry ,password : Entry):
        dataUser = Handler().getUser(username.get())
        self.user = User(
                    status   = "stable",
                    login    = dataUser[0],
                    password = dataUser[3],
                    name     = dataUser[1],
                    lastName = dataUser[2],
                    mail     = dataUser[4],
                    right    = dataUser[5],
                    city     = dataUser[6]
        )
        if(blake2b(bytearray(password.get(), "utf8")).hexdigest()==self.user.password):
            self.destroyMenu(self.loginMenuWidget)
            self.destroy()
            super().__init__(self.master)
            self.pack()
            self.showMenu(self.user.right)

    def showMenu           (self, right):
        if right == 'AS':
            print('AS')
            self.asMenu()
        elif right == 'AC':
            print('AC')
            self.acMenu()

    def destroyMenu        (self, menu : dict):
        for widget in menu:
            print(menu[widget])
            menu[widget].destroy()

    def loginMenu          (self): 
        usernameInput = self.createInput(name                = 'login',
                                        show                 = '',
                                        xpos                 = 450,
                                        ypos                 = 200,
                                        width                = 200,
                                        height               = 40)
        usernameLabel = self.createLabel(text                = 'Username : ',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#000000',
                                        backgroundColor      = '#FFFFFF',
                                        backgroundColorHover = '#FFFFFF',
                                        xpos                 = 300,
                                        ypos                 = 200,
                                        width                = 150,
                                        height               = 40)
        passwordInput = self.createInput(name                = 'password',
                                        show                 = '*',
                                        xpos                 = 450,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40)
        passwordLabel = self.createLabel(text                = 'Password : ',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#000000',
                                        backgroundColor      = '#FFFFFF',
                                        backgroundColorHover = '#FFFFFF',
                                        xpos                 = 300,
                                        ypos                 = 300,
                                        width                = 150,
                                        height               = 40)
        passwordShow  = self.createButton(text               = 'show',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 300,
                                        width                = 50,
                                        height               = 40,
                                        action               = lambda input = passwordInput : (self.changeShowStatus(input)))
        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())
        login         = self.createButton(text               = 'Login',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#00AA00',
                                        backgroundColorHover = '#00DD00',
                                        xpos                 = 750,
                                        ypos                 = 500,
                                        width                = 200,
                                        height               = 40,
                                        action               = lambda username = usernameInput, password = passwordInput : self.checklogin(username, password))

        self.loginMenuWidget = {
            'quit'  : quit,
            'login' : login,
            'username Input' : usernameInput,
            'username Label' : usernameLabel,
            'password Input' : passwordInput,
            'Password Label' : passwordLabel,
            'password Show'  : passwordShow
        }

    def acMenu             (self):
        userGestButton  = self.createButton(text             = 'User Gestion',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 300,
                                        width                = 50,
                                        height               = 40,
                                        action               = lambda : (self.showuserGestMenu('ac')))

        ftpButton       = self.createButton(text             = 'User Gestion',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 300,
                                        width                = 50,
                                        height               = 40,
                                        action               = lambda : (self.ftpMenu()))
        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())  
        self.acMenuWidget = {
            'quit'  : quit,
            'userGestButton' : userGestButton,
            'ftpButton' : ftpButton
        }

    def asMenu             (self):
        print("AS Menu")
        userGestButton  = self.createButton(text             = 'User Gestion',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 450,
                                        ypos                 = 200,
                                        width                = 200,
                                        height               = 40,
                                        action               = lambda : (self.showuserGestMenu('as')))

        ftpButton       = self.createButton(text             = 'FTP Gestion',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 450,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40,
                                        action               = lambda : (self.ftpMenu()))
        toolboxButton   = self.createButton(text             = 'ToolBox',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 450,
                                        ypos                 = 400,
                                        width                = 200,
                                        height               = 40,
                                        action               = lambda : (self.toolboxMenu()))
        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())

        self.asMenuWidget = {
            'quit'  : quit,
            'userGestButton' : userGestButton,
            'ftpButton' : ftpButton,
            'toolboxButton' : toolboxButton,
        }

    def showuserGestMenu   (self,menu):
        if menu == 'as':
            self.destroyMenu(self.asMenuWidget)
        elif menu == 'ac':
            self.destroyMenu(self.acMenuWidget)
        self.userGestMenu()

    def showftpMenu        (self,menu):
        if menu == 'as':
            self.destroyMenu(self.asMenuWidget)
        elif menu == 'ac':
            self.destroyMenu(self.acMenuWidget)
        self.ftpMenu()

    def userGestMenu       (self):
        searchUserLabel     = self.createLabel(text          = 'Password : ',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#000000',
                                        backgroundColor      = '#FFFFFF',
                                        backgroundColorHover = '#FFFFFF',
                                        xpos                 = 300,
                                        ypos                 = 300,
                                        width                = 150,
                                        height               = 40)
        searchUserButton   = self.createButton(text          = 'Search',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 300,
                                        width                = 60,
                                        height               = 40,
                                        action               = lambda : self.userUpdateMenu())
        searchUserInput    = self.createInput(name           = 'searchuser',
                                        show                 = '',
                                        xpos                 = 450,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40)
        

        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())

        self.userGestMenuWidget ={
            'quit'  : quit,
            'searchUserButton' : searchUserButton,
            'searchUserLabel'  : searchUserLabel,
            'searchUserInput'  : searchUserInput
        }

    def userUpdateMenu     (self):
        self.destroyMenu()

    def ftpMenu            (self):
        pass

    def toolboxMenu        (self):
        self.destroyMenu(self.asMenuWidget)
        scanportButton  = self.createButton(text             = 'Scanport',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 450,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40,
                                        action               = lambda : self.scanportMenu())

        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())

        self.toolboxMenuWidget = {
            'quit'  : quit,
            'scanportButton' : scanportButton
        }
    def scanportMenu       (self):
        self.destroyMenu(self.toolboxMenuWidget)

        simpleScanInput = self.createInput(name              = 'simpleScan',
                                        show                 = '',
                                        xpos                 = 450,
                                        ypos                 = 200,
                                        width                = 200,
                                        height               = 40)
        simpleScanLabel = self.createLabel(text              = 'Scan one port',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#000000',
                                        backgroundColor      = '#FFFFFF',
                                        backgroundColorHover = '#FFFFFF',
                                        xpos                 = 300,
                                        ypos                 = 200,
                                        width                = 150,
                                        height               = 40)
        simpleScanButton  = self.createButton(text           = 'Scan',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 200,
                                        width                = 50,
                                        height               = 40,
                                        action               = lambda port  = simpleScanInput : (PortScanner("simple",int(port.get()),'127.0.0.1').scan()))



        rangeScanInput    = self.createInput(name            = 'rangeScan',
                                        show                 = '',
                                        xpos                 = 450,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40)
        rangeScanLabel    = self.createLabel(text            = 'Scan a range of ports',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#000000',
                                        backgroundColor      = '#FFFFFF',
                                        backgroundColorHover = '#FFFFFF',
                                        xpos                 = 250,
                                        ypos                 = 300,
                                        width                = 200,
                                        height               = 40)
        rangeScanButton    = self.createButton(text          = 'Scan',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 650,
                                        ypos                 = 300,
                                        width                = 50,
                                        height               = 40,
                                        action               = lambda port  = rangeScanInput : (PortScanner("range",[port.get()],'127.0.0.1').scan()))


        allScanButton      = self.createButton(text          = 'Scan all ports',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#222222',
                                        backgroundColorHover = '#111111',
                                        xpos                 = 450,
                                        ypos                 = 400,
                                        width                = 250,
                                        height               = 40,
                                        action               = lambda port  = simpleScanInput : (PortScanner("all").scan()))
        
        quit          = self.createButton(text               = 'Quit',
                                        font                 = 'Arial',
                                        fontSize             = 12,
                                        fontStyle            = 'bold',
                                        fontColor            = '#FFFFFF',
                                        backgroundColor      = '#AA0000',
                                        backgroundColorHover = '#440000',
                                        xpos                 = 80,
                                        ypos                 = 640,
                                        width                = 100,
                                        height               = 40,
                                        action               = lambda : self.master.destroy())

        self.toolboxMenuWidget = {
            'quit'  : quit,
            'simpleScanInput' : simpleScanInput,
            'simpleScanLabel' : simpleScanLabel,
            'simpleScanButton': simpleScanButton,
            'rangeScanInput'  : rangeScanInput,
            'rangeScanLabel'  : rangeScanLabel,
            'rangeScanButton' : rangeScanButton,
            'allScanButton'   : allScanButton
        }