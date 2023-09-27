from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import webbrowser
from openpyxl import load_workbook

#carrega a planilha
caminho = './assets/spreadsheets/LEIAUTE PADRAO.xlsx'
caminho_icon = "./assets/images/icon-removebg-preview.ico"
caminho_logo = "./assets/images/LOGO2.png"
caminho_tema = './assets/themes/azure/azure.tcl'

def jan_Lucro():
    #cria a janela
    
    lucroReal = tk.Toplevel()
    lucroReal.grab_set()
    lucroReal.title("Lucro Presumido / Real")
    lucroReal.geometry("400x360")
    lucroReal.iconbitmap(caminho_icon)
    lucroReal.resizable(False, False)
    
    #carrega a logo
    img = ImageTk.PhotoImage(Image.open(caminho_logo))
    panel2 = tk.Label(lucroReal, image = img)
    panel2.grid(row = 0, columnspan = 3, column = 0, sticky = N, padx = 55, pady = 30)
    
    #cria as opções de sim ou nao da desoneração
    label=Label(lucroReal, text="Optante por desoneração?", font=("Calibri 15"))
    label.grid(row = 1, columnspan = 3, column = 0, sticky = W, padx = 27, pady = 10)
    sim = ttk.Button(lucroReal, text = 'Sim', width = 23, style = "Accentbutton", command = jan_naoDesonerado)
    sim.grid(row = 2, column = 0, sticky = W, padx = 27, pady = 10)
    nao = ttk.Button(lucroReal, text = 'Não', width = 23, style = "Accentbutton", command = jan_desonerado)
    nao.grid(row = 2, column = 2, sticky = W, pady = 10)
    
def jan_desonerado():
    #cria a janela
    desonerado = tk.Toplevel()
    desonerado.grab_set()
    desonerado.title("Não optante por desoneração")
    desonerado.geometry("400x630")
    desonerado.iconbitmap(caminho_icon)
    desonerado.resizable(False, False)
    
    #seta as variaveis globais para serem usadas pela funcao calculo1()
    global entry1
    global decimoTerceiro1
    global ferias1
    global ferias1_31
    global fgts1
    global multaFgts1
    global inssPatronal
    global valorDecimo1
    global valorFerias1
    global valorTerco1
    global valorFgts1
    global valorMulta1
    global valorTotal1
    global valorInss
    global entryFap1
    global entryRat1
    global valorRatFap2
    global valorInssTerceiros1
    
    #cria a entrada de usuário, texto, botões, etc
    label=Label(desonerado, text="Salário", font=("Calibri 15"))
    label.grid(row = 1, column = 0, sticky = W, padx = 27, pady = 10)
    entry1 = Entry(desonerado, width= 20)
    entry1.focus_set()
    entry1.grid(row = 1, column = 2, sticky = W, pady = 10)
    
    labelRat=Label(desonerado, text="Rat", font=("Calibri 15"))
    labelRat.grid(row = 2, column = 0, sticky = W, padx = 27, pady = 10)
    entryRat1 = Entry(desonerado, width= 20)
    entryRat1.grid(row = 2, column = 2, sticky = W, pady = 10)
    labelFap=Label(desonerado, text="Fap", font=("Calibri 15"))
    labelFap.grid(row = 3, column = 0, sticky = W, padx = 27, pady = 10)
    entryFap1 = Entry(desonerado, width= 20)
    entryFap1.grid(row = 3, column = 2, sticky = W, pady = 10)
    
    calcular = ttk.Button(desonerado, text = 'Calcular', width = 23, style = "Accentbutton", command = calculo1)
    calcular.grid(row = 13, column = 0, sticky = W, padx = 27, pady = 10)
    decimo = Label(desonerado, text="Décimo Terceiro", font=("Calibri 15"))
    decimo.grid(row = 4, column = 0, sticky = W, padx = 27, pady = 10)
    valorDecimo1 = Label(desonerado, text='', font=("Calibri 15"))
    valorDecimo1.grid(row = 4, column = 2, sticky = W, pady = 10)
    ferias2 = Label(desonerado, text="Férias", font=("Calibri 15"))
    ferias2.grid(row = 5, column = 0, sticky = W, padx = 27, pady = 10)
    valorFerias1 = Label(desonerado, text='', font=("Calibri 15"))
    valorFerias1.grid(row = 5, column = 2, sticky = W, pady = 10)
    umTerco = Label(desonerado, text="Um terço de férias", font=("Calibri 15"))
    umTerco.grid(row = 6, column = 0, sticky = W, padx = 27, pady = 10)
    valorTerco1 = Label(desonerado, text='', font=("Calibri 15"))
    valorTerco1.grid(row = 6, column = 2, sticky = W, pady = 10)
    fgts2 = Label(desonerado, text="FGTS", font=("Calibri 15"))
    fgts2.grid(row = 7, column = 0, sticky = W, padx = 27, pady = 10)
    valorFgts1 = Label(desonerado, text='', font=("Calibri 15"))
    valorFgts1.grid(row = 7, column = 2, sticky = W, pady = 10)
    multa = Label(desonerado, text="Multa FGTS", font=("Calibri 15"))
    multa.grid(row = 8, column = 0, sticky = W, padx = 27, pady = 10)
    valorMulta1 = Label(desonerado, text='', font=("Calibri 15"))
    valorMulta1.grid(row = 8, column = 2, sticky = W, pady = 10)
    inssPatronal = Label(desonerado, text="Inss Patronal", font=("Calibri 15"))
    inssPatronal.grid(row = 9, column = 0, sticky = W, padx = 27, pady = 10)
    valorInss = Label(desonerado, text='', font=("Calibri 15"))
    valorInss.grid(row = 9, column = 2, sticky = W, pady = 10)  
    ratFap = Label(desonerado, text="Valor Rat Fap", font=("Calibri 15"))
    ratFap.grid(row = 10, column = 0, sticky = W, padx = 27, pady = 10)
    valorRatFap2 = Label(desonerado, text='', font=("Calibri 15"))
    valorRatFap2.grid(row = 10, column = 2, sticky = W, pady = 10)
    inssTerceiros = Label(desonerado, text="INSS Terceiros", font=("Calibri 15"))
    inssTerceiros.grid(row = 11, column = 0, sticky = W, padx = 27, pady = 10)
    valorInssTerceiros1 = Label(desonerado, text='', font=("Calibri 15"))
    valorInssTerceiros1.grid(row = 11, column = 2, sticky = W, pady = 10) 
    total2 = Label(desonerado, text="Total", font=("Calibri 15"))
    total2.grid(row = 12, column = 0, sticky = W, padx = 27, pady = 10)
    valorTotal1 = Label(desonerado, text='', font=("Calibri 15"))
    valorTotal1.grid(row = 12, column = 2, sticky = W, pady = 10)
    
#faz os  calculos do funcionario      
def calculo1():
    #seta as variaveis globais para serem usadas pela jan_desonerado
    global decimoTerceiro1
    global ferias2
    global ferias1_31
    global fgts2
    global multaFgts1
    global entry1
    global inssPatronal
    global valorDecimo1
    global valorFerias1
    global valorTerco1
    global valorFgts1
    global valorMulta1
    global valorTotal1
    global valorInss
    global entryFap1
    global entryRat1
    global valorRatFap2
    global valorInssTerceiros1
    
    #faz os calculos
    salario1 = entry1.get()
    floatSalario1 = float(salario1)
    fap = entryFap1.get()
    rat = entryRat1.get()
    floatFap = float(fap)
    floatRat = float(rat)
    decimoTerceiro1 = floatSalario1 / 12
    ferias2 = floatSalario1 / 12
    ferias1_31 = ferias2 / 3
    fgts2 = (round(floatSalario1, 2) + round(decimoTerceiro1, 2) + round(ferias2, 2) + round(ferias1_31, 2)) * 0.08
    multaFgts1 = round(fgts2, 2) * 0.032
    inssPatronal = (floatSalario1 + decimoTerceiro1 + ferias2 + ferias1_31) * 0.2
    aliquota = floatRat * floatFap
    aliquota = aliquota / 100
    valorRatFap3 = (round(floatSalario1, 2) + round(decimoTerceiro1, 2) + round(ferias2, 2) + round(ferias1_31, 2)) * aliquota
    inssTerceiros1 = (round(floatSalario1, 2) + round(decimoTerceiro1, 2) + round(ferias2, 2) + round(ferias1_31, 2)) * 0.058
    total = floatSalario1 + decimoTerceiro1 + ferias2 + ferias1_31 + fgts2 + multaFgts1 + inssPatronal + valorRatFap3 + inssTerceiros1
    
    #altera o texto exibido no layout
    valorDecimo1.configure(text = round(decimoTerceiro1, 2))
    valorFerias1.configure(text = round(ferias2, 2))
    valorTerco1.configure(text = round(ferias1_31, 2))
    valorFgts1.configure(text = round(fgts2, 2))
    valorMulta1.configure(text = round(multaFgts1, 2))
    valorInss.configure(text = round(inssPatronal, 2))
    valorTotal1.configure(text = round(total, 2))
    valorInssTerceiros1.configure(text = round(inssTerceiros1, 2))
    valorRatFap2.configure(text = round(valorRatFap3, 2))

def jan_naoDesonerado():
    #cria a janela
    naoDesonerado = tk.Toplevel()
    naoDesonerado.grab_set()
    naoDesonerado.title("Optante por desoneração")
    naoDesonerado.geometry("400x590")
    naoDesonerado.iconbitmap(caminho_icon)
    naoDesonerado.resizable(False, False)

    
    #seta as variaveis globais para serem usadas pela funcao calculo2()
    global entry2
    global decimoTerceiro2
    global ferias2
    global ferias1_32
    global fgts2
    global multaFgts2
    global inssPatronal1
    global valorDecimo2
    global valorFerias2
    global valorTerco2
    global valorFgts2
    global valorMulta2
    global valorTotal2
    global entryFap
    global entryRat
    global valorRatFap1
    global valorInssTerceiros
    
    #cria a entrada de usuário, texto, botões, etc
    label=Label(naoDesonerado, text="Salário", font=("Calibri 15"))
    label.grid(row = 1, column = 0, sticky = W, padx = 27, pady = 10)
    entry2 = Entry(naoDesonerado, width= 20)
    entry2.focus_set()
    entry2.grid(row = 1, column = 2, sticky = W, pady = 10)
    labelRat=Label(naoDesonerado, text="Rat", font=("Calibri 15"))
    labelRat.grid(row = 2, column = 0, sticky = W, padx = 27, pady = 10)
    entryRat = Entry(naoDesonerado, width= 20)
    entryRat.grid(row = 2, column = 2, sticky = W, pady = 10)
    labelFap=Label(naoDesonerado, text="Fap", font=("Calibri 15"))
    labelFap.grid(row = 3, column = 0, sticky = W, padx = 27, pady = 10)
    entryFap = Entry(naoDesonerado, width= 20)
    entryFap.grid(row = 3, column = 2, sticky = W, pady = 10)
    calcular = ttk.Button(naoDesonerado, text = 'Calcular', width = 23, style = "Accentbutton", command = calculo2)
    calcular.grid(row = 15, column = 0, sticky = W, padx = 27, pady = 10)
    decimo = Label(naoDesonerado, text="Décimo Terceiro", font=("Calibri 15"))
    decimo.grid(row = 4, column = 0, sticky = W, padx = 27, pady = 10)
    valorDecimo2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorDecimo2.grid(row = 4, column = 2, sticky = W, pady = 10)
    ferias3 = Label(naoDesonerado, text="Férias", font=("Calibri 15"))
    ferias3.grid(row = 5, column = 0, sticky = W, padx = 27, pady = 10)
    valorFerias2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorFerias2.grid(row = 5, column = 2, sticky = W, pady = 10)
    umTerco = Label(naoDesonerado, text="Um terço de férias", font=("Calibri 15"))
    umTerco.grid(row = 6, column = 0, sticky = W, padx = 27, pady = 10)
    valorTerco2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorTerco2.grid(row = 6, column = 2, sticky = W, pady = 10)
    fgts3 = Label(naoDesonerado, text="FGTS", font=("Calibri 15"))
    fgts3.grid(row = 7, column = 0, sticky = W, padx = 27, pady = 10)
    valorFgts2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorFgts2.grid(row = 7, column = 2, sticky = W, pady = 10)
    multa = Label(naoDesonerado, text="Multa FGTS", font=("Calibri 15"))
    multa.grid(row = 8, column = 0, sticky = W, padx = 27, pady = 10)
    valorMulta2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorMulta2.grid(row = 8, column = 2, sticky = W, pady = 10)
    ratFap = Label(naoDesonerado, text="Valor Rat Fap", font=("Calibri 15"))
    ratFap.grid(row = 10, column = 0, sticky = W, padx = 27, pady = 10)
    valorRatFap1 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorRatFap1.grid(row = 10, column = 2, sticky = W, pady = 10)
    inssTerceiros = Label(naoDesonerado, text="INSS Terceiros", font=("Calibri 15"))
    inssTerceiros.grid(row = 11, column = 0, sticky = W, padx = 27, pady = 10)
    valorInssTerceiros = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorInssTerceiros.grid(row = 11, column = 2, sticky = W, pady = 10)
    total3 = Label(naoDesonerado, text="Total", font=("Calibri 15"))
    total3.grid(row = 12, column = 0, sticky = W, padx = 27, pady = 10)
    valorTotal2 = Label(naoDesonerado, text='', font=("Calibri 15"))
    valorTotal2.grid(row = 12, column = 2, sticky = W, pady = 10)

#faz os  calculos do funcionario  
def calculo2():
    #seta as variaveis globais para serem usadas pela jan_naoDesonerado
    global decimoTerceiro2
    global ferias3
    global ferias1_32
    global fgts3
    global multaFgts2
    global entry2
    global inssPatronal1
    global valorDecimo2
    global valorFerias2
    global valorTerco2
    global valorFgts2
    global valorMulta2
    global valorTotal2
    global entryFap
    global entryRat
    global valorRatFap1
    global valorInssTerceiros
    
    #faz os calculos
    salario2 = entry2.get()
    fap = entryFap.get()
    rat = entryRat.get()
    floatFap = float(fap)
    floatRat = float(rat)
    floatSalario2 = float(salario2)
    decimoTerceiro2 = floatSalario2 / 12
    ferias3 = floatSalario2 / 12
    ferias1_32 = ferias3 / 3
    fgts3 = (round(floatSalario2, 2) + round(decimoTerceiro2, 2) + round(ferias3, 2) + round(ferias1_32, 2)) * 0.08
    multaFgts2 = round(fgts3, 2) * 0.032
    aliquota = floatRat * floatFap
    aliquota = aliquota / 100
    valorRatFap = (round(floatSalario2, 2) + round(decimoTerceiro2, 2) + round(ferias3, 2) + round(ferias1_32, 2)) * aliquota
    inssTerceiros = (round(floatSalario2, 2) + round(decimoTerceiro2, 2) + round(ferias3, 2) + round(ferias1_32, 2)) * 0.058
    total = floatSalario2 + decimoTerceiro2 + ferias3 + ferias1_32 + fgts3 + multaFgts2 + valorRatFap + inssTerceiros
    
    #altera o texto exibido no layout
    valorDecimo2.configure(text = round(decimoTerceiro2, 2))
    valorFerias2.configure(text = round(ferias3, 2))
    valorTerco2.configure(text = round(ferias1_32, 2))
    valorFgts2.configure(text = round(fgts3, 2))
    valorMulta2.configure(text = round(multaFgts2, 2))
    valorTotal2.configure(text = round(total, 2))
    valorRatFap1.configure(text = round(valorRatFap, 2))
    valorInssTerceiros.configure(text = round(inssTerceiros, 2))
    
def jan_Simples():
    #cria a janela
    simplesNacional = tk.Toplevel()
    simplesNacional.grab_set()
    simplesNacional.title("Simples Nacional")
    simplesNacional.geometry("400x560")
    simplesNacional.iconbitmap(caminho_icon)
    simplesNacional.resizable(False, False)
    
    #carrega a logo
    img = ImageTk.PhotoImage(Image.open(caminho_logo))
    panel2 = tk.Label(simplesNacional, image = img)
    panel2.grid(row = 0, columnspan = 3, column = 0, sticky = N, padx = 55, pady = 30)
    
    #seta as variaveis globais para serem usadas pela funcao calculo()
    global entry
    global decimoTerceiro
    global ferias
    global ferias1_3
    global fgts
    global multaFgts
    global valorDecimo
    global valorFerias
    global valorTerco
    global valorFgts
    global valorMulta
    global valorTotal
    
    #cria a entrada de usuário, texto, botões, etc
    label=Label(simplesNacional, text="Salário", font=("Calibri 15"))
    label.grid(row = 1, column = 0, sticky = W, padx = 27, pady = 10)
    entry = Entry(simplesNacional, width= 20)
    entry.focus_set()
    entry.grid(row = 1, column = 2, sticky = W, pady = 10)
    calcular = ttk.Button(simplesNacional, text = 'Calcular', width = 23, style = "Accentbutton", command = calculo)
    calcular.grid(row = 8, column = 0, sticky = W, padx = 27, pady = 10)
    decimo = Label(simplesNacional, text="Décimo Terceiro", font=("Calibri 15"))
    decimo.grid(row = 2, column = 0, sticky = W, padx = 27, pady = 10)
    valorDecimo = Label(simplesNacional, text='', font=("Calibri 15"))
    valorDecimo.grid(row = 2, column = 2, sticky = W, pady = 10)
    ferias1 = Label(simplesNacional, text="Férias", font=("Calibri 15"))
    ferias1.grid(row = 3, column = 0, sticky = W, padx = 27, pady = 10)
    valorFerias = Label(simplesNacional, text='', font=("Calibri 15"))
    valorFerias.grid(row = 3, column = 2, sticky = W, pady = 10)
    umTerco = Label(simplesNacional, text="Um terço de férias", font=("Calibri 15"))
    umTerco.grid(row = 4, column = 0, sticky = W, padx = 27, pady = 10)
    valorTerco = Label(simplesNacional, text='', font=("Calibri 15"))
    valorTerco.grid(row = 4, column = 2, sticky = W, pady = 10)
    fgts1 = Label(simplesNacional, text="FGTS", font=("Calibri 15"))
    fgts1.grid(row = 5, column = 0, sticky = W, padx = 27, pady = 10)
    valorFgts = Label(simplesNacional, text='', font=("Calibri 15"))
    valorFgts.grid(row = 5, column = 2, sticky = W, pady = 10)
    multa = Label(simplesNacional, text="Multa FGTS", font=("Calibri 15"))
    multa.grid(row = 6, column = 0, sticky = W, padx = 27, pady = 10)
    valorMulta = Label(simplesNacional, text='', font=("Calibri 15"))
    valorMulta.grid(row = 6, column = 2, sticky = W, pady = 10)
    total1 = Label(simplesNacional, text="Total", font=("Calibri 15"))
    total1.grid(row = 7, column = 0, sticky = W, padx = 27, pady = 10)
    valorTotal = Label(simplesNacional, text='', font=("Calibri 15"))
    valorTotal.grid(row = 7, column = 2, sticky = W, pady = 10)
    
#faz os  calculos do funcionario    
def calculo():
    #seta as variaveis globais para serem usadas pela jan_Simples
    global decimoTerceiro
    global ferias
    global ferias1_3
    global fgts
    global multaFgts
    global entry
    global valorDecimo
    global valorFerias
    global valorTerco
    global valorFgts
    global valorMulta
    global valorTotal
    
    #faz os calculos
    salario = entry.get()
    floatSalario = float(salario)
    decimoTerceiro = floatSalario / 12
    ferias = floatSalario / 12
    ferias1_3 = ferias / 3
    fgts = (round(floatSalario, 2) + round(decimoTerceiro, 2) + round(ferias, 2) + round(ferias1_3, 2)) * 0.08
    multaFgts = round(fgts, 2) * 0.032
    total = floatSalario + decimoTerceiro + ferias + ferias1_3 + fgts + multaFgts
    
    #altera o texto exibido no layout
    valorDecimo.configure(text = round(decimoTerceiro, 2))
    valorFerias.configure(text = round(ferias, 2))
    valorTerco.configure(text = round(ferias1_3, 2))
    valorFgts.configure(text = round(fgts, 2))
    valorMulta.configure(text = round(multaFgts, 2))
    valorTotal.configure(text = round(total, 2))
    
def jan_Calculadora():
    #cria a janela
    janCalculadora = tk.Toplevel()
    janCalculadora.grab_set()
    janCalculadora.title("Cálculo Funcionário")
    janCalculadora.geometry("400x360")
    janCalculadora.iconbitmap(caminho_icon)
    janCalculadora.resizable(False, False)
    
    #carrega a logo
    img = ImageTk.PhotoImage(Image.open(caminho_logo))
    panel2 = tk.Label(janCalculadora, image = img)
    panel2.grid(row = 0, columnspan = 3, column = 0, sticky = N, padx = 55, pady = 30)
    
    #criando botões
    simples = ttk.Button(janCalculadora, text = 'Simples Nacional', width = 23, style = "Accentbutton", command = jan_Simples)
    simples.grid(row = 1, column = 0, sticky = W, padx = 27, pady = 10)
    lucro = ttk.Button(janCalculadora, text = 'Lucro Presumido/Real', width = 23, style = "Accentbutton", command = jan_Lucro)
    lucro.grid(row = 1, column = 2, sticky = W, pady = 10)
    