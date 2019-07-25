"""
*********************************************************************
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores


 Lenguaje: Python 3.4.2
 Autor: Pablo Garcia Brenes y Marco Fernandez
 Versión: 1.0
 Fecha Última Modificación: Mayo 3/2015
 
*********************************************************************** """
#==================== Biblioteca ====================================#
import tkinter
from tkinter import *
import os
import winsound
import threading
from threading import Thread
import time
import random
import sys


def load_img(name): #Para subir imagnenes
    path= os.path.join("imgs",name) #Establece donde debe buscar la imagen
    img= PhotoImage(file=path)
    return img



#==================== Start Window ==================================#
Carros_Flag=True
TIME_FLAG=True
TIEMPO=180
LIVES=7
POINTS=0
TRONCO_FLAG=True
LEVEL=1

def Start():
    global Player
    Menu.withdraw() #Extrae la ventana de menu
    
    Start= Toplevel()  #Crea una nueva ventana
    Start.minsize(width=550,height=600)  #Define el tamaño
    Start.resizable(width=False,height=False)


#=========Imagenes

    Fondo_juego= load_img("Fondo_juego editador1.png")
    Player_img= load_img("Rana.png")
    Car1_img= load_img("Car1.png")
    Car2_img= load_img("Car2.png")
    Camion_img= load_img("Camion.png")
    logs_img=load_img("short_log.png")
    loglong_img=load_img("longlog.png")
    
    

#=========Canvas
    
    Canvas1= tkinter.Canvas(Start, width=550,height=600)
    Canvas1.place(x=0,y=0)
        
    Canvas1.create_image(250,300, image=Fondo_juego)  #Pone fondo en canvas

    def Carril_medio(): #Crea los carros
        global Car01,Car02,Car03
        global Car11,Car12,Car13
        global Camion1,Camion2,Camion3
        global lista_final,lista_medio,lista_arriba,lisa_abajo
        global logs1,logs2,logs3
        global loglong1,loglong2,loglong3
        global log_short1,log_short2,log_short3
        Car01=Canvas1.create_image(0,500, image= Car1_img)
        Car02=Canvas1.create_image(150,500, image= Car1_img)
        Car03=Canvas1.create_image(450,500, image= Car1_img)
        lista_medio= [["Rojo", Car01],["Rojo",Car02],["Rojo",Car03]]  #Ingresa los carros en una lista 
                                                             #Crea los carros azules y pone en lista
        Car11=Canvas1.create_image(400,550, image= Car2_img)
        Car12=Canvas1.create_image(250,550, image= Car2_img)
        Car13=Canvas1.create_image(100,550, image= Car2_img)
        lista_abajo=[["Azul",Car11],["Azul",Car12],["Azul",Car13]]
                                                             #Crea los camiones
        Camion1= Canvas1.create_image(50,450,image=Camion_img)
        Camion2= Canvas1.create_image(250,450,image=Camion_img)
        Camion3= Canvas1.create_image(450,450,image=Camion_img)
        lista_arriba=[["Camion",Camion1],["Camion",Camion2],["Camion",Camion3]]

        logs1=Canvas1.create_image(0,150, image= logs_img)
        logs2=Canvas1.create_image(150,150, image= logs_img)
        logs3=Canvas1.create_image(450,150, image= logs_img)
        lago_medio= [["Corto", logs1],["Corto",logs2],["Corto",logs3]]  #Ingresa los troncos en una lista 
                                                             #Crea los troncos largos y pone en lista
        loglong1=Canvas1.create_image(400,200, image= loglong_img)
        loglong2=Canvas1.create_image(250,200, image= loglong_img)
        loglong3=Canvas1.create_image(100,200, image= loglong_img)
        lago_abajo=[["Largo",loglong1],["Largo",loglong2],["Largo",loglong3]]
                                                             #Crea los troncos
        log_short1= Canvas1.create_image(50,100,image=loglong_img)
        log_short2= Canvas1.create_image(250,100,image=loglong_img)
        log_short3= Canvas1.create_image(450,100,image=loglong_img)
        lago_arriba=[["Cortos",log_short1],["Cortos",log_short2],["Cortos",log_short3]]

        lista_final=[lista_medio,lista_abajo,lista_arriba,lago_medio,lago_abajo,lago_arriba]
        
#===========Mover Carros ===========#
    Player=Canvas1.create_image(0,600, image=Player_img)
        
    def mover_carro1(i):  #Funion para mover carros
        return aux_mover(i,i)
    def aux_mover(i,c):
        global lista_final  
        while Carros_Flag==True:  #Mientras el Flag este en true se muevan
            if i>len(lista_final)-1:
                return
            else:
                if c<=2:
                    choque()
                    Ahogado()
                    if lista_final[i][c][0]== "Rojo":   #Mueve la lista de los carros Rojos
                        if Canvas1.coords(lista_final[i][c][1])[0]<= 500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,500)
                        return aux_mover(i,c+1)
                    elif lista_final[i][c][0]== "Azul":   #Mueve la lista de los carros Azules
                        if Canvas1.coords(lista_final[i][c][1])[0]<= 500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,550)
                        return aux_mover(i,c+1)
                    elif lista_final[i][c][0]== "Camion":   #Mueve la lista de los carros Camiones
                        if Canvas1.coords(lista_final[i][c][1])[0]>=0:
                            Canvas1.move(lista_final[i][c][1],-25,0)
                        elif Canvas1.coords(lista_final[i][c][1])[0] <0:
                            Canvas1.coords(lista_final[i][c][1],500,450)
                        return aux_mover(i,c+1) 
                    elif lista_final[i][c][0]== "Corto":   #Mueve la lista de los troncos en el medio
                        if Canvas1.coords(lista_final[i][c][1])[0]>=0:
                            Canvas1.move(lista_final[i][c][1],-25,0)
                            sobre_tronco()
                        elif Canvas1.coords(lista_final[i][c][1])[0] <0:
                            Canvas1.coords(lista_final[i][c][1],500,150)
                        return aux_mover(i,c+1)
                    elif lista_final[i][c][0]== "Largo":   #Mueve la lista de los troncos de abajo
                        if Canvas1.coords(lista_final[i][c][1])[0]<= 500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                            sobre_tronco()
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,200)
                        return aux_mover(i,c+1)
                    elif lista_final[i][c][0]== "Cortos":   #Mueve la lista de los troncos de arriba
                        if Canvas1.coords(lista_final[i][c][1])[0]<=500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                            sobre_tronco()
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,100)
                        return aux_mover(i,c+1)
                else:
                    return aux_mover(i+1,0)
        
#=========Choques=================#
    def choque():
        global Player
        global Car01,Car02,Car03
        global Car11,Car12,Car13
        global Camion1,Camion2,Camion3
        global LIVES
        if Canvas1.coords(Car01)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car02)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
            Canvas2.delete(LIVES)
        elif Canvas1.coords(Car03)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car11)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car12)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car13)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion1)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion2)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion3)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            time.sleep(0.01)
            LIVES-=1
            respawn()
    #=========Ahogado================#
    def Ahogado():
        global logs1,logs2,logs3
        global loglong1,loglong2,loglong3
        global log_short1,log_short2,log_short3
        global LIVES
        global Player
        if Canvas1.coords(Player)[1]>60:
            if Canvas1.coords(Player)[1]<250:
                xlogs1=Canvas1.coords(logs1)[0]
                xlogs2=Canvas1.coords(logs2)[0]
                xlogs3=Canvas1.coords(logs3)[0]
                xloglong1=Canvas1.coords(loglong1)[0]
                xloglong2=Canvas1.coords(loglong2)[0]
                xloglong3=Canvas1.coords(loglong3)[0]
                xlog_short1=Canvas1.coords(log_short1)[0]
                xlog_short2=Canvas1.coords(log_short2)[0]
                xlog_short3=Canvas1.coords(log_short3)[0]
                if xloglong1==Canvas1.coords(Player)[0]or xloglong1+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xloglong2==Canvas1.coords(Player)[0]or xloglong2+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xloglong3==Canvas1.coords(Player)[0]or xloglong3+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlog_short1==Canvas1.coords(Player)[0]or xlog_short1-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlog_short2==Canvas1.coords(Player)[0]or xlog_short2-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlog_short3==Canvas1.coords(Player)[0]or xlog_short3-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlogs1==Canvas1.coords(Player)[0]or xlogs1-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlogs2==Canvas1.coords(Player)[0]or xlogs2-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlogs3==Canvas1.coords(Player)[0]or xlogs3-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                else:
                    LIVES-=1
                    Canvas1.delete(Player)
                    time.sleep(0.01)
                    respawn()

    #==========Sobre Tronco===========#
    def sobre_tronco():
        global logs1,logs2,logs3
        global loglong1,loglong2,loglong3
        global log_short1,log_short2,log_short3
        
        if Canvas1.coords(logs1)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(logs2)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(logs3)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(loglong1)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(loglong2)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(loglong3)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
            
        elif Canvas1.coords(log_short1)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(log_short2)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(log_short3)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
            
            
        
   #========Respawn==================#
    def respawn():
        if LIVES>0:
            print(LIVES)
            global Player
            Player=Canvas1.create_image(0,600,image=Player_img)
        elif LIVES ==0:
            game_over()

    #========== Winner ===================#
    def aux_Winner():
        Winner=Toplevel()
        Winner.minisize(width=100,height=100)
        Winner.resizable(width=False,height=False)
        Winner_Label(Winner,text="You win!").pack

    def Winner():
        global Player
        if Canvas1.coords(Player)[1]<=90:
            cordenadas=Canvas1.coords(Player)
            Canvas1.delete(Player)
            time.sleep(0.01)
            puntaje()
            respawn()
        else:
            return

    #====== Movimiento=============#
    def MOVIMIENTO(): #Inicia el movimiento de carros y troncos
        while True:
            mover_carro1(0)  #Funcion que mueve la listas de troncos y carros
            time.sleep(0.5)  #Que tan seguido ejecuta 

    #Gamer Over =======================================
    def aux_game_over():
        Game_ov= Toplevel()
        Game_ov.minsize(width=100,height=100)
        Game_ov.resizable(width=False,height=False)
        Game_Label= Label(Game_ov,text="Game Over Sucker").pack()
        
    def game_over():
        global LIVES, TIME_FLAG,Carros_Flag,TIEMPO,POINTS
        Canvas1.delete(ALL)
        lives=0
        TIME_FLAG== False
        Carros_Flag== False
        aux_game_over()
#============Timer ===================#
    def cronometro():
        vidas()
        global TIEMPO
        Canvas2.delete(ALL) #le hace un refresh al canvas y borra dato anterior
        TIEMPO=TIEMPO-1
        timepo=Canvas2.create_text(50,10, text=TIEMPO,fill="yellow",font="Cooper_black") #crea el tiempo en el canvas
        if TIEMPO==0: #Condicion de Finalizacion
            game_over()
        else:
            Canvas2.after(1000,cronometro) #define cada cuanto ejecuta cronometro
        
#=========== Canvas2 ==============#
    Canvas2=tkinter.Canvas(Start,width=550,height=30,bg="blue")
    Canvas2.place(x=-1,y=-1)

    global vidas
    Tiempo= Label(Canvas2,text="Time:",bg="black",fg="yellow").place(x=0,y=5)
    Vida= Label(Canvas2,text="Lives:",bg="black",fg="yellow").place(x=100,y=5)
    Score= Label(Canvas2,text="Score:",bg="black",fg="yellow").place(x=200,y=5)
    Level= Label(Canvas2,text="Level:",bg="black",fg="yellow").place(x=300,y=5)
    
 #=========== Vidas ==================#
    def vidas():  # Hace que se desplieguen las vidas en el GUI
        global LIVES
        if LIVES>=0:
            vidas= Label(Canvas2,text=LIVES,bg="black",fg="yellow").place(x=150,y=5)
        else:
            print(LIVES)
  #========= Puntaje ==============#
    def puntaje():
        global POINTS
        aux_puntaje()
        vidas= Label(Canvas2,text=POINTS,bg="black",fg="yellow").place(x=250,y=5)

    def aux_puntaje():
        global TIEMPO, POINTS, LEVEL,LIVES
        puntos=(LIVES*LEVEL-TIEMPO)+1000
        POINTS=puntos+POINTS
        print(POINTS)
        
        
        


            


#============ Threads ==================#
    def mover_carros_start():  #Thread para mover los carros
        mover1= Thread(target=MOVIMIENTO,args=())
        mover1.start()
    def timer():
        tiempo= Thread(target=cronometro,args=())
        tiempo.start()
        
        
   
#============ Movimiento ===============# 
    def MoveRight(event):  #Mueve hacia la derecha
        try:
            if Canvas1.coords(Player)[0]>=510:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,50,0)  #Mueve 42 pixeles
        except:
            print("Error Movimiento hacia derecha")

    def MoveLeft(event):  #Mueve hacia la izquierda
        try:
            if Canvas1.coords(Player)[0]<=15:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,-50,0)  #Mueve 42 pixeles
        except:
            print("Error Movimiento hacia izquierda")

    def MoveDown(event): #Mueve hacia abajo
        global POINTS
        try:
            if Canvas1.coords(Player)[1]>=600:  #Impide que se mueva si esta muy cerca del borde
                print ("No es la tecla")
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,0,50)  #Mueve 42 pixeles
        except:
            print("Error Movimiento hacia abajo")

    def MoveUp(event):  #Mueva hacia arriba
        Winner()
        global POINTS
        try:
            if Canvas1.coords(Player)[1]<=75:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,0,-50)  #Mueve 42 pixeles
        except:
            print("Error Movimiento hacia arriba")

    

#=========Para que funcionen las teclas
    Canvas1.bind("<Right>",MoveRight)
    Canvas1.bind("<Left>",MoveLeft)
    Canvas1.bind("<Up>",MoveUp)
    Canvas1.bind("<Down>",MoveDown)
    Canvas1.focus_set()


    def back():
        Start.withdraw()
        Menu.deiconify()
        
    Back_button=Button(Start,width=5,height=1, text="Back",command= back)
    Back_button.place(x=480,y=2)
    
    Carril_medio() #Lee la funcion con la creacion de los carros
    mover_carros_start() #Inicia el Thread de los carros
    Canvas2.after(1,timer) #Hace que comience el timer
    Start.mainloop()
    

   

    
    
#=================== Menu Window ==================================   

Menu= Tk() #Ventana Principal 
Menu.title("Frogger")  #Escribe titulo en la ventana
Menu.minsize(500,500) #Establece tamaño de la ventana
Menu.resizable(width=False,height=False) # Impide que modifiquen tamaño de ventana

Background=load_img("Menu.png") #Localiza imagen en fondo
Backg_Label= Label(Menu, image=Background)  #pone imagen en un label
Backg_Label.place(x=0,y=0)

#=========Imagenes de los Botones ==============================
imgbotton1= load_img("Start.png")  #Carga las imagenes de los botones
img_Label1= Label(Menu, image= imgbotton1) #Es el label para los botones

imgbotton2= load_img("Options.png")
img_Label2= Label(Menu, image= imgbotton2)

imgbotton3= load_img("Highscores.png")
img_Label3= Label(Menu, image= imgbotton3)

imgbotton4= load_img("Help.png")
img_Label4= Label(Menu, image= imgbotton4)

imgbotton5= load_img("About.png")
img_Label5= Label(Menu, image= imgbotton5)

imgbotton6= load_img("Exit.png")
img_Label6= Label(Menu, image= imgbotton6)

# ==============Botones en el menu ========================================
button1= Button(Menu,width=150,height=30,image=imgbotton1,command= Start )   #(donde, que dice, color) fg=frontground
button1.place(x=190,y=150)

button2= Button(Menu,width=150,height=30, image=imgbotton2)   
button2.place(x=190,y=210)                                   #Indica donde colocar el boton

button3= Button(Menu,width=150,height=30, image=imgbotton3)   
button3.place(x=190,y=270)

button4= Button(Menu,width=150,height=30, image=imgbotton4)   
button4.place(x=190,y=330)

button5= Button(Menu,width=150,height=30, image=imgbotton5)   
button5.place(x=190,y=390)

button6= Button(Menu,width=150,height=30, image=imgbotton6)   
button6.place(x=190,y=450)

Menu.mainloop()
