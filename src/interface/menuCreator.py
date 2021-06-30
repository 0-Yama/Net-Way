import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from typing import Collection
from functools import partial

class MenuCreator(tk.Frame):

    def __init__       (self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.login()
    def createButton     (self, info) -> tk.Button:
        
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
            print('conf =   ',info["action"])
            button.config(command = info["action"])
                
        except:
            pass
        button.place(bordermode=OUTSIDE, x=info['xpos'], y=info['ypos'], width=info['width'], height=info['height'])
        return button
    def createLabel      (self, info) -> tk.Label:
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
    def createInput      (self, info) -> tk.Entry:
        input = tk.Entry(
                        self.master,
                        show=info['show'],
                        relief=FLAT,
                        textvariable=info['textVar']
                        )
        input.place(bordermode=OUTSIDE, x=info['xpos'], y=info['ypos'], width=info['width'], height=info['height'])
        return input
    def changeShowStatus (self, entry : tk.Entry) -> None:
        if entry.config()['show'][4]:
            print(entry.config()['show'][4])
            entry.configure(show='')
        else:
            print(entry.config()['show'][4])
            entry.configure(show='*')  

    def checklogin(self, login : str, password : str):
        pass

    def login          (self):       
        
        self.loginTextInput = ''
        usernameInput = self.createInput({
                                    'show'                 : '',
                                    'xpos'                 : 450,
                                    'ypos'                 : 200,
                                    'width'                : 200,
                                    'height'               : 40,
                                    'textVar'              : self.loginTextInput
                                    })
        usernameLabel = self.createLabel({
                                    'text'                 : 'Username : ',
                                    'font'                 : 'Arial',
                                    'fontSize'             : 12,
                                    'fontStyle'            : 'bold',
                                    'fontColor'            : '#000000',
                                    'backgroundColor'      : '#FFFFFF',
                                    'backgroundColorHover' : '#FFFFFF',
                                    'xpos'                 : 300,
                                    'ypos'                 : 200,
                                    'width'                : 150,
                                    'height'               : 40})
        
        
        self.passwordTextInput = ''
        passwordInput = self.createInput({
                                    'show'                 : '*',
                                    'xpos'                 : 450,
                                    'ypos'                 : 300,
                                    'width'                : 200,
                                    'height'               : 40,
                                    'textVar'              : self.passwordTextInput
                                    })
        passwordLabel = self.createLabel({
                                    'text'                 : 'Password : ',
                                    'font'                 : 'Arial',
                                    'fontSize'             : 12,
                                    'fontStyle'            : 'bold',
                                    'fontColor'            : '#000000',
                                    'backgroundColor'      : '#FFFFFF',
                                    'backgroundColorHover' : '#FFFFFF',
                                    'xpos'                 : 300,
                                    'ypos'                 : 300,
                                    'width'                : 150,
                                    'height'               : 40})
        passwordShow  = self.createButton({
                                    'text'                 : 'show',
                                    'font'                 : 'Arial',
                                    'fontSize'             : 12,
                                    'fontStyle'            : 'bold',
                                    'fontColor'            : '#FFFFFF',
                                    'backgroundColor'      : '#222222',
                                    'backgroundColorHover' : '#111111',
                                    'xpos'                 : 650,
                                    'ypos'                 : 300,
                                    'width'                : 50,
                                    'height'               : 40,
                                    'action'               : lambda input = passwordInput : (self.changeShowStatus(input))
                                    })

        quit          = self.createButton({
                            'text'                 : 'Quit',
                            'font'                 : 'Arial',
                            'fontSize'             : 12,
                            'fontStyle'            : 'bold',
                            'fontColor'            : '#FFFFFF',
                            'backgroundColor'      : '#AA0000',
                            'backgroundColorHover' : '#440000',
                            'xpos'                 : 80,
                            'ypos'                 : 640,
                            'width'                : 100,
                            'height'               : 40,
                            'action'               : lambda : self.master.destroy()
                            })
        login         = self.createButton({
                                    'text'                 : 'Login',
                                    'font'                 : 'Arial',
                                    'fontSize'             : 12,
                                    'fontStyle'            : 'bold',
                                    'fontColor'            : '#FFFFFF',
                                    'backgroundColor'      : '#00AA00',
                                    'backgroundColorHover' : '#00DD00',
                                    'xpos'                 : 750,
                                    'ypos'                 : 500,
                                    'width'                : 200,
                                    'height'               : 40,
                                    'action'               : lambda  login = self.loginTextInput, password = self.passwordTextInput : self.checklogin(login, password)
                                    })

        self.loginMenu = {
            'quit'  : quit,
            'login' : login,
            'username Input' : usernameInput,
            'username Label' : usernameLabel,
            'password Input' : passwordInput,
            'Password Label' : passwordLabel,
            'password Show'  : passwordShow
        }