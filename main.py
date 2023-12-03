import tkinter as tk
import tkinter.ttk as ttk
import pygame
from PIL import Image, ImageTk
from threading import Thread
from time import sleep
import time
import sqlite3
import random


t = 1 #le t est egale a 1 parseque l'ecran de qui suit les music et la par defaut s
h = 0
n = 0
onpage = 0
current_frame = None
chanson_en_cours = ''
button_state = 0  # 0 for play, 1 for pause
def switch(page_function):
    # Détruire tous les widgets dans le main_frame
    for widget in main_fm.winfo_children():
        widget.destroy()
    #puis sa vient faire un callback pour generer sur la main_fm la frame qui a dans la function event qui est relier au button de la frame en question 
    page_function()#c'est la function lambda (qui est une fonction avec la frame en question) a qui va genere la frame qui est relier au button corespondant

def home_page():
    
    global n 

    #color of all the background of the home page
    root.config(bg='#0F2140')#bg of the root
    canvas1.config(bg='#404040')#nav bar
   
   
    home_page_fm = tk.Frame(main_fm, bg='#272727')
    home_page_lb = tk.Label(home_page_fm, text='home page', bg='#0F2140', fg = 'white')
    home_page_lb.pack(pady=80)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Sélectionnez les trois chansons les plus écoutées en ordre décroissant
    cursor.execute("SELECT DISTINCT chanson, nombre_ecoutes FROM Ecoutes ORDER BY nombre_ecoutes DESC")


    # Récupérez les résultats
    resultats = cursor.fetchall()

    # Affichez les trois chansons les plus écoutées
    titres_plus_ecoutes = []

    # Parcourez les résultats et ajoutez les trois titres les plus écoutés à la liste
    for index, (chanson, nombre_ecoutes) in enumerate(resultats, start=1):
        print(f"{index}. Chanson : {chanson}, Nombre d'écoutes : {nombre_ecoutes}")
        # Ajoutez le titre à la liste
        titres_plus_ecoutes.append(chanson)
        # Si nous avons déjà ajouté trois titres, sortez de la boucle
        if index == 3:
           break


    # Fermez la connexion à la base de données
    conn.close()


   #3-pic of icon nav bar
    sp9 = Image.open("home.png")
    global Sp9 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp9 = ImageTk.PhotoImage(sp9)

   #3-pic of icon nav bar
    sp10 = Image.open("musique.png")
    global Sp10 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp10 = ImageTk.PhotoImage(sp10)

    #3-pic of icon nav bar
    sp13 = Image.open("playist-2.png")
    global Sp13 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp13 = ImageTk.PhotoImage(sp13)



    def get_time_of_day():
       current_time = time.localtime()
       hour = current_time.tm_hour
    
       if 5 <= hour < 12:
           return "hello ! good morning 🌅 ."
       elif 12 <= hour < 18:
           return "hello ! good afternoon ☕ ."
       else:
          return "hello ! good evening 🌆 ."
    #update du message tous les 6 s 
    def update_message():
       message = get_time_of_day()
       message_label.config(text=message)
       message_label.after(60000, update_message)  # Met à jour toutes les 60 secondes (1 minute)
    

    message_label = tk.Label(home_page_fm,bg='#272727',fg='white' ,text="", font=('Garamond', 20))
    message_label.place(relx = 0.05, rely=0.02)

    update_message()  # Lance la mise à jour automatique du message
    #changement de l'image de la nav bar pour que sa montre dans quel frame je suis
    global homeButton
    canvas1.itemconfig(homeButton, image=Sp9)
     
    global lecteurButton
    canvas1.itemconfig(lecteurButton, image=Sp10)

    global playistButton
    canvas1.itemconfig(playistButton, image=Sp13)

    #la mainframe c'est la frame qui contient la frame1 et la frame2 et il y'a les deux fleche sur le cote pour le passage de frame 

    Mainframe = tk.Frame(home_page_fm, bg='gray', width=420, height=100)
    title_font2 = ('Georgia', 16)

    frame1 = tk.Frame(Mainframe, bg='#404040', width=350, height=120)


   #ces image sont pour jour l'animation des point qui te situe dans quel frame tu es
    global canvas_Point_icon
    canvas_Point_icon = tk.Canvas(frame1, width=60, height=20, bg='#404040', highlightthickness=0)#highlightthickness c'est pour enlever la ligne blanche qui entre le main_fm et le option_fm qui enfait un border
    canvas_Point_icon.place(relx=0.93, rely=0.10, anchor= 'center')

    point1 = Image.open("point-1.png")
    resized_image1 = point1.resize((10, 10))
    global Point1 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Point1 = ImageTk.PhotoImage(resized_image1)

    global Pointicon
    Pointicon = canvas_Point_icon.create_image(20, 10, image=Point1)
    canvas_Point_icon.tag_bind(Pointicon, "<Button-1>")


    point2 = Image.open("point-2.png")
    resized_image2 = point2.resize((10, 10))
    global Point2 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Point2 = ImageTk.PhotoImage(resized_image2)

    global Pointicon2
    Pointicon2 = canvas_Point_icon.create_image(40, 10, image=Point2)
    canvas_Point_icon.tag_bind(Pointicon2, "<Button-1>")





    current_frame = frame1
    current_frame.grid()

    frame2 = tk.Frame(Mainframe, bg='#404040', width=350, height=120)
    def create_labels_on_frame2():


      global canvas_Point_icon2
      canvas_Point_icon2 = tk.Canvas(frame2, width=60, height=20, bg='#404040', highlightthickness=0)#highlightthickness c'est pour enlever la ligne blanche qui entre le main_fm et le option_fm qui enfait un border
      canvas_Point_icon2.place(relx=0.93, rely=0.10, anchor= 'center')

      point3 = Image.open("point-2.png")
      resized_image3 = point3.resize((10, 10))
      global Point3 # Nécessaire pour éviter la suppression des références des images par le garbage collector
      Point3 = ImageTk.PhotoImage(resized_image3)

      global Pointicon3
      Pointicon3 = canvas_Point_icon2.create_image(20, 10, image=Point3)
      canvas_Point_icon2.tag_bind(Pointicon3, "<Button-1>")


      point4 = Image.open("point-1.png")
      resized_image4 = point4.resize((10, 10))
      global Point4 # Nécessaire pour éviter la suppression des références des images par le garbage collector
      Point4 = ImageTk.PhotoImage(resized_image4)

      global Pointicon4
      Pointicon4 = canvas_Point_icon2.create_image(40, 10, image=Point4)
      canvas_Point_icon2.tag_bind(Pointicon4, "<Button-1>")


      global canvas_classement
      canvas_classement = tk.Canvas(frame2, width=290, height=110, bg='#404040', highlightthickness=0)#highlightthickness c'est pour enlever la ligne blanche qui entre le main_fm et le option_fm qui enfait un border
      canvas_classement.place(relx=0.43, rely=0.55, anchor= 'center')

      first_titre = titres_plus_ecoutes[0]
      second_titre = titres_plus_ecoutes[1]
      third_titre = titres_plus_ecoutes[2]

      
      if first_titre == 'Before you go':
            first = Image.open("cover-1.png")
      if first_titre == 'Money In The Grave':
            first = Image.open("cover-2.png")
      if first_titre == 'Mash up':
            first = Image.open("cover-3.png")
      if first_titre == 'Stressed Out':
            first = Image.open("cover-6.png")
      if first_titre == 'Mount Everest':
            first = Image.open("cover-7.png")
      if first_titre ==  'In The Stars':
            first = Image.open("cover-8.png")
      if first_titre ==  '7Years':
            first = Image.open("cover-9.png")
      if first_titre == 'love Nwantiti':
            first = Image.open("cover-10.png")
      if first_titre == 'Lovely':
            first = Image.open("cover-11.png")
      if first_titre == 'i Hate you':
            first = Image.open("cover-11.png")


      if second_titre == 'Before you go':
            second = Image.open("cover-1.png")
      if second_titre == 'Money In The Grave':
            second = Image.open("cover-2.png")
      if second_titre == 'Mash up':
            second = Image.open("cover-3.png")
      if second_titre == 'Stressed Out':
            second = Image.open("cover-6.png")
      if second_titre == 'Mount Everest':
            second = Image.open("cover-7.png")
      if second_titre ==  'In The Stars':
            second = Image.open("cover-8.png")
      if second_titre ==  '7Years':
            second = Image.open("cover-9.png")
      if second_titre == 'love Nwantiti':
            second = Image.open("cover-10.png")
      if second_titre == 'Lovely':
            second = Image.open("cover-11.png")
      if second_titre == 'i Hate you':
            second = Image.open("cover-11.png")

      if third_titre == 'Before you go':
            third = Image.open("cover-1.png")
      if third_titre == 'Money In The Grave':
            third = Image.open("cover-2.png")
      if third_titre == 'Mash up':
            third = Image.open("cover-3.png")
      if third_titre == 'Stressed Out':
            third = Image.open("cover-6.png")
      if third_titre == 'Mount Everest':
            third = Image.open("cover-7.png")
      if third_titre ==  'In The Stars':
            third = Image.open("cover-8.png")
      if third_titre ==  '7Years':
            third = Image.open("cover-9.png")
      if third_titre == 'love Nwantiti':
            third = Image.open("cover-10.png")
      if third_titre == 'Lovely':
            third = Image.open("cover-11.png")
      if third_titre == 'i Hate you':
            third = Image.open("cover-11.png")
            

      resized_image6 = first.resize((50, 50))
      global First # Nécessaire pour éviter la suppression des références des images par le garbage collector
      First = ImageTk.PhotoImage(resized_image6)

      podium = Image.open("podium.png")
      resized_image9 = podium.resize((250, 100))
      global Podium # Nécessaire pour éviter la suppression des références des images par le garbage collector
      Podium = ImageTk.PhotoImage(resized_image9)

      global first_song
      first_song = canvas_classement.create_image(140, 27, image=First)
      canvas_classement.tag_bind(first_song, "<Button-1>")

      global podium_song
      podium_song = canvas_classement.create_image(140, 80, image=Podium)
      canvas_classement.tag_bind(podium_song, "<Button-1>")

      resized_image7 = second.resize((50, 50))
      global Second # Nécessaire pour éviter la suppression des références des images par le garbage collector
      Second = ImageTk.PhotoImage(resized_image7)


      global second_song
      second_song = canvas_classement.create_image(55, 35, image=Second)
      canvas_classement.tag_bind(second_song, "<Button-1>")

      resized_image8 = third.resize((50, 50))
      global Third# Nécessaire pour éviter la suppression des références des images par le garbage collector
      Third = ImageTk.PhotoImage(resized_image8)

      global third_song
      third_song = canvas_classement.create_image(230, 43, image=Third)
      canvas_classement.tag_bind(third_song, "<Button-1>")




    


    def show_next_frame():
      global t
      global current_frame
      if t < 2:  # Limite supérieure, vous pouvez ajuster cette valeur
          t += 1 #en faite qui soit a la frame 2 ou 1 lorsque que l'utilisateur appuiyeras sur le button il sera redigier vers ou restera sur la frame2
          current_frame = frame2
          current_frame.grid_forget()  # Supprime le cadre actuel de la grille.
          current_frame.grid(row=0, column=0)
          create_labels_on_frame2()  # Redraw labels on frame2
          print(t)  # Affiche la valeur de t.

    def show_prev_frame():
       global t
       global current_frame
       if t > 0:  # Limite inférieure, vous pouvez ajuster cette valeur
          t -= 1 #et lorsque qui appuiera sur prev depuis la frame 1 ou 2  il se redirigera  ou restera toujour vers ou dans  la frame1
          current_frame.grid_forget()  # Supprime le cadre actuel de la grille.
          current_frame = frame1
          current_frame.grid(row=0, column=0)
          
          print(t)  # Affiche la valeur de t.
    #cette fonction est le button pour revenir a la musique d'avant dans la frame 2
    def skip_back2():
            global n
            n -= 2
            #pour que les n se sont negative sinon sa embrouille tout le circuit et les couleur
            if n < 0:
                n = 0

            for widget in frame1.winfo_children():
              if isinstance(widget, tk.Label):
                  widget.destroy()
            

            song_name = list_of_songs[n]

            pygame.mixer.music.load(song_name)
            pygame.mixer.music.play(loops=0)
            pygame.mixer.music.set_volume(.5)

            label = tk.Label(frame1, text="{}/{}".format(n+1, len(list_of_covers)), bg='#404040', fg='white', font=title_font)
            label.place(relx=.83, rely=.75)


            image1 = Image.open(list_of_covers[n])
            image2 = image1.resize((100, 100))
            load = ImageTk.PhotoImage(image2)
   
            label1 = tk.Label(frame1, image=load)
            label1.image = load
            label1.place(relx=.03, rely=.05)  # Adjusted the y-position

            stripped_string = list_name_of_song[n]

            song_name_label = tk.Label(frame1, text=stripped_string, bg='#404040', fg='white', font=title_font)
            song_name_label.place(relx=.62, rely=.19, anchor='center')


            n += 1
    #cette fonction permet d'avancer a la musique d'appres dans la frame 1
    def skik_forward2():
         global n 
         if n == 0: #dans le cas ou n = 0 en apuiyyant sur prev est puisque n < 0 il sera egal 0 est en plus jouera le firt song mais j'appuerai sur next il me l'aurait rejouait ducoup je rajoute 1 pour lorsque j'appuie sur next et que je suis sur le first song sa me le rejout pas mais passe au prochain 
           n += 1
    
         if n >= len(list_of_songs):
            n = 0
         
         for widget in frame1.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
            

         song_name = list_of_songs[n]

         pygame.mixer.music.load(song_name)
         pygame.mixer.music.play(loops=0)
         pygame.mixer.music.set_volume(.5)

         label = tk.Label(frame1, text="{}/{}".format(n + 1, len(list_of_covers)), bg='#404040', fg='white', font=title_font)
         label.place(relx=.83, rely=.75)


         image1 = Image.open(list_of_covers[n])
         image2 = image1.resize((100, 100))
         load = ImageTk.PhotoImage(image2)
   
         label1 = tk.Label(frame1, image=load)
         label1.image = load
         label1.place(relx=.03, rely=.05)  # Adjusted the y-position

         stripped_string = list_name_of_song[n]

         song_name_label = tk.Label(frame1, text=stripped_string, bg='#404040', fg='white', font=title_font)
         song_name_label.place(relx=.62, rely=.19, anchor='center')

         n += 1
    
   

       


    list_of_covers = ['cover-1.jpeg', 'cover-2.jpeg', 'cover-3.jpeg', 'cover-6.jpeg', 'cover-7.jpeg', 'cover-8.jpeg', 'cover-9.jpeg', 'cover-10.jpeg', 'cover-11.jpeg', 'cover-12.jpeg'] 
    #si aucun son et lancer donc n = 0 alors il affichera que un message mais si un song et en cour d'ecoute le n sera forcement plus grand que 0 du coup il affichera le song en questions
    if n == 0:
        label = tk.Label(frame1, text="Veuillz lancer un titre.", bg='#404040', fg='white', font=title_font2)
        label.place(relx=.27, rely=.4)
    else:
        
        title_font = ('Georgia', 16, 'bold')
        label = tk.Label(frame1, text="{}/{}".format(n, len(list_of_covers)), bg='#404040', fg='white', font=title_font)
        label.place(relx=.83, rely=.75)


        image1 = Image.open(list_of_covers[n-1])
        image2 = image1.resize((100, 100))
        load = ImageTk.PhotoImage(image2)
   
        label1 = tk.Label(frame1, image=load)
        label1.image = load
        label1.place(relx=.03, rely=.05)  # Adjusted the y-position

        stripped_string = list_name_of_song[n-1]

        image_next = Image.open("next-button3.png")
        image_prev= Image.open("previous-3.png")

        global nextbtn2
        nextbtn2 = ImageTk.PhotoImage(image_next)
        global prevbtn2
        prevbtn2 = ImageTk.PhotoImage(image_prev)
 
        canevasnextbtn2 = tk.Canvas(frame1, width=50, height=50,bg= '#404040', highlightthickness=0)
        canevasnextbtn2.place(relx=0.73, rely=0.5, anchor='center')


        nextbutton2 = canevasnextbtn2.create_image(30, 35, image=nextbtn2)
        canevasnextbtn2.tag_bind(nextbutton2, "<Button-1>",lambda event : skik_forward2())



        canevasprevbtn2 = tk.Canvas(frame1, width=50, height=50, bg='#404040', highlightthickness=0)
        canevasprevbtn2.place(relx=0.45, rely=0.5, anchor='center')


        prevbutton2 = canevasprevbtn2.create_image(30, 35, image=prevbtn2)
        canevasprevbtn2.tag_bind(prevbutton2, "<Button-1>",lambda event : skip_back2())


        # Customize font style and size

        title_font = ('Georgia', 16, 'bold')  # Change font, size, and style as needed
        song_name_label = tk.Label(frame1, text=stripped_string, bg='#404040', fg='white', font=title_font)
        song_name_label.place(relx=.62, rely=.2, anchor='center') 
     

   #les fleche pour change de frame sur situer sur le home_page_fm
    image1 = Image.open("right-arrow.png")
    image2 = Image.open("left-arrow-2.png")


    resized_image1 = image1.resize((24, 24))
    resized_image2 = image2.resize((40, 40))
    
    global nextbtn
    nextbtn = ImageTk.PhotoImage(resized_image1)
    global prevbtn
    prevbtn = ImageTk.PhotoImage(resized_image2)


    canevasnextbtn = tk.Canvas(home_page_fm, width=40, height=80, bg='#272727', highlightthickness=0)
    canevasnextbtn.place(relx=0.99, rely=0.2, anchor='center')


    nextbutton = canevasnextbtn.create_image(10, 35, image=nextbtn)
    canevasnextbtn.tag_bind(nextbutton, "<Button-1>", lambda event: show_next_frame())

    canevasprevbtn = tk.Canvas(home_page_fm, width=30, height=80, bg='#272727', highlightthickness=0)
    canevasprevbtn.place(relx=0.01, rely=0.2, anchor='center')


    prevbutton = canevasprevbtn.create_image(30, 35, image=prevbtn)
    canevasprevbtn.tag_bind(prevbutton, "<Button-1>", lambda event : show_prev_frame())



 

    Mainframe.place(relx=.08, rely=.1)


    def switch_1(x):
       global n 
       n = 1
       song_name = '2Money-In-The-Grave.mp3'
       switch(x)
       get_album_cover(song_name, 1)
       global canvas
       if song_name.startswith('2'):
          main_fm.config(bg="#3F110F")
          canvas.config(bg="#3F110F")
          canvas1.config(bg='#661B19')#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 2

    def switch_2(x):
       global n 
       n = 0
       song_name = '1before-you-go.mp3'
       switch(x)
       get_album_cover(song_name, 0)
       global canvas
       if song_name.startswith('1'):
          main_fm.config(bg="#40220A")
          canvas.config(bg="#40220A")
          canvas1.config(bg='#673710')#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 1
    def switch_3(x):
       global n 
       n = 5
       song_name = '5Mount-Everest.mp3'
       switch(x)
       #les numero d'emplacement des cover sur en delai de 1 par rapport au n parseque il commence par 0
       get_album_cover(song_name, 4)
       global canvas
       if song_name.startswith('5'):
          main_fm.config(bg="#333333")
          canvas.config(bg="#333333")
          canvas1.config(bg="#404040")#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 5
    def switch_4(x):
       global n 
       n = 9
       song_name = '9Lovely.mp3'
       switch(x)
       #les numero d'emplacement des cover sur en delai de 1 par rapport au n parseque il commence par 0
       get_album_cover(song_name, 8)
       global canvas
       if song_name.startswith('9'):
           main_fm.config(bg="#402816")
           canvas.config(bg="#402816")
           canvas1.config(bg="#59391F")#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 9
    def switch_5(x):
       global n 
       n = 7
       song_name = '77Years.mp3'
       switch(x)
       #les numero d'emplacement des cover sur en delai de 1 par rapport au n parseque il commence par 0
       get_album_cover(song_name, 6)
       global canvas
       if song_name.startswith('7'):
           main_fm.config(bg="#202B40")
           canvas.config(bg="#202B40")
           canvas1.config(bg="#2D3C59")#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 7
    def switch_6(x):
       global n 
       n = 4
       song_name = '4Stressed-out.mp3'
       switch(x)
       #les numero d'emplacement des cover sur en delai de 1 par rapport au n parseque il commence par 0
       get_album_cover(song_name, 3)
       global canvas
       if song_name.startswith('4'):
          main_fm.config(bg="#401812")
          canvas.config(bg="#401812")
          canvas1.config(bg="#66261D")#nav bar
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       n = 4
       

       
    title_font1 = ('Helvetica', 16, 'bold')
    Title = tk.Label(home_page_fm, text='Your favourite artists', bg='#272727', fg='white', font=title_font1)
    Title.place(relx=0.01, rely=0.32)


    #se sont les image des artiste dans des canevas 

    canvas = tk.Canvas(home_page_fm, width=405, height=70, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.45, anchor='center')

    image1 = Image.open("h1.png")
    image2 = Image.open("h2.png")
    image3 = Image.open("h3.png")
    image4 = Image.open("h4.png")
    image5 = Image.open("h5.png")

    resized_image1 = image1.resize((70, 70))
    resized_image2 = image2.resize((70, 70))
    resized_image3 = image3.resize((70, 70))
    resized_image4 = image4.resize((70, 70))
    resized_image5 = image5.resize((70, 70))

    global Image1, Image2, Image3, Image4, Image5 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Image1 = ImageTk.PhotoImage(resized_image3)
    Image2 = ImageTk.PhotoImage(resized_image2)
    Image3 = ImageTk.PhotoImage(resized_image1)
    Image4 = ImageTk.PhotoImage(resized_image4)
    Image5 = ImageTk.PhotoImage(resized_image5)

    button_padding = 10
    button_x = 40

    Artist1 = canvas.create_image(button_x, 35, image=Image1)
    canvas.tag_bind(Artist1, "<Button-1>")

    button_x += 70 + button_padding

    Artist2 = canvas.create_image(button_x, 35, image=Image2)
    canvas.tag_bind(Artist2, "<Button-1>")

    button_x += 70 + button_padding

    Artist3 = canvas.create_image(button_x, 35, image=Image3)
    canvas.tag_bind(Artist3, "<Button-1>")

    button_x += 70 + button_padding

    Artist4 = canvas.create_image(button_x, 35, image=Image4)
    canvas.tag_bind(Artist4, "<Button-1>")

    button_x += 70 + button_padding

    Artist5 = canvas.create_image(button_x, 35, image=Image5)
    canvas.tag_bind(Artist5, "<Button-1>")
    #c'est pour afficher les noms en dessous des images des artiste asocier 

    title_font2 = ('Helvetica', 12, 'bold')
    name_fm = tk.Frame(home_page_fm, bg='#272727', width=400, height=70)

    name1 = tk.Label(name_fm, text='Juice WRLD', bg='#272727', fg = 'white', font=title_font2)
    name1.pack(padx=7, side='left')

    name2 = tk.Label(name_fm, text='Lil Tjay', bg='#272727', fg = 'white', font=title_font2)
    name2.pack(padx=7, side='left')

    name3 = tk.Label(name_fm, text='Charlie Puth', bg='#272727', fg = 'white', font=title_font2)
    name3.pack(padx=7, side='left')

    name4 = tk.Label(name_fm, text='Travis Scott', bg='#272727', fg = 'white', font=title_font2)
    name4.pack(padx=7, side='left')

    name5 = tk.Label(name_fm, text='Ed Sheeran', bg='#272727', fg = 'white', font=title_font2)
    name5.pack(padx=7, side='left')

    name_fm.place(relx=0.5, rely=0.54, anchor='center')

    title_font3 = ('Helvetica', 10, 'bold')#for the title of the music 
    title_font4 = ('Helvetica', 10)#for the aritist of the song 


    #1-cover song
    sp1 = Image.open("cover-1.png")#sp1 = song picture 1
    Resized_image1 = sp1.resize((38, 38))
    global Sp1 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp1 = ImageTk.PhotoImage(Resized_image1)

    #2-cover song
    sp2 = Image.open("cover-2.png")#sp2 = song picture 2
    Resized_image2 = sp2.resize((38, 38))
    global Sp2 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp2 = ImageTk.PhotoImage(Resized_image2)

    #play button = pb
    pb = Image.open("play-2.png")#pb = play buttton
    Resized_image3 = pb.resize((25, 25))
    global pb2 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    pb2 = ImageTk.PhotoImage(Resized_image3)

    #3-cover song
    sp3 = Image.open("cover-7.png")#sp3 = song picture 3
    Resized_image3 = sp3.resize((38, 38))
    global Sp3 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp3 = ImageTk.PhotoImage(Resized_image3)
    
   #4-cover song
    sp4 = Image.open("cover-11.png")#sp4 = song picture 4
    Resized_image4 = sp4.resize((38, 38))
    global Sp4 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp4 = ImageTk.PhotoImage(Resized_image4)

    sp5 = Image.open("cover-9.png")#sp5 = song picture 5
    Resized_image5 = sp5.resize((38, 38))
    global Sp5 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp5 = ImageTk.PhotoImage(Resized_image5)

    sp6 = Image.open("cover-6.png")#sp6 = song picture 6
    Resized_image6 = sp6.resize((38, 38))
    global Sp6 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp6 = ImageTk.PhotoImage(Resized_image6)
    
    Title2 = tk.Label(home_page_fm, text='Your favourite artists', bg='#272727', fg='white', font=title_font1)
    Title2.place(relx=0.01, rely=0.58)

    song_fm = tk.Frame(home_page_fm, bg='#272727', width=420, height=150)

     #premier ligne dans la quel est afficher deux titre
    song_1 = tk.Frame(song_fm, bg='#404040', width=420, height=37.5)

    canvas = tk.Canvas(song_1, width=255, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.30, rely=0.15, anchor='center')

    name_s1 = tk.Label(song_1, bg='#272727', text='Before You Go', font=title_font3, fg='white')
    name_s1.place(relx=0.28, rely=0.3, anchor='center')

    name_s2 = tk.Label(song_1, bg='#272727', text='Song . Lewis Calpadi . 3:39', font=title_font4, fg='white')
    name_s2.place(relx=0.28, rely=0.7, anchor='center')

    song1 = canvas.create_image(30, 53, image= Sp1)
    canvas.tag_bind(song1, "<Button-1>")

    canvas = tk.Canvas(song_1, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.49, rely=0.43, anchor='center')

    playbutton = canvas.create_image(15, 15, image= pb2)
    canvas.tag_bind(playbutton, "<Button-1>", lambda event : switch_2(lecteur_page))

    canvas = tk.Canvas(song_1, width=210, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.77, rely=0.15, anchor='center')

    song2 = canvas.create_image(30, 53, image= Sp2)
    canvas.tag_bind(song2, "<Button-1>")
    
    name_s3 = tk.Label(song_1,bg= '#272727', text='Money In The grave', font=title_font3, fg='white')
    name_s3.place(relx=0.76, rely=0.3, anchor='center')

    name_s4 = tk.Label(song_1,bg = '#272727', text='Song . Drake . 3:26', font=title_font4, fg='white')
    name_s4.place(relx=0.76, rely=0.7, anchor='center')

    canvas = tk.Canvas(song_1, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.95, rely=0.43, anchor='center')

    playbutton = canvas.create_image(15, 15, image= pb2)
    canvas.tag_bind(playbutton, "<Button-1>", lambda event : switch_1(lecteur_page))


    song_1.place(relx=0.5, rely=0.15, anchor='center')#le relx et rely est proportionnelle au compartiment qui le contient

    #deuxieme ligne dans laquelle est aussi afficher deux titre
    song_2 = tk.Frame(song_fm, bg='gray', width=420, height=37.5)

    canvas = tk.Canvas(song_2, width=255, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.30, rely=0.15, anchor='center')

    name_s1 = tk.Label(song_2, bg='#272727', text='Mount Everest', font=title_font3, fg='white')
    name_s1.place(relx=0.28, rely=0.3, anchor='center')

    name_s2 = tk.Label(song_2, bg='#272727', text='Song . Labrinth . 2:26', font=title_font4, fg='white')
    name_s2.place(relx=0.28, rely=0.7, anchor='center')

    song1 = canvas.create_image(30, 53, image= Sp3)
    canvas.tag_bind(song1, "<Button-1>")
     
    #play button on the home page
    canvas_Play_Button = tk.Canvas(song_2, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas_Play_Button.place(relx=0.49, rely=0.43, anchor='center')

    playbutton = canvas_Play_Button.create_image(15, 15, image= pb2)
    canvas_Play_Button.tag_bind(playbutton, "<Button-1>", lambda event : switch_3(lecteur_page))

    canvas = tk.Canvas(song_2, width=210, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.77, rely=0.15, anchor='center')

    song2 = canvas.create_image(30, 53, image= Sp4)
    canvas.tag_bind(song2, "<Button-1>")
    
    name_s3 = tk.Label(song_2,bg= '#272727', text='lovely', font=title_font3, fg='white')
    name_s3.place(relx=0.76, rely=0.3, anchor='center')

    name_s4 = tk.Label(song_2,bg = '#272727', text='Song . Billie . 3:26', font=title_font4, fg='white')
    name_s4.place(relx=0.76, rely=0.7, anchor='center')

    canvas = tk.Canvas(song_2, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.95, rely=0.43, anchor='center')

    playbutton = canvas.create_image(15, 15, image= pb2)
    canvas.tag_bind(playbutton, "<Button-1>", lambda event : switch_4(lecteur_page))

    song_2.place(relx=0.5, rely=0.43, anchor='center')

    #troisieme ligne dans laquelle est afficher aussi 2 titre
    song_3 = tk.Frame(song_fm, bg='gray', width=420, height=37.5)

    canvas = tk.Canvas(song_3, width=255, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.30, rely=0.15, anchor='center')

    name_s5 = tk.Label(song_3, bg='#272727', text='7 Years', font=title_font3, fg='white')
    name_s5.place(relx=0.28, rely=0.3, anchor='center')

    name_s6 = tk.Label(song_3, bg='#272727', text='Song . Lukas Graham . 3:59', font=title_font4, fg='white')
    name_s6.place(relx=0.28, rely=0.7, anchor='center')
    #cover of the song 
    song1 = canvas.create_image(30, 53, image= Sp5)
    canvas.tag_bind(song1, "<Button-1>")

    canvas = tk.Canvas(song_3, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.49, rely=0.43, anchor='center')

    playbutton = canvas.create_image(15, 15, image= pb2)
    canvas.tag_bind(playbutton, "<Button-1>", lambda event : switch_5(lecteur_page))

    canvas = tk.Canvas(song_3, width=210, height=80, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.77, rely=0.15, anchor='center')

    song2 = canvas.create_image(30, 53, image= Sp6)
    canvas.tag_bind(song2, "<Button-1>")
    
    name_s7 = tk.Label(song_3,bg= '#272727', text='Stressed Out', font=title_font3, fg='white')
    name_s7.place(relx=0.76, rely=0.3, anchor='center')

    name_s8 = tk.Label(song_3,bg = '#272727', text='Song . Twen . 3:26', font=title_font4, fg='white')
    name_s8.place(relx=0.76, rely=0.7, anchor='center')

    canvas = tk.Canvas(song_3, width=30, height=30, bg='#272727', highlightthickness=0)
    canvas.place(relx=0.95, rely=0.43, anchor='center')

    playbutton = canvas.create_image(15, 15, image= pb2)
    canvas.tag_bind(playbutton, "<Button-1>", lambda event : switch_6(lecteur_page))

    song_3.place(relx=0.5, rely=0.71, anchor='center')

    song_fm.place(relx=0.5, rely=0.76, anchor='center')

    home_page_fm.pack(fill=tk.BOTH, expand=True)

def lecteur_page():
    pygame.init()
    global n
    #color of all the background of the lecteur
    root.config(bg='#40220A')#bg of the root


    global playButton
    global pause_img
    global button_state
    global canvas
    
    if button_state == 1:
          canvas.itemconfig(playButton, image=pause_img)
          pygame.mixer.music.unpause()
          button_state = 0

    #conn = sqlite3.connect("database.db")

    # Créez un curseur pour exécuter des commandes SQL
    #cursor = conn.cursor()

    # Définissez la structure de la table pour stocker le nombre d'écoutes par chanson
    #cursor.execute("""
    #CREATE TABLE IF NOT EXISTS Ecoutes (
        #id INTEGER PRIMARY KEY AUTOINCREMENT,
        #chanson TEXT,
        #nombre_ecoutes INTEGER
    #   )
    #""")

    # Enregistrez les modifications et fermez la connexion à la base de données
    #conn.commit()
    #onn.close()

   
    nombre_decoutes = {
       'Before you go':0,
       'Money In The Grave':0,
       'Mash up':0,
       'Stressed Out':0,
       'Mount Everest':0,
       'In The Stars':0,
       '7Years':0,
       'love Nwantiti':0,
       'Lovely':0,
       'i Hate you':0
       
    }


    duree_chansons = {
    'Before you go': 206,  # Exemple de durée en secondes
    'Money In The Grave': 205,
    'Mash up':206,
    'Stressed Out':210,
    'Mount Everest':210,
    'In The Stars':217,
    '7Years':238,
    'love Nwantiti':10,
    'Lovely':206,
    'i Hate you':252

    }

    def commencer_lecture_chanson(chanson):
        global temps_debut_ecoute
        temps_debut_ecoute = time.time()


    # Fonction pour arrêter la lecture d'une chanson
    def arreter_lecture_chanson(chanson):
       global temps_debut_ecoute
       global chanson_en_cours
       duree_ecoute = time.time() - temps_debut_ecoute
       if duree_ecoute > (duree_chansons[chanson] / 2):
           nombre_decoutes[chanson] += 1  # Incrémente le nombre d'écoutes si plus de la moitié a été écoutée
           conn = sqlite3.connect("database.db")
           cursor = conn.cursor()
           chanson = chanson_en_cours

           # Récupérez le nombre d'écoutes actuel pour cette chanson depuis la base de données
           cursor.execute("SELECT nombre_ecoutes FROM Ecoutes WHERE chanson = ?", (chanson,))
           resultat = cursor.fetchone()

           if resultat:
              nombre_ecoutes_actuel = resultat[0]
           else:
              nombre_ecoutes_actuel = 0

           # Incrémentez le nombre d'écoutes actuel de 1
           nouveau_nombre_ecoutes = nombre_ecoutes_actuel + 1

           # Mettez à jour le nombre d'écoutes dans la base de données
           cursor.execute("UPDATE Ecoutes SET nombre_ecoutes = ? WHERE chanson = ?", (nouveau_nombre_ecoutes, chanson))

           # Validez la transaction et fermez la connexion
           conn.commit()
           conn.close()
           
   



    #3-cover song
    sp10 = Image.open("home-2.png")#sp3 = song picture 3
    global Sp10 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp10 = ImageTk.PhotoImage(sp10)
    
    sp11 = Image.open("lecteur.png")#sp3 = song picture 3
    global Sp11 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp11 = ImageTk.PhotoImage(sp11)

    sp12 = Image.open("playist-2.png")#sp3 = song picture 3
    global Sp12 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp12 = ImageTk.PhotoImage(sp12)
   #changement de l'image de la nav bar pour que sa montre dans quel frame je suis
    global homeButton
    canvas1.itemconfig(homeButton, image=Sp10)

    global lecteurButton
    canvas1.itemconfig(lecteurButton, image=Sp11)

    global playistButton
    canvas1.itemconfig(playistButton, image=Sp12)

    

    global get_album_cover #pour pouvoir appeller cette fonction dans le home page et pour lancer les song depuis labas
    def get_album_cover(song_name, n):
       # Clear previous title and cover image
       for widget in main_fm.winfo_children():
          if isinstance(widget, tk.Label):
               widget.destroy()

       image1 = Image.open(list_of_covers[n])
       image2 = image1.resize((250, 250))
       load = ImageTk.PhotoImage(image2)

       label1 = tk.Label(main_fm, image=load)
       label1.image = load
       label1.place(relx=.19, rely=.1)  # Adjusted the y-position

       stripped_string = list_name_of_song[n]

        # Customize font style and size
       title_font = ('Helvetica', 16, 'bold')  # Change font, size, and style as needed
       song_name_label = tk.Label(main_fm, text=stripped_string, bg='#272727', fg='white', font=title_font)
       song_name_label.place(relx=.5, rely=.61, anchor='center')  # Adjusted the y-position

       # Color bg of the song_name_label comme ça c'est la même couleur que le bg de la fenêtre
       if song_name.startswith('1'):
         global chanson_en_cours
         song_name_label.config(bg="#40220A", fg='white')
         chanson_en_cours = 'Before you go'
         commencer_lecture_chanson(chanson_en_cours)

       if song_name.startswith('2'):
          song_name_label.config(bg="#3F110F", fg='white')
          arreter_lecture_chanson(chanson_en_cours)
          print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
          chanson_en_cours = 'Money In The Grave'
          commencer_lecture_chanson(chanson_en_cours)


       if song_name.startswith('3'):
         song_name_label.config(bg="#2C1F29", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'Mash up'
         commencer_lecture_chanson(chanson_en_cours)


       if song_name.startswith('4'):
         song_name_label.config(bg="#401812", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'Stressed Out'
         commencer_lecture_chanson(chanson_en_cours)

       if song_name.startswith('5'):
         song_name_label.config(bg="#333333", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'Mount Everest'
         commencer_lecture_chanson(chanson_en_cours)

       if song_name.startswith('6'):
         song_name_label.config(bg="#272727", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'In The Stars'
         commencer_lecture_chanson(chanson_en_cours)

       if song_name.startswith('7'):
         song_name_label.config(bg="#202B40", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = '7Years'
         commencer_lecture_chanson(chanson_en_cours)

       if song_name.startswith('8'):
         song_name_label.config(bg="#40120B", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'love Nwantiti'
         commencer_lecture_chanson(chanson_en_cours)
      
       if song_name.startswith('9'):
         song_name_label.config(bg="#402816", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'Lovely'
         commencer_lecture_chanson(chanson_en_cours)


       if song_name.startswith('10'):
         song_name_label.config(bg="#1D1940", fg='white')
         arreter_lecture_chanson(chanson_en_cours)
         print('ecoute ' + str(nombre_decoutes[chanson_en_cours]))
         chanson_en_cours = 'i Hate you'
         commencer_lecture_chanson(chanson_en_cours)


       #color du background quand  on appuie sur previous music


    def threading():
       t1 = Thread()
       t1.start()

    def skip_forward(event):
       threading()
       global n
       global button_state
       current_song = n
       global h
       
       #dans le cas ou l'utilisateur au lancement de l'appli n'appuie pas sur le play button mais sur le forward donc le h = 0 et un moyen de verifier cette situation du coup l'image du playbutton passe direct a play avec le song en train d'etre jouer
       if h == 0:
          canvas.itemconfig(playButton, image=pause_img)
          pygame.mixer.music.unpause()
          button_state = 0

       if n == 0: #dans le cas ou n = 0 en apuiyyant sur prev est puisque n < 0 il sera egal 0 est en plus jouera le firt song mais j'appuerai sur next il me l'aurait rejouait ducoup je rajoute 1 pour lorsque j'appuie sur next et que je suis sur le first song sa me le rejout pas mais passe au prochain 
           n += 1
    
       if n >= len(list_of_songs):
           n = 0
       #cette condition est creer pour si le button est sur pause mais que l'utilisateur passe de music sur la prochaine music l'image du playbutton sera play et non pause 
       if button_state == 1:
           canvas.itemconfig(playButton, image=pause_img)
           pygame.mixer.music.unpause()
           button_state = 0

       #colors of background lorsque on appuie sur next music
       song_name = list_of_songs[n]
       if song_name.startswith('1'):
           main_fm.config(bg="#40220A")#color of the frame
           canvas.config(bg="#40220A")
           canvas1.config(bg='#673710')#nav bar
        
       if song_name.startswith('2'):
          main_fm.config(bg="#3F110F")
          canvas.config(bg="#3F110F")
          canvas1.config(bg='#661B19')#nav bar

    
       if song_name.startswith('3'):
           main_fm.config(bg="#2C1F29")
           canvas.config(bg="#2C1F29")
           canvas1.config(bg="#402D3A")#nav bar

       if song_name.startswith('4'):
           main_fm.config(bg="#401812")
           canvas.config(bg="#401812")
           canvas1.config(bg="#66261D")#nav bar
   


       if song_name.startswith('5'):
           main_fm.config(bg="#333333")
           canvas.config(bg="#333333")
           canvas1.config(bg="#404040")#nav bar

       if song_name.startswith('6'):
           main_fm.config(bg="#272727")
           canvas.config(bg="#272727")
           canvas1.config(bg="#404040")#nav bar

       if song_name.startswith('7'):
           main_fm.config(bg="#202B40")
           canvas.config(bg="#202B40")
           canvas1.config(bg="#2D3C59")#nav bar

       if song_name.startswith('8'):
           main_fm.config(bg="#40120B")
           canvas.config(bg="#40120B")
           canvas1.config(bg="#661E12")#nav bar

       if song_name.startswith('9'):
           main_fm.config(bg="#402816")
           canvas.config(bg="#402816")
           canvas1.config(bg="#59391F")#nav bar

       if song_name.startswith('10'):
           main_fm.config(bg="#1D1940")
           canvas.config(bg="#1D1940")
           canvas1.config(bg="#2F2866")#nav bar


           
    
       pygame.mixer.music.load(song_name)
       pygame.mixer.music.play(loops=0)
       pygame.mixer.music.set_volume(.5)
       get_album_cover(song_name, n)
  

       n += 1
       print(n)
    global toggle_play_pause
    def toggle_play_pause():
        global button_state
        global h
        global n
        song_name = list_of_songs[h]
        if n > 0:
            h = 1
        #la premiere condition qui va verifier c'est celle du premier titre et si true il ne va pas verifier les autres conditions ducoup il ne va pas le button en pause au lancement du premier titre
        if h == 0:
           canvas.itemconfig(playButton, image=pause_img)#je me la src canvas  en play et puis remet le button state a zero pour que lorsque je vais reapuiiyait sa fait pause 
           button_state = 0
           pygame.mixer.music.load(song_name)
           pygame.mixer.music.play(loops=0)
           pygame.mixer.music.set_volume(.5)
           get_album_cover(song_name, h)
           #pour changer la couleur gris au lancement du premier titre
           main_fm.config(bg="#40220A")#color of the frame
           canvas.config(bg="#40220A")
           canvas1.config(bg='#673710')#nav bar
           h = 1
           #je met le n = 1 pour que dans le home page les premier song s'affiche comme song en train d'etre jouer
           n = 1

        elif button_state == 0:
           canvas.itemconfig(playButton, image=Image2)
           pygame.mixer.music.pause()
           button_state = 1
        else:
          canvas.itemconfig(playButton, image=pause_img)
          pygame.mixer.music.unpause()
          button_state = 0

    def skip_back(event):
        global n
        n -= 2
        global button_state

       #dans le cas ou l'utilisateur au lancement de l'appli n'appuie pas sur le play button mais sur le back donc le h = 0 et un moyen de verifier cette situation du coup l'image du playbutton passe direct a play avec le song en train d'etre jouer
        if h == 0:
          canvas.itemconfig(playButton, image=pause_img)
          pygame.mixer.music.unpause()
          button_state = 0
        #cette condition est creer pour si le button est sur pause mais que l'utilisateur passe de music sur la prochaine music l'image du playbutton sera play et non pause 
        if button_state == 1:
           canvas.itemconfig(playButton, image=pause_img)
           pygame.mixer.music.unpause()
           button_state = 0
         
      #pour que les n se sont negative sinon sa embrouille tout le circuit et les couleur
        if n < 0:
           n = 0

        song_name = list_of_songs[n]
        if song_name.startswith('1'):
           main_fm.config(bg="#40220A")#color of the frame
           canvas.config(bg="#40220A")
           canvas1.config(bg='#673710')#nav bar
        
        if song_name.startswith('2'):
          main_fm.config(bg="#3F110F")
          canvas.config(bg="#3F110F")
          canvas1.config(bg='#661B19')#nav bar
    
        if song_name.startswith('3'):
           main_fm.config(bg="#2C1F29")
           canvas.config(bg="#2C1F29")
           canvas1.config(bg="#402D3A")#nav bar

        if song_name.startswith('4'):
           main_fm.config(bg="#401812")
           canvas.config(bg="#401812")
           canvas1.config(bg="#66261D")#nav bar

        if song_name.startswith('5'):
           main_fm.config(bg="#333333")
           canvas.config(bg="#333333")
           canvas1.config(bg="#404040")#nav bar

        if song_name.startswith('6'):
           main_fm.config(bg="#272727")
           canvas.config(bg="#272727")
           canvas1.config(bg="#404040")#nav bar

        if song_name.startswith('7'):
           main_fm.config(bg="#202B40")
           canvas.config(bg="#202B40")
           canvas1.config(bg="#2D3C59")#nav bar

        if song_name.startswith('8'):
           main_fm.config(bg="#40120B")
           canvas.config(bg="#40120B")
           canvas1.config(bg="#661E12")#nav bar

        if song_name.startswith('9'):
           main_fm.config(bg="#402816")
           canvas.config(bg="#402816")
           canvas1.config(bg="#59391F")#nav bar

        if song_name.startswith('10'):
           main_fm.config(bg="#1D1940")
           canvas.config(bg="#1D1940")
           canvas1.config(bg="#2F2866")#nav bar
    
         
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)
        get_album_cover(song_name, n)

        n += 1#j'ajoute 1 ici parseque dans le cas ou je joue le song 3 par example donc mon n = 4 lorsque je vais passer back pour la prev music le n - 2 = 2  et va jouer le song 2 du coup lorsque je vais apuuiyer sur forward sa rejouer le song 2 et en ajoutant 1 a la fin de chaque apuie sur prev music je vais empecher ce bug
        print(n)

    global shuffle
    def shuffle(event):
        global n 


        n = random.randint(0, 9)

        song_name = list_of_songs[n]
        if song_name.startswith('1'):
           main_fm.config(bg="#40220A")#color of the frame
           canvas.config(bg="#40220A")
           canvas1.config(bg='#673710')#nav bar
        
        if song_name.startswith('2'):
          main_fm.config(bg="#3F110F")
          canvas.config(bg="#3F110F")
          canvas1.config(bg='#661B19')#nav bar
    
        if song_name.startswith('3'):
           main_fm.config(bg="#2C1F29")
           canvas.config(bg="#2C1F29")
           canvas1.config(bg="#402D3A")#nav bar

        if song_name.startswith('4'):
           main_fm.config(bg="#401812")
           canvas.config(bg="#401812")
           canvas1.config(bg="#66261D")#nav bar

        if song_name.startswith('5'):
           main_fm.config(bg="#333333")
           canvas.config(bg="#333333")
           canvas1.config(bg="#404040")#nav bar

        if song_name.startswith('6'):
           main_fm.config(bg="#272727")
           canvas.config(bg="#272727")
           canvas1.config(bg="#404040")#nav bar

        if song_name.startswith('7'):
           main_fm.config(bg="#202B40")
           canvas.config(bg="#202B40")
           canvas1.config(bg="#2D3C59")#nav bar

        if song_name.startswith('8'):
           main_fm.config(bg="#40120B")
           canvas.config(bg="#40120B")
           canvas1.config(bg="#661E12")#nav bar

        if song_name.startswith('9'):
           main_fm.config(bg="#402816")
           canvas.config(bg="#402816")
           canvas1.config(bg="#59391F")#nav bar

        if song_name.startswith('10'):
           main_fm.config(bg="#1D1940")
           canvas.config(bg="#1D1940")
           canvas1.config(bg="#2F2866")#nav bar

        


        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)
        get_album_cover(song_name, n)
  

        n += 1


    

    pygame.mixer.init()
    global list_of_covers
    global list_name_of_song
    global list_of_songs
    list_of_songs = ['1before-you-go.mp3', '2Money-In-The-Grave.mp3', '3Mash-up.mp3', '4Stressed-out.mp3', '5Mount-Everest.mp3', '6In-The-Stars.mp3', '77Years.mp3', '8love-nwantiti.mp3', '9Lovely.mp3', '10I-Hate-you.mp3']  
    list_of_covers = ['cover-1.jpeg', 'cover-2.jpeg', 'cover-3.jpeg', 'cover-6.jpeg', 'cover-7.jpeg', 'cover-8.jpeg', 'cover-9.jpeg', 'cover-10.jpeg', 'cover-11.jpeg', 'cover-12.jpeg']  
    list_name_of_song = ['Before you go', 'Money In The Grave', 'Mash up', 'Stressed Out', 'Mount Everest', 'In The Stars', '7Years', 'love Nwantiti', 'Lovely', 'i Hate you']  
    #je creer cette condition pour lorsque je lance un son et que je vais la frame home page au retour dans la frame lecteur la presentation du titre en train de joue sera toujours presente
    if n == 0:
       main_fm.config(bg="#272727")  # Définir la couleur de fond par défaut
       canvas1.config(bg='#404040')

       message_label = tk.Label(main_fm,bg='#272727',fg='white' ,text="click on the playbutton to start the first song", font=('Garamond', 15))
       message_label.place(relx = 0.5, rely=0.4, anchor='center')

       canvas = tk.Canvas(main_fm, width=250, height=70, bg='#272727', highlightthickness=0)
       canvas.place(relx=0.5, rely=0.75, anchor='center')
       
       nextimage = Image.open("next-button-2.png")
       playimage = Image.open("play-2.png")
       previousimage = Image.open("previous-2.png")

       resized_image1 = nextimage.resize((36, 36))
       resized_image2 = playimage.resize((36, 36))
       resized_image3 = previousimage.resize((36, 36))

       global Image1, Image2, Image3, Image4 # Nécessaire pour éviter la suppression des références des images par le garbage collector
       Image1 = ImageTk.PhotoImage(resized_image3)
       Image2 = ImageTk.PhotoImage(resized_image2)
       Image3 = ImageTk.PhotoImage(resized_image1)

       button_padding = 10
       button_x = 50

       previousButton = canvas.create_image(button_x, 35, image=Image1)
       canvas.tag_bind(previousButton, "<Button-1>", skip_back)

       button_x += 70 + button_padding
    
 
       pause_img = tk.PhotoImage(file="pause.png")

       playButton = canvas.create_image(button_x, 35, image=Image2)
       canvas.tag_bind(playButton, "<Button-1>",  lambda event: toggle_play_pause())

       button_x += 70 + button_padding

       nextButton = canvas.create_image(button_x, 35, image=Image3)
       canvas.tag_bind(nextButton, "<Button-1>", skip_forward)

       
    else:
       # parseque la fin de chaque appuie sur back or forward la position de n est 1 de plus pour le prochain song mais si je veux afficher le song actuelle il faut que j'enleve 1 au n 
       n -= 1 #pour qu'il revienne au titre en question et pas celui d'apres
       print(n)
       song_name = list_of_songs[n]
       get_album_cover(song_name, n)

       canvas = tk.Canvas(main_fm, width=400, height=70, bg='#40220A', highlightthickness=0)
       canvas.place(relx=0.5, rely=0.75, anchor='center')


       nextimage = Image.open("next-button-2.png")
       playimage = Image.open("play-2.png")
       previousimage = Image.open("previous-2.png")
       shuffleButton = Image.open("shuffle.png")

       resized_image1 = nextimage.resize((36, 36))
       resized_image2 = playimage.resize((36, 36))
       resized_image3 = previousimage.resize((36, 36))
       resized_image4 = shuffleButton.resize((36, 36))
       
       Image1 = ImageTk.PhotoImage(resized_image3)
       Image2 = ImageTk.PhotoImage(resized_image2)
       Image3 = ImageTk.PhotoImage(resized_image1)
       Image4 = ImageTk.PhotoImage(resized_image4)

       button_padding = 10
       button_x = 120

       previousButton = canvas.create_image(button_x, 35, image=Image1)
       canvas.tag_bind(previousButton, "<Button-1>", skip_back)

       button_x += 70 + button_padding
    
       pause_img = tk.PhotoImage(file="pause.png")
       button_state = 0  # 0 for play, 1 for pause
       playButton = canvas.create_image(button_x, 35, image=Image2)
       canvas.tag_bind(playButton, "<Button-1>",  lambda event: toggle_play_pause())

       button_x += 70 + button_padding

       nextButton = canvas.create_image(button_x, 35, image=Image3)
       canvas.tag_bind(nextButton, "<Button-1>", skip_forward)


       button_x += 55 + button_padding


       shuffleButton = canvas.create_image(button_x, 35, image=Image4)
       canvas.tag_bind(shuffleButton, "<Button-1>", shuffle)

       if song_name.startswith('1'):
          main_fm.config(bg="#40220A")
          canvas.config(bg="#40220A")
          canvas1.config(bg='#673710')#nav bar

        
       if song_name.startswith('2'):
          main_fm.config(bg="#3F110F")#le bg de la fenetre
          canvas.config(bg="#3F110F")#le canevas des button play prev et next
          canvas1.config(bg='#661B19')#nav bar
    
       if song_name.startswith('3'):
          main_fm.config(bg="#2C1F29")
          canvas.config(bg="#2C1F29")
          canvas1.config(bg="#402D3A")#nav bar

       if song_name.startswith('4'):
          main_fm.config(bg="#401812")
          canvas.config(bg="#401812")
          canvas1.config(bg="#66261D")#nav bar
         
       if song_name.startswith('5'):
          main_fm.config(bg="#333333")
          canvas.config(bg="#333333")
          canvas1.config(bg="#404040")#nav bar

       if song_name.startswith('6'):
           main_fm.config(bg="#272727")
           canvas.config(bg="#272727")
           canvas1.config(bg="#404040")#nav bar

       
       if song_name.startswith('7'):
           main_fm.config(bg="#202B40")
           canvas.config(bg="#202B40")
           canvas1.config(bg="#2D3C59")#nav bar

       if song_name.startswith('8'):
           main_fm.config(bg="#40120B")
           canvas.config(bg="#40120B")
           canvas1.config(bg="#661E12")#nav bar

       if song_name.startswith('9'):
           main_fm.config(bg="#402816")
           canvas.config(bg="#402816")
           canvas1.config(bg="#59391F")#nav bar
           
       if song_name.startswith('10'):
           main_fm.config(bg="#1D1940")
           canvas.config(bg="#1D1940")
           canvas1.config(bg="#2F2866")#nav bar
           
           
       n += 1#je rajoute un 1 au n pour que lorsque le user appuiyera sur forward il ne rejouera pas le meme song mais passera au prochain


def playist_page():

    
    sp1= Image.open("playist-1.png")#sp3 = song picture 3
    global Sp1 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp1 = ImageTk.PhotoImage(sp1)


    sp2= Image.open("musique.png")#sp3 = song picture 3
    global Sp2 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp2 = ImageTk.PhotoImage(sp2)

    sp3= Image.open("home-2.png")#sp3 = song picture 3
    global Sp3 # Nécessaire pour éviter la suppression des références des images par le garbage collector
    Sp3 = ImageTk.PhotoImage(sp3)

    global playistButton
    canvas1.itemconfig(playistButton, image=Sp1)

    global lecteurButton
    canvas1.itemconfig(lecteurButton, image=Sp2)

    global homeButton
    canvas1.itemconfig(homeButton, image=Sp3)
    #color of all the background
    #le bg du root et du main et de la meme couleur pour reliere le main_fm et le option_fm
    root.config(bg='#271C09')
    canvas1.config(bg='#402E0E')
    main_fm.config(bg='#271C09')

    playist_page_lb = tk.Label(main_fm, text='playist page', bg='#271C09', fg='white')
    playist_page_lb.pack(pady=80)
def main():
    
    def disable_resize(event):
        root.resizable(False, False)
           
  
    global root #je fait sa pour pouvoir l'utiliser dans les autre fonction en haut pour changer les background en fonction de la musique est relier le main_fm et le option_fm
    root = tk.Tk()
    # Spécifie la position initiale de la fenêtre (x, y)
    root.geometry("420x600+600+100")  # Largeur x Hauteur + Position_X + Position_Y
    root.title("Projet Spotify Music")
    root.bind("<Configure>", disable_resize)
    #root.config(bg = "gray") (sa vient relier la main frame et le option frame qui sont sur la fenetre principale)

    global main_fm
    main_fm = tk.Frame(root, bg='gray')  # Frame pour afficher les différentes pages
    main_fm.pack(fill=tk.BOTH, expand=True)

   
    global canvas1
    canvas1 = tk.Canvas(root, width=420, height=80, bg='#0F2140', highlightthickness=0)#highlightthickness c'est pour enlever la ligne blanche qui entre le main_fm et le option_fm qui enfait un border
    canvas1.place(relx=0.5, rely=0.94, anchor= 'center')

    # Chargement de l'image originale mais dans la main function les image non pas besoin de global puisque la fonction est toujour en exsecution
    homeimage = Image.open("home.png")
    lecteurimage = Image.open("lecteur.png")
    playistimage = Image.open("playist-2.png")


    # Redimensionnement de l'image
    resized_image1 = homeimage.resize((60, 60))  # Nouvelle taille (36x36)
    resized_image2 = lecteurimage.resize((60, 60))
    resized_image3 = playistimage.resize((60, 60))

    # Création d'un PhotoImage à partir de l'image redimensionnée
    Image1 = ImageTk.PhotoImage(homeimage)
    Image2 = ImageTk.PhotoImage(lecteurimage)
    Image3 = ImageTk.PhotoImage(playistimage)

    # Création des boutons côte à côte
    button_padding = 10  # Espacement entre les boutons
    button_x = 125  # Coordonnée x de départ pour le premier bouton

    global homeButton
    homeButton = canvas1.create_image(button_x, 40, image=Image1)#(X, Y, ref image)
    canvas1.tag_bind(homeButton, "<Button-1>", lambda event: switch(home_page))


    button_x += 70 + button_padding  # (espace entre les  button) Mise à jour de la coordonnée x pour le prochain bouton
    
    global lecteurButton
    lecteurButton = canvas1.create_image(button_x, 40, image=Image2)
    canvas1.tag_bind(lecteurButton, "<Button-1>", lambda event: switch(lecteur_page))#la fonction event avec l'aide de lambda c'est une facon d'une une function dans sa propre function

    button_x += 70 + button_padding  # Mise à jour de la coordonnée x pour le dernier bouton

    global playistButton
    playistButton = canvas1.create_image(button_x, 40, image=Image3)
    canvas1.tag_bind(playistButton, "<Button-1>", lambda event: switch(playist_page))

    switch(home_page)  # Afficher la home page au démarrage (sa va afficher la main_fm en question au demarage)

    root.mainloop()


if __name__ == "__main__":
    main()
