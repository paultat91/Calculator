#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:45:24 2022

@author: paul
"""

import tkinter as tk

class calculator():

    def __init__(self):
        self.master = tk.Tk() 
        self.master.title('Calculator ')
        self.nome = tk.StringVar()
        
    def string_to_float(self):
        a = self.nome.get()
        for i in range(len(a)):
            if a[i]=='+':
                b = a[:i:]
                c = a[i+1:]
                ans = float(b) + float(c)
                
            if a[i]=='-':
                b = a[:i:]
                c = a[i+1:]
                ans = float(b) - float(c)
                
            if a[i]=='/':
                b = a[:i:]
                c = a[i+1:]
                ans = float(b) / float(c)
                
            if a[i]=='*':
                b = a[:i:]
                c = a[i+1:]
                ans = float(b) * float(c)
        
        if ans == int(ans):
            ans = int(ans)
        return ans
        
    def calculate(self):  
        return lambda:self.nome.set(self.string_to_float())  

    def write(self, num):
        return lambda:self.nome.set(self.nome.get()+num)
        
    def make_calc(self):   
        e0 = tk.Entry(self.master, textvariable=self.nome) 
        e0.grid(columnspan=4) 
        
        e1=tk.Button(self.master,text = '7', command = self.write('7')) 
        e1.grid(row=2, column=0)
        
        e2=tk.Button(self.master,text = '8', command = self.write('8')) 
        e2.grid(row=2, column=1)
        
        e3=tk.Button(self.master,text = '9', command = self.write('9')) 
        e3.grid(row=2, column=2)
        
        e3a=tk.Button(self.master,text = '/', command = self.write('/')) 
        e3a.grid(row=2, column=3)
        
        e4=tk.Button(self.master,text = '4', command = self.write('4')) 
        e4.grid(row=3, column=0)
        
        e5=tk.Button(self.master,text = '5', command = self.write('5')) 
        e5.grid(row=3, column=1)
        
        e6=tk.Button(self.master,text = '6', command = self.write('6')) 
        e6.grid(row=3, column=2)
        
        e6a=tk.Button(self.master,text = '*', command = self.write('*')) 
        e6a.grid(row=3, column=3)
        
        e7=tk.Button(self.master,text = '1', command = self.write('1')) 
        e7.grid(row=4, column=0)
        
        e8=tk.Button(self.master,text = '2', command = self.write('2')) 
        e8.grid(row=4, column=1)
        
        e9=tk.Button(self.master,text = '3', command = self.write('3')) 
        e9.grid(row=4, column=2)
        
        e9a=tk.Button(self.master,text = '-', command = self.write('-')) 
        e9a.grid(row=4, column=3)
        
        e10=tk.Button(self.master,text = '0', command = self.write('0')) 
        e10.grid(row=5, column=0)
        
        e11=tk.Button(self.master,text = '.', command = self.write('.')) 
        e11.grid(row=5, column=1)
        
        e12=tk.Button(self.master,text = '+', command = self.write('+')) 
        e12.grid(row=5, column=2)
        
        e13=tk.Button(self.master,text = '=', command = self.calculate()) 
        e13.grid(row=5, column=3) 
        
        tk.Label(self.master, text="").grid(row=1)
        tk.Label(self.master, text="").grid(row=6)
        tk.mainloop() 
    
 
if __name__=="__main__":
    calc = calculator()
    calc.make_calc()

        
    
    
