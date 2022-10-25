from tkinter import *
import tkinter

#### Cores ####

cor1 = '#0a0a0a' #black
cor2 = '#fafcff' #white
cor3 = '#21c25c' #green
cor4 = '#eb463b' #red
cor5 = '#dedcdc' #gray
cor6 = '#3080f0' #blue

#### Variáveis Globais ####

#Serão utilizadas dentro das funções
global tempo
global ativador
global contador
global limitador

tempo = '00:00:00'
ativador = False
contador = 0
limitador = 60

#### Funções ####

def iniciar():
    global tempo
    global ativador
    global contador
    global limitador

    #Inicializador da função
    if ativador == True:

        temporario = str(tempo)

        #Dividindo o horário em hora, minuto e segundo
        hora, minuto, segundo = map(int, temporario.split(':'))
        hora = int(hora)
        minuto = int(minuto)
        segundo = int(contador)

        #Mudança de horário: de segundos para minutos
        if segundo == limitador:
            minuto += 1
            contador = 0
            segundo = 0

        # Mudança de horário: de minutos para horas
        if minuto == limitador:
            hora += 1
            contador = 0
            minuto = 0

        if hora == 24:
            hora = 0
            minuto = 0
            segundo = 0
            contador = 0

        hora = str(0) + str(hora)
        minuto = str(0) + str(minuto)
        segundo = str(0) + str(segundo)

        temporario = str(hora[-2:]) + ':' + str(minuto[-2:]) + ":" + str(segundo[-2:])
        lblTempo['text'] = temporario
        tempo = temporario

        lblTempo.after(1000, iniciar)
        contador += 1

def start():
    global ativador
    #Transformando ativador em True faz com que 'iniciar()' funcione
    ativador = True
    iniciar()

def parar():
    global ativador
    #Tornando o ativador igual a 'False' a função 'start' não roda
    ativador = False

def reiniciar():
    global contador
    global tempo

    #Reiniciado o tempo
    tempo = "00:00:00"
    lblTempo['text'] = tempo

    #Zerando o contador para recomeçar a contagem
    contador = 0

def zerar():
    global contador
    global tempo
    global ativador

    #Reiniciado o tempo
    tempo = "00:00:00"
    lblTempo['text'] = tempo

    #Zerando o contador para recomeçar a contagem
    contador = 0

    ativador = False

#### Janela ####

janela = Tk()
janela.title("Cronômetro")
janela.geometry("400x200")
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='logo.png'))

#### Labels #####

lblCronometro = Label(janela, text='Cronômetro', font=("Arial 16 bold"), bg=cor1, fg=cor2)
lblCronometro.place(x=132, y=5)

lblTempo = Label(janela, text=tempo, font=("Times 65 bold"), bg=cor1, fg=cor6, anchor=E)
lblTempo.place(x=34, y=30)

#### Botões ####

btnIniciar = Button(janela, command=start, width=10, height=2, text="Iniciar", bg=cor1, fg=cor2, font=("Ivy 10 bold"), relief='raised', overrelief='ridge')
btnIniciar.place(x=20, y=140)

btnPausar = Button(janela, command=parar, width=10, height=2, text="Pausar", bg=cor1, fg=cor2, font=("Ivy 10 bold"), relief='raised', overrelief='ridge')
btnPausar.place(x=110, y=140)

btnReiniciar = Button(janela, command=reiniciar, width=10, height=2, text="Reiniciar", bg=cor1, fg=cor2, font=("Ivy 10 bold"), relief='raised', overrelief='ridge')
btnReiniciar.place(x=200, y=140)

btnZerar = Button(janela, command=zerar, width=10, height=2, text="Zerar", bg=cor1, fg=cor2, font=("Ivy 10 bold"), relief='raised', overrelief='ridge')
btnZerar.place(x=290, y=140)

janela.mainloop()