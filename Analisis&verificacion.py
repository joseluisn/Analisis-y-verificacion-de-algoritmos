# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:35:35 2019

@author: JOSE LUIS NOVOA
"""
import tkinter as tk
class MainApplication:
    def __init__(self,master):
        self.master = master
        self.create_Main_Window()
    
    def create_Main_Window(self):
        self.frame = tk.Frame(self.master)
        self.master.title("Proyecto Analisis y Verificacion De Algoritmos")
        self.master.geometry("520x480")
        self.master.config(bg="beige")
        self.button = tk.Button(self.master)
        self.button.place(x=100,y=400,width=100,height=30)
        self.button["text"] = "Enter players\n (click me)"
        self.button["command"] = self.new_window
        self.quit = tk.Button(self.master, text="QUIT",command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.quit.place(x=300,y=400,width=100,height=30)
        self.frame.pack()


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = secundary_window(self.newWindow)

class secundary_window:
    def __init__(self, master):
        self.master=master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.master.title("Proyecto Analisis y Verificacion De Algoritmos")
        self.master.geometry("520x480")
        self.master.config(bg="beige")
        nombre = tk.StringVar(self.master)
        tk.Label(self.frame,text="Bienvenido - Ingrese la sgte informacion").pack()
        tk.Label(self.master, text = "Nombre:").pack()
        caja1 = tk.Entry(self.master, textvariable=nombre)
        caja1.pack()
        apellido= tk.StringVar(self.master)
        tk.Label(self.master, text = "Apellido:").pack()
        caja2 = tk.Entry(self.master, textvariable=apellido)
        caja2.pack()
        edad = tk.StringVar(self.master)
        tk.Label(self.master, text = "Edad:").pack()
        caja3 = tk.Entry(self.master, textvariable=edad)
        caja3.pack()
        telefono = tk.StringVar(self.master)
        tk.Label(self.master, text = "Telefono:").pack()
        caja4 = tk.Entry(self.master, textvariable=telefono)
        caja4.pack()  
        universidad = tk.StringVar(self.master)
        tk.Label(self.master, text = "Institucion:").pack()
        caja5 = tk.Entry(self.master, textvariable=universidad)
        caja5.pack()      
        nivel = tk.StringVar(self.master)
        tk.Label(self.master, text = "Ranking:").pack()
        caja6 = tk.Entry(self.master, textvariable=nivel)
        caja6.pack()
        self.button = tk.Button(self.master)
        self.button.place(x=100,y=400,width=100,height=30)
        self.button["text"] = "Save"
        self.quitButton = tk.Button(self.master, text = 'Quit', command = self.master.destroy)
        self.quitButton.pack(side="bottom")
        self.quitButton.place(x=300,y=400,width=100,height=30)
        
        
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
if __name__ == '__main__':
    main()
