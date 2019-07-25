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


def read_file(): #Lee los HighScores
        global P1,P1_SCORE,P1_LEVEL,P2,P2_SCORE,P2_LEVEL,P3,P3_SCORE,P3_LEVEL
        file = open("highscores.txt","r")
        file.seek(1)
        P1= file.read(6)                    #PLAYER 1
        file.seek(8)
        P1_SCORE= file.read(4)             
        file.seek(13)
        P1_LEVEL= file.read(2)              

        file.seek(19)
        P2= file.read(6)                    #PLAYER 2
        file.seek(26)
        P2_SCORE= file.read(4)             
        file.seek(31)
        P2_LEVEL= file.read(2)              

        file.seek(37)
        P3= file.read(6)                    #PLAYER 3
        file.seek(44)
        P3_SCORE= file.read(4)              
        file.seek(49)
        P3_LEVEL= file.read(2)             
        file.close()#Se cierra el archivo


#==================== Start Window ==================================#
Carros_Flag=True          #Se definen las variables necesarias para la
TIME_FLAG=True            # ejecución del programa
TIEMPO=180
LIVES=7
POINTS=0
TRONCO_FLAG=True
LEVEL=1
CASITAS=[0,0,0,0,0]
SPEED=0.7

#========== Nickname Window================#

def Name():#Ventana que pide el nombre de usuario
    def go():
        global Jugador
        nick=nom.get()
        Jugador=nick
        print(Jugador)
        print("El numero de caracteres ingresadors es:"+str(len(nick)))
        if restriction(nick)==True:
            Name.destroy()
            Start()
        else:
            print("Error: El nickname debe ser de 6 caracteres.")

    def restriction(nick):#Restricción del entry,tiene que ser de 6 dígitos
        if len(nick)!=6:
            return False
        else:
            return True
    
    Menu.withdraw()
    Name=Toplevel(bg="black")
    Name.geometry("200x200+250+50")
    Name.resizable(width=False,height=False)
    nick=Label(Name,bg="black",fg="yellow",text="Enter your nickname").place(x=50,y=20)
    nom=StringVar()
    nickb=Entry(Name,textvariable=nom).place(x=45,y=40)
    
    bstart=Button(Name,text="Continue",command=go).place(x=50,y=100)

    Name.mainloop()
    

    

def Start():
    global Player
    Menu.withdraw() #Extrae la ventana de menu
    music_stop() # Detiene la musica
    
    Start= Toplevel()  #Crea una nueva ventana
    Start.minsize(width=550,height=600)  #Define el tamaño
    Start.resizable(width=False,height=False)


#=========Imagenes

    Fondo_juego= load_img("Fondo_juego editador1.png") #Se cargan todas las imagenes que se utilizan en
    Player_img= load_img("frognueva.png")               #el juego
    Car1_img= load_img("Car1.png")
    Car2_img= load_img("Car2.png")
    Camion_img= load_img("Camion.png")
    logs_img=load_img("short_log.png")
    loglong_img=load_img("longlog.png")
    Win_img=load_img("Winningfinal.png")
    bgover=load_img("lost1.png")
    
    
    

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
        global Mixto1,Mixto2,Mixto3
        global log_mix1,log_mix2,log_mix3
        global los_mixtos1,los_mixtos2,los_mixtos3
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

        Mixto1=Canvas1.create_image(50,400,image= Car2_img)
        Mixto2=Canvas1.create_image(200,400,image= Car1_img)
        Mixto3=Canvas1.create_image(400,400,image= Car2_img)
        lista_mixta=[["Mixta",Mixto1],["Mixta",Mixto2],["Mixta",Mixto3]]

        logs1=Canvas1.create_image(50,150, image= logs_img)
        logs2=Canvas1.create_image(250,150, image= logs_img)
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

        log_mix1= Canvas1.create_image(50,300,image=loglong_img)
        log_mix2= Canvas1.create_image(200,300,image=loglong_img)
        log_mix3= Canvas1.create_image(350,300,image=loglong_img)
        lago_mixta=[["Troncos",log_mix1],["Troncos",log_mix2],["Troncos",log_mix3]]

        los_mixtos1=Canvas1.create_image(50,250,image=logs_img)
        los_mixtos2=Canvas1.create_image(250,250,image=logs_img)
        los_mixtos3=Canvas1.create_image(450,250,image=logs_img)
        lago_largo_mixta=[["Troncos_largos",los_mixtos1],["Troncos_largos",los_mixtos2],["Troncos_largos",los_mixtos3]]

        #Lista con todos los elementos a mover
        lista_final=[lista_medio,lista_abajo,lista_arriba,lista_mixta,lago_medio,lago_abajo,lago_arriba,lago_mixta,lago_largo_mixta]
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
                    elif lista_final[i][c][0]== "Mixta":
                        if Canvas1.coords(lista_final[i][c][1])[0]<= 500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,400)
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
                    elif lista_final[i][c][0]== "Troncos":   #Mueve la lista de los troncos de arriba
                        if Canvas1.coords(lista_final[i][c][1])[0]<=500:
                            Canvas1.move(lista_final[i][c][1],25,0)
                            sobre_tronco()
                        elif Canvas1.coords(lista_final[i][c][1])[0] >500:
                            Canvas1.coords(lista_final[i][c][1],0,300)
                        return aux_mover(i,c+1)
                    elif lista_final[i][c][0]== "Troncos_largos":   #Mueve la lista de los troncos en el medio
                        if Canvas1.coords(lista_final[i][c][1])[0]>=0:
                            Canvas1.move(lista_final[i][c][1],-25,0)
                            sobre_tronco()
                        elif Canvas1.coords(lista_final[i][c][1])[0] <0:
                            Canvas1.coords(lista_final[i][c][1],500,250)
                        return aux_mover(i,c+1)                    
                else:
                    return aux_mover(i+1,0)
        
#=========Choques=================#
    def choque(): #Se define la función de los choques
        global Player
        global Car01,Car02,Car03
        global Car11,Car12,Car13
        global Camion1,Camion2,Camion3
        global Mixto1,Mixto2,Mixto3
        global LIVES
        if Canvas1.coords(Car01)== Canvas1.coords(Player): #Si las coordenadas coinciden
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn() #Hace que la rana aparesca en el pricipio otra vez
        elif Canvas1.coords(Car02)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
            Canvas2.delete(LIVES)
        elif Canvas1.coords(Car03)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car11)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car12)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Car13)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion1)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion2)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Camion3)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Mixto1)== Canvas1.coords(Player): #Aqui
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Mixto2)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
        elif Canvas1.coords(Mixto3)== Canvas1.coords(Player):
            Canvas1.delete(Player)
            winsound.PlaySound("choque1.wav",winsound.SND_ASYNC)
            time.sleep(0.01)
            LIVES-=1
            respawn()
    #=========Ahogado================#
    def Ahogado(): #Hace que la rana se muera si no se encuentre sobre un tronco
        global logs1,logs2,logs3
        global loglong1,loglong2,loglong3
        global log_short1,log_short2,log_short3
        global log_mix1,log_mix2,log_mix3
        global los_mixtos1,los_mixtos2,los_mixtos3
        global LIVES
        global Player
        if Canvas1.coords(Player)[1]>60:
            if Canvas1.coords(Player)[1]<350:
                xlogs1=Canvas1.coords(logs1)[0]
                xlogs2=Canvas1.coords(logs2)[0]
                xlogs3=Canvas1.coords(logs3)[0]
                xloglong1=Canvas1.coords(loglong1)[0]
                xloglong2=Canvas1.coords(loglong2)[0]
                xloglong3=Canvas1.coords(loglong3)[0]
                xlog_short1=Canvas1.coords(log_short1)[0]
                xlog_short2=Canvas1.coords(log_short2)[0]
                xlog_short3=Canvas1.coords(log_short3)[0]
                xlog_mix1=Canvas1.coords(log_mix1)[0]
                xlog_mix2=Canvas1.coords(log_mix2)[0]
                xlog_mix3=Canvas1.coords(log_mix3)[0]
                xlos_mixtos1=Canvas1.coords(los_mixtos1)[0] #negativo
                xlos_mixtos2=Canvas1.coords(los_mixtos2)[0]
                xlos_mixtos3=Canvas1.coords(los_mixtos3)[0]
                
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
                elif xlog_mix1==Canvas1.coords(Player)[0] or xlog_mix1+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlog_mix2==Canvas1.coords(Player)[0] or xlog_mix2+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlog_mix3==Canvas1.coords(Player)[0] or xlog_mix3+25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlos_mixtos1==Canvas1.coords(Player)[0]or xlos_mixtos1-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlos_mixtos2==Canvas1.coords(Player)[0]or xlos_mixtos2-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                elif xlos_mixtos3==Canvas1.coords(Player)[0]or xlos_mixtos3-25==Canvas1.coords(Player)[0]:
                    sobre_tronco()
                
                else:
                    LIVES-=1
                    Canvas1.delete(Player)
                    winsound.PlaySound("Ahogado1.wav",winsound.SND_ASYNC)
                    time.sleep(0.01)
                    respawn()

    #==========Sobre Tronco===========#
    def sobre_tronco():#Movimiento mientras la rana se encuentra sobre los troncos
        global logs1,logs2,logs3
        global loglong1,loglong2,loglong3
        global log_short1,log_short2,log_short3
        global log_mix1,log_mix2,log_mix3
        global los_mixtos1,los_mixtos2,los_mixtos3
        
        if Canvas1.coords(logs1)==Canvas1.coords(Player):#Se mueve junto al tronco -25
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(logs2)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(logs3)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(loglong1)==Canvas1.coords(Player):#Se mueve junto al trocon 25
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
        elif Canvas1.coords(log_mix1)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(log_mix2)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(log_mix3)==Canvas1.coords(Player):
            Canvas1.move(Player,25,0)
        elif Canvas1.coords(los_mixtos1)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(los_mixtos2)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
        elif Canvas1.coords(los_mixtos3)==Canvas1.coords(Player):
            Canvas1.move(Player,-25,0)
            
            
            
        
   #========Respawn==================#
    def respawn():#Devuleve la rana al punto de inicio
        if LIVES>0:#Si las vidas osn mayores a 0 sigue el programa
            print(LIVES)
            global Player
            Player=Canvas1.create_image(0,600,image=Player_img)
        elif LIVES ==0:#Si se queda sin vidas abre el game over
            game_over()

    #========== Winner ===================#
    def aux_Winner():#Se abre el winner cuando se llenan todas las casillas de las ranas
        Winner=Toplevel()#Se crea la ventana del winner
        Winner.geometry("500x300+100+50")
        Winner.resizable(width=False,height=False)
        Winner.title("Congratulations")
        label_frog=Label(Winner,image=Win_img).pack()

        def back():
            Winner.destroy()
            Menu.deiconify()
            play_music()
        

    def Winner(): #Funcion que hace que sume al puntaje y devuelva la rana
        global Player, CASITAS,POINTS,LIVES,LEVEL,TIEMPO
        if CASITAS==[1,1,1,1,1]:
            TIME_FLAG== False
            Carros_Flag== False
            Highscores()
            aux_Winner()
        else:
            if Canvas1.coords(Player)[1]==50: # Verifica si la rana esta en las Casitas de ganar
                print(Canvas1.coords(Player))
                if 50<Canvas1.coords(Player)[0]<100: #Primera casita
                    if CASITAS[0]==0: #Verifica si aun no se ha llenado
                        time.sleep(0.01)
                        puntaje()
                        respawn()
                        CASITAS[0]=1
                        print(CASITAS)
                        if CASITAS==[1,1,1,1,1]:
                            TIME_FLAG== False
                            Carros_Flag== False
                            Highscores()
                            aux_Winner()
                        else:
                            return
                        print(CASITAS)
                    else:
                        respawn()
                
                elif 150<Canvas1.coords(Player)[0]<200: #Segunda casita
                    if CASITAS[1]==0: #Verifica si aun no se ha llenado
                        time.sleep(0.01)
                        puntaje()
                        respawn()
                        CASITAS[1]=1
                        print(CASITAS)
                        if CASITAS==[1,1,1,1,1]:
                            TIME_FLAG== False
                            Carros_Flag== False
                            Highscores()
                            aux_Winner()
                        else:
                            return
                        print(CASITAS)
                    else: 
                       respawn()
                elif 250<Canvas1.coords(Player)[0]<300: #Segunda casita
                    if CASITAS[2]==0: #Verifica si aun no se ha llenado
                        time.sleep(0.01)
                        puntaje()
                        respawn()
                        CASITAS[2]=1
                        print(CASITAS)
                        if CASITAS==[1,1,1,1,1]:
                            TIME_FLAG== False
                            Carros_Flag== False
                            Highscores()
                            aux_Winner()
                        else:
                            return 
                        print(CASITAS)
                    else:
                        respawn()
                elif 350<Canvas1.coords(Player)[0]<400: #Segunda casita
                    if CASITAS[3]==0: #Verifica si aun no se ha llenado
                        time.sleep(0.01)
                        puntaje()
                        respawn()
                        CASITAS[3]=1
                        print(CASITAS)
                        if CASITAS==[1,1,1,1,1]:
                            TIME_FLAG== False
                            Carros_Flag== False
                            Highscores()
                            aux_Winner()
                        else:
                            return
                        print(CASITAS)
                    else:
                        respawn()
                elif 450<Canvas1.coords(Player)[0]<500: #Segunda casita
                    if CASITAS[4]==0: #Verifica si aun no se ha llenado
                        time.sleep(0.01)
                        puntaje()
                        respawn()
                        CASITAS[4]=1
                        print(CASITAS)
                        if CASITAS==[1,1,1,1,1]:
                            TIME_FLAG== False
                            Carros_Flag== False
                            Highscores()
                            aux_Winner()
                        else:
                            return
                    else:
                        respawn()
                else:
                    Canvas1.delete(Player)
                    respawn()
                    
            else:
                
                return

    #====== Movimiento=============#
    def MOVIMIENTO(): #Inicia el movimiento de carros y troncos
        while True:
            mover_carro1(0)  #Funcion que mueve la listas de troncos y carros
            time.sleep(SPEED)  #Que tan seguido ejecuta

    #Gamer Over =======================================
    def aux_game_over():#Ventana que despliega al perder
        Game_ov= Toplevel()
        Game_ov.minsize(width=400,height=300)
        Game_ov.resizable(width=False,height=False)
        Game_Label= Label(Game_ov,image=bgover).place(x=0,y=0)
        def reboot():#Reinicia el juego
            Start.destroy()
            Game_ov.destroy()
            Menu.deiconify()
            
        Game_Bot=Button(Game_ov,text="Menu",command=reboot).place(x=300,y=250)
    
        
    def game_over():
        global LIVES, TIME_FLAG,Carros_Flag,TIEMPO,POINTS
        TIME_FLAG== False
        Carros_Flag== False
        thread=Thread(target=aux_game_over,args=())
        thread.start()
        Highscores()
        time.sleep(3600)
        
        

    #===============Retirar Highscore================#
    def Highscores():#Creación de los mejores puntajes
        read_file()
        global P1_SCORE,P2_SCORE,P3_SCORE
        global POINTS,LEVEL
        file = open("highscores.txt","r+")
        print(POINTS)
        if (int(POINTS)>int(P1_SCORE)) == True:             #COMPARACION CON EL SCORE 1
            file.seek(1)
            file.write(player)
            print(P1_SCORE)
            file.seek(8)
            if POINTS < 100: #Si el score es menor a 100 completa con 00
                POINTS_local ="00"+str(POINTS)
                file.write(str(POINTS_local))
            elif POINTS > 100 and POINTS <1000:#sino con un 0
                POINTS_local= "0"+str(POINTS)
                file.write(str(POINTS_local))
            else:
                file.write(str(POINTS))
            file.seek(13)
            if LEVEL < 10:
                LEVEL_local= "0"+str(LEVEL)
                file.write(str(LEVEL_local))
        elif (int(POINTS)>int(P2_SCORE)) == True:
            file.seek(19)
            file.write(player)
            print(P2_SCORE)
            file.seek(26)
            if POINTS < 100:
                POINTS_local ="00"+str(POINTS)
                file.write(str(POINTS_local))
            elif POINTS > 100 and POINTS <1000:
                POINTS_local= "0"+str(POINTS)
                file.write(str(POINTS_local))
            else:
                file.write(str(POINTS))
            file.seek(31)
            if LEVEL < 10:
                LEVEL_local= "0"+str(LEVEL)
                file.write(str(LEVEL_local))  
        elif (int(POINTS) > int(P3_SCORE)) == True:
            file.seek(37)
            file.write(player)
            print(P1_SCORE)
            file.seek(44)
            if POINTS < 100:
                POINTS_local ="00"+str(POINTS)
                file.write(str(POINTS_local))
            elif POINTS > 100 and POINTS <1000:
                POINTS_local= "0"+str(POINTS)
                file.write(str(POINTS_local))
            else:
                file.write(str(POINTS))
            file.seek(49)
            if LEVEL < 10:
                LEVEL_local= "0"+str(LEVEL)
                file.write(str(LEVEL_local))
        file.close()
        
#============Timer ===================#
    def cronometro(): #Se define el cronómetro del juego
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
    Canvas2=tkinter.Canvas(Start,width=550,height=30,bg="black")
    Canvas2.place(x=-1,y=-1)

    global vidas, Jugador,LEVEL
    Tiempo= Label(Canvas2,text="Time:",bg="black",fg="yellow").place(x=0,y=5)
    Vida= Label(Canvas2,text="Lives:",bg="black",fg="yellow").place(x=100,y=5)
    Score= Label(Canvas2,text="Score:",bg="black",fg="yellow").place(x=200,y=5)
    Level= Label(Canvas2,text="Level:",bg="black",fg="yellow").place(x=300,y=5)
    print(Jugador)
    PlayerN= Label(Canvas2,text=Jugador,bg="black",fg="yellow").place(x=400,y=5)
    Level_num=Label(Canvas2,text=LEVEL,bg="black",fg="yellow").place(x=350,y=5)
    
    
 #=========== Vidas ==================#
    def vidas():  # Hace que se desplieguen las vidas en el GUI
        global LIVES
        if LIVES>=0:
            vidas= Label(Canvas2,text=LIVES,bg="black",fg="yellow").place(x=150,y=5)
        else:
            print(LIVES)
  #========= Puntaje ==============#
    def puntaje(): #Lo despliega en la ventana del juego
        global POINTS
        aux_puntaje()
        vidas= Label(Canvas2,text=POINTS,bg="black",fg="yellow").place(x=250,y=5)

    def aux_puntaje():#Calcula el puntaje
        global TIEMPO, POINTS, LEVEL,LIVES
        puntos=(LIVES*LEVEL-TIEMPO)+1000
        POINTS=puntos+POINTS
        print(POINTS)
        

#============ Threads ==================#
    def mover_carros_start():  #Thread para mover los carros
        global mover1
        mover1= Thread(target=MOVIMIENTO,args=())
        mover1.start()
    def timer():
        global LIVES,TIEMPO,POINTS
        global tiempo
        POINTS=0
        LIVES=7
        TIEMPO=180
        tiempo= Thread(target=cronometro,args=())
        tiempo.start()
        
        
   
#============ Movimiento ===============# 
    def MoveRight(event):  #Mueve hacia la derecha
        try:
            if Canvas1.coords(Player)[0]>=510:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,50,0)  #Mueve 50 pixeles
                winsound.PlaySound("movement1.wav",winsound.SND_ASYNC)
        except:
            print("Error Movimiento hacia derecha")

    def MoveLeft(event):  #Mueve hacia la izquierda
        try:
            if Canvas1.coords(Player)[0]<=15:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,-50,0)  #Mueve 50 pixeles
                winsound.PlaySound("movement1.wav",winsound.SND_ASYNC)
        except:
            print("Error Movimiento hacia izquierda")

    def MoveDown(event): #Mueve hacia abajo
        global POINTS
        try:
            if Canvas1.coords(Player)[1]>=600:  #Impide que se mueva si esta muy cerca del borde
                print ("No es la tecla")
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,0,50)  #Mueve 50 pixeles
                winsound.PlaySound("movement1.wav",winsound.SND_ASYNC)
        except:
            print("Error Movimiento hacia abajo")

    def MoveUp(event):  #Mueva hacia arriba
        global POINTS
        try:
            if Canvas1.coords(Player)[1]<=75:  #Impide que se mueva si esta muy cerca del borde
                Canvas1.move(Player ,0,0)
            else:
                Canvas1.move(Player ,0,-50)  #Mueve 50 pixeles
                winsound.PlaySound("movement1.wav",winsound.SND_ASYNC)
                Winner()
        except:
            print("Error Movimiento hacia arriba")

    

#=========Para que funcionen las teclas
    Canvas1.bind("<Right>",MoveRight)
    Canvas1.bind("<Left>",MoveLeft)
    Canvas1.bind("<Up>",MoveUp)
    Canvas1.bind("<Down>",MoveDown)
    Canvas1.focus_set()


    def back():#Vuelve al menu
        Start.withdraw()
        Menu.deiconify()
        play_music()

    # ============== Musica ==========#

    
    Back_button=Button(Start,width=5,height=1, text="Back",command= back)
    Back_button.place(x=480,y=2)
    
    Carril_medio() #Lee la funcion con la creacion de los carros
    mover_carros_start() #Inicia el Thread de los carros
    Canvas2.after(1,timer) #Hace que comience el timer
    Start.mainloop()
    

   


#=============== Options Window ===============#
def options():
    Menu.withdraw()
    music_stop()
    options=Toplevel()#Options
    options.title("Options")
    options.geometry("530x420+100+50")
    options.resizable(width=False,height=False)
    optbg=load_img("Helpimg.png")
    bgopt= Label(options,image=optbg).place(x=0,y=0)

    nivf=Radiobutton(options,value=1,command=sel1).place(x=55,y=150)#Radiobuttons para elegir el nivel
    nivm=Radiobutton(options,value=2,command=sel2).place(x=260,y=150)
    nivi=Radiobutton(options,value=3,command=sel3).place(x=445,y=150)
    def menuo():#Vuelve al menu
        options.destroy()
        Menu.deiconify()
        play_music()
    botmo=Button(options,text="Menu",command=menuo).place(x=10,y=390)

    options.mainloop()
def sel1():#Define la velocidad del juego según lo elegido
    global SPEED
    SPEED=0.7
def sel2():
    global SPEED
    SPEED=0.4
def sel3():
    global SPEED
    SPEED=0.1
#=======================About================#
def about():#Ventana de información
    Menu.withdraw()
    music_stop()
    about=Toplevel()
    about.title("About")
    about.geometry("515x500+100+50")
    about.resizable(width=False,height=False)
    abbg=load_img("bgab2.png")
    abpt=Label(about,image=abbg).place(x=0,y=0)

    def menab():
        about.destroy()
        Menu.deiconify()
        play_music()

    botn=Button(about,text="Menu",command=menab).place(x=400,y=450)

    about.mainloop()

#=============== Scores ================#
def scores():#Ventana donde se muestran los secores
    Menu.withdraw()
    music_stop()
    scores=Toplevel()#Highscores
    scores.title("Highscores")
    scores.geometry("600x600+100+50")
    scores.resizable(width=False,height=False)
    scores.focus_set()
    fondo_high=load_img("Highscores1.png")
    fondo_label=Label(scores,image=fondo_high)
    fondo_label.place(x=0,y=0)

    def print_scores():
        Player1= Label(scores, text=P1,bg="black",fg="white")
        Player1.place(x=200,y=300)
        Player1= Label(scores, text=P1_SCORE,bg="black",fg="white")
        Player1.place(x=300,y=300)

        Player2= Label(scores, text=P2,bg="black",fg="white")
        Player2.place(x=200,y=400)
        Player2= Label(scores, text=P2_SCORE,bg="black",fg="white")
        Player2.place(x=300,y=400)

        Player3= Label(scores, text=P3,bg="black",fg="white")
        Player3.place(x=200,y=500)
        Player3= Label(scores, text=P3_SCORE,bg="black",fg="white")
        Player3.place(x=300,y=500)
        
    

    def Return1():
        scores.destroy()
        Menu.deiconify()
        play_music()
        
    but=Button(scores,text="Menu",command= Return1).place(x=10,y=550)
    read_file()
    print_scores()
    scores.mainloop()
    
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


imgbotton5= load_img("About.png")
img_Label5= Label(Menu, image= imgbotton5)

imgbotton6= load_img("Exit.png")
img_Label6= Label(Menu, image= imgbotton6)


# ==============Botones en el menu ========================================
button1= Button(Menu,width=150,height=30,image=imgbotton1,command= Name )   #(donde, que dice, color) fg=frontground
button1.place(x=190,y=150)

button2= Button(Menu,width=150,height=30,command=options, image=imgbotton2)   
button2.place(x=190,y=210)                                   #Indica donde colocar el boton

button3= Button(Menu,width=150,height=30,command=scores,image=imgbotton3)   
button3.place(x=190,y=270)

button5= Button(Menu,width=150,height=30,command=about, image=imgbotton5)   
button5.place(x=190,y=320)

button6= Button(Menu,width=150,height=30, image=imgbotton6,command=exit)   
button6.place(x=190,y=380)

def musica():
    winsound.PlaySound("Frogger_Menu.wav",winsound.SND_ASYNC)
def music_stop():
    winsound.PlaySound(None,0)
def play_music():
    music_thread=Thread(target=musica,args=())
    music_thread.daemon = True
    music_thread.start()

play_music()

Menu.mainloop()


##TO-DO
##Ventana fea de pedir nickname
##poner el loading al inicio del juego
##QUITAR EL COMENTARIODE AHOGADO
##
##
