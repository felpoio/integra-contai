from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

import dados_empresa
import gestao_empresa
import contabil
import fiscal
import pessoal

#carrega a planilha
caminho_icon = "./assets/images/icon-removebg-preview.ico"
caminho_logo = "./assets/images/LOGO2.png"
caminho_tema = './assets/themes/azure/azure.tcl'

#cria a janela
root = tk.Tk()
root.title("Contai")
root.geometry("400x360")
root.iconbitmap(caminho_icon)
root.resizable(False, False)

#pega o tema da janela
root.tk.call('source', caminho_tema)
style = ttk.Style(root)
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')

#carrega a logo
img = ImageTk.PhotoImage(Image.open(caminho_logo))
panel = tk.Label(root, image = img)
panel.grid(row = 0, columnspan = 3, column = 0, sticky = N, padx = 55, pady = 30)

#cria os botoes
dados_empresa = ttk.Button(root, text = 'Dados da Empresa', width = 23, style = "Accentbutton", command = dados_empresa.jan_dadoEmpresa)
dados_empresa.grid(row = 1, column = 0, sticky = W, padx = 27, pady = 10)
gestao_empresa = ttk.Button(root, text = 'Gestão da Empresa', width = 23, style = "Accentbutton", command = gestao_empresa.jan_gestaoEmpresa)
gestao_empresa.grid(row = 1, column = 2, sticky = W, pady = 10)
#dep_contabil = ttk.Button(root, text = 'Departamento Contábil', width = 23, style = "Accentbutton", command = contabil.jan_depContabil)
#dep_contabil.grid(row = 2, column = 0, sticky = W, padx = 27, pady = 10)
#dep_fiscal = ttk.Button(root, text = 'Departamento Fiscal', width = 23, style = "Accentbutton", command = fiscal.jan_depFiscal)
#dep_fiscal.grid(row = 2, column = 2, sticky = W, pady = 10)
#dep_pessoal = ttk.Button(root, text = 'Departamento Pessoal', width = 23, style = "Accentbutton", command = pessoal.jan_depPessoal)
#dep_pessoal.grid(row = 3, column = 0, sticky = W, padx = 27, pady = 10)
sair = ttk.Button(root, text = 'Sair', width = 23, style = "Accentbutton", command = root.destroy)
sair.grid(row = 3, column = 2, sticky = W)


root.mainloop()