from tkinter import*
import sqlite3
from random import randint
import pygame
from pygame.locals import*

#On crée la base de donneés de notre jeu
connexion = sqlite3.connect('DonneesCountryHunter.db')
#On crée un objet Cursor pour se déplacer dans la base
curseur = connexion.cursor()
#Cette base contient 2 clés : le nom de l'élément et le pays correspondant
curseur.execute("""
    CREATE TABLE IF NOT EXISTS ImagesSonsFacile(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT,
    pays TEXT
    )
    """)


curseur = connexion.cursor()
#On parcourt tous les enregistrement de la base par ligne en
for enregistrement in curseur.execute('SELECT * FROM ImagesSonsFacile'):
    print(enregistrement)
connexion.close()

def enregistrer_donnees(nb, base):
    '''Sert à enregister des données dans la table ImagesSonsFacile'''
    if isinstance(nb,int) and nb!=0:
        connexion = sqlite3.connect(base)
        curseur = connexion.cursor()
        
        for i in range(nb):
            print("Enregistrement de l'élément : ",i+1)
            n = input("Nom de l'élément : ")
            p = input("Pays de l'élément : ")
            curseur.execute('''INSERT INTO ImagesSonsFacile(nom,pays) VALUES(?,?)''',(n,p))
            connexion.commit()
        connexion.close()
    else : 
        print("Il n'y a aucun élément à enregistrer !")  
        
        
def nomElement():
    global aff
    '''Affiche le nom de l'élément'''
    global liste_images
    
    if liste_images[0][0] == 'img1':             
        aff = Label(cadre_fenetre1, text= 'Tour Eiffel')      
           
    elif liste_images[0][0] == 'img2':
        aff=Label(cadre_fenetre1,text='Statue de la Liberté')
        
    elif liste_images[0][0] == 'img3':
        aff=Label(cadre_fenetre1,text='Tour de Pise')
       
    elif liste_images[0][0] == 'img4':
        aff=Label(cadre_fenetre1,text='Big Ben')
          
    elif liste_images[0][0] == 'img5':
        aff=Label(cadre_fenetre1,text='Opéra de _')
         
    elif liste_images[0][0]== 'img6':
        aff=Label(cadre_fenetre1,text='PSY')
         
    elif liste_images[0][0] == 'img7':
        aff=Label(cadre_fenetre1,text='Porte de Brandebourg')
            
    elif liste_images[0][0] == 'img8':
        aff=Label(cadre_fenetre1,text='Winston Churchill')
           
    elif liste_images[0][0] == 'img9':
        aff=Label(cadre_fenetre1,text='Périclès')
            
    elif liste_images[0][0] == 'img10':
        aff=Label(cadre_fenetre1,text='La muraille de _')
          
    elif liste_images[0][0] == 'img14':
        aff=Label(cadre_fenetre1,text='Empire State Building')
        
    elif liste_images[0][0] == 'img15':
        aff=Label(cadre_fenetre1,text='Lionel Messi')
        
    elif liste_images[0][0] == 'img16':
        aff=Label(cadre_fenetre1,text='Chute Niagara')
        
    elif liste_images[0][0] == 'img17':
        aff=Label(cadre_fenetre1,text='Che Guevara')
        
    elif liste_images[0][0] == 'img18':
        aff=Label(cadre_fenetre1,text='Léonard de vinci')
        
    elif liste_images[0][0] == 'img19':
        aff=Label(cadre_fenetre1,text='Karl Marx')
        
    elif liste_images[0][0] == 'img20':
        aff=Label(cadre_fenetre1,text='Jason Statham')
    
    elif liste_images[0][0] == 'img21':             
        aff = Label(cadre_fenetre1, text= 'Zone 51')
           
    elif liste_images[0][0] == 'img22':
        aff=Label(cadre_fenetre1,text='Burj Khalifa')
        
    elif liste_images[0][0] == 'img23':
        aff=Label(cadre_fenetre1,text='Drapeau des _')
        
    elif liste_images[0][0] == 'img24':
        aff=Label(cadre_fenetre1,text='Léon Trotski')
        
    elif liste_images[0][0] == 'img25':
        aff=Label(cadre_fenetre1,text='Drapeau de _')
        
    elif liste_images[0][0] == 'img26':
        aff=Label(cadre_fenetre1,text='Drapeau de _')
        
    elif liste_images[0][0] == 'img27':
        aff=Label(cadre_fenetre1,text='Tour de _')
        
    elif liste_images[0][0] == 'img28':
        aff=Label(cadre_fenetre1,text='_ _')
        
    elif liste_images[0][0] == 'img29':
        aff=Label(cadre_fenetre1,text='Dalaï Lama')
        
    aff.pack()
def ElementFacile():
    '''Prend dans la table ImagesSonsFacile des éléments aléatoires et renvoit les bonnes images'''
    global liste_images
    global imageCan
    global score
    can1.grid()
    connexion = sqlite3.connect('DonneesCountryHunter.db')
    curseur = connexion.cursor()
    liste_id = [] #Contient les numéros des lignes dans la table
    liste_images =[] #Contient les noms des fichiers images sous forme d'une liste
    for i in range(10):
        num = (randint(1,14))
        while num in liste_id:           #Evite la répétition
            num = (randint(1,14))
        if num not in liste_id:
            liste_id.append(num)
        
    for num in liste_id:
        ligne =(num,)
        for nom in curseur.execute("SELECT nom FROM ImagesSonsFacile WHERE id =?",ligne):
            liste_images.append(nom) #On récupère le nom de l'image/son correspondant
    
    
    score=0
    chemin = 'Projet/images/' +liste_images[0][0]+'.png'
    img = PhotoImage(file=chemin)
    imageCan = can1.create_image(165,200, image = img)
    can2.bind("<Button-1>", pointeur)
    nomElement()
 
    
    connexion.close() 
    fenetre.mainloop()

def ElementNormal():
    '''Prend dans la table ImagesSonsFacile des éléments aléatoires et renvoit les bonnes images'''
    global liste_images
    global imageCan
    global score
    connexion = sqlite3.connect('DonneesCountryHunter.db')
    curseur = connexion.cursor()
    liste_id = [] #Contient les numéros des lignes dans la table
    liste_images =[] #Contient les noms des fichiers images sous forme d'une liste
    for i in range(10):
        num = (randint(15,26))
        while num in liste_id:      #Evite la répétition
            num = (randint(15,26))
        if num not in liste_id:
            liste_id.append(num)
        
    for num in liste_id:
        ligne =(num,)
        for nom in curseur.execute("SELECT nom FROM ImagesSonsFacile WHERE id =?",ligne):
            liste_images.append(nom) #On récupère le nom de l'image/son correspondant

    score = 0
    chemin = 'Projet/images/' +liste_images[0][0]+'.png'
    img = PhotoImage(file=chemin)
    imageCan = can1.create_image(165,200, image = img)
    can2.bind("<Button-1>", pointeur)
    nomElement()
        
    connexion.close() 
    fenetre.mainloop()

def ElementHunter():
    '''Prend dans la table ImagesSonsFacile des éléments aléatoires et renvoit les bonnes images'''
    global liste_images
    global imageCan
    global score
    global aff
    connexion = sqlite3.connect('DonneesCountryHunter.db')
    curseur = connexion.cursor()
    liste_id = [] #Contient les numéros des lignes dans la table
    liste_images =[] #Contient les noms des fichiers images sous forme d'une liste
    for i in range(3):
        num = (randint(27,29))
        while num in liste_id:  #Evite la répétition
            num = (randint(27,29))
        if num not in liste_id:
            liste_id.append(num)
            
    for num in liste_id:
        ligne =(num,)
        for nom in curseur.execute("SELECT nom FROM ImagesSonsFacile WHERE id =?",ligne):
            liste_images.append(nom) #On récupère le nom de l'image/son correspondant
            
    score = 0
    chemin = 'Projet/images/' +liste_images[0][0]+'.png'
    img = PhotoImage(file=chemin)
    imageCan = can1.create_image(165,200, image = img)
    can2.bind("<Button-1>", pointeur)
    nomElement()
    
    aff.pack()
    connexion.close() 
    fenetre.mainloop()

def transition():
    '''Gère la transition entre deux images et la fin du jeu'''
    global liste_images
    global imageCan
    liste_images.remove(liste_images[0])
    can1.delete(fenetre,imageCan)
    for mot in cadre_fenetre2.winfo_children():
        mot.destroy()                     #Retire la réponse et le score
    for mot in cadre_fenetre1.winfo_children():
        mot.destroy()
    if liste_images == []:                #Lorsqu'on a fait toutes les images
        fenfille = Toplevel()
        cadre_fenetre3= Frame(fenfille)
        cadre_fenetre3.grid()
        resultat = Label(cadre_fenetre3, text= 'FIN DU JEU \n Votre score final est de :'+str(score), font=('Arial',16))
        resultat.pack()
        if score == 1000:
            bravo = Label(cadre_fenetre3, text= 'Un sans faute !! Vous êtes un vrai Hunter bravo !')
            bravo.pack()
        elif 500<score<1000:
            bien = Label(cadre_fenetre3, text='Vous êtes bon, bien joué !')
            bien.pack()
        else:
            bof = Label(cadre_fenetre3, text="Vous pouvez faire mieux,c'est indéniable")
            bof.pack()
    else:
        chemin = 'Projet/images/' +liste_images[0][0]+'.png'
        img = PhotoImage(file=chemin)
        imageCan = can1.create_image(165,200, image = img)
        can2.bind("<Button-1>", pointeur)
        nomElement()
        fenetre.mainloop()
    

def pointeur(event): 
    '''Contrôle le clic de l'utilisateur et renvoie une réponse avec le score'''
    global liste_images
    global score
    X = event.x
    Y = event.y
    if liste_images[0][0] == 'img1':
        if 473 < event.x < 498 and 210 < event.y < 242:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()

    elif liste_images[0][0] == 'img2' or liste_images[0][0]== 'img14' or liste_images[0][0]== 'img21':
        if 110 < event.x < 280 and 225 < event.y < 290:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img3' or liste_images[0][0] == 'img18':
        if 500 < event.x < 531 and 226 < event.y < 262:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0]== 'img4' or liste_images[0][0]== 'img8' or liste_images[0][0]== 'img20':
        if 445 < event.x < 484 and 174 < event.y < 212:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img5':
        if 810 < event.x < 930 and 412 < event.y < 510:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img6':
        if 845 < event.x < 858 and 257 < event.y < 277:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img7' or liste_images[0][0] == 'img19':
        if 500 < event.x < 517 and 194 < event.y < 214:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
            500,214,517,194
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
                
    elif liste_images[0][0] == 'img9':
        if 538 < event.x < 553 and 248 < event.y < 264:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img10' or liste_images[0][0] == 'img11':
        if 694 < event.x < 874 and 195 < event.y < 315:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
        
                
    elif liste_images[0][0] == 'img12' or liste_images[0][0] == 'img27' or liste_images[0][0] == 'img28':
        if 874 < event.x < 894 and 248 < event.y < 269:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img13':
        if 305 < event.x < 360 and 388 < event.y < 450:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
        
                
    elif liste_images[0][0] == 'img15' or liste_images[0][0] == 'img17':
        if 620 < event.x < 657 and 565 < event.y < 625:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img16':
        if 416 < event.x < 620 and 118 < event.y < 325:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img22':
        if 626 < event.x < 650 and 295 < event.y < 317:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img23':
        if 484 < event.x < 507 and 190 < event.y < 210:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img24':
        if 553 < event.x < 1000 and 25 < event.y < 209:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img25':
        if 837 < event.x < 859 and 240 < event.y < 261:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img26':
        if 502 < event.x < 628 and 408 < event.y < 486:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img27':
        if 883 < event.x < 920 and 570 < event.y < 595:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        
    elif liste_images[0][0] == 'img28':
        if 883 < event.x < 920 and 570 < event.y < 595:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
                
    elif liste_images[0][0] == 'img29':
        if 883 < event.x < 920 and 570 < event.y < 595:
            score +=100
            reponse = Label(cadre_fenetre2,text='Bonne réponse !!!')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
        else:
            score -=100
            reponse = Label(cadre_fenetre2,text='Mauvaise réponse')
            reponse.pack()
            point = Label(cadre_fenetre2,text='score: '+str(score)+' points')
            point.pack()
    
    suivant = Button(cadre_fenetre2,text='Suivant',command=transition)
    suivant.pack()       

fenetre = Tk()
pygame.init()
fen2 = pygame.display.set_mode((300,300))
pygame.mixer.music.load('Projet/Musique/Huntew.wav')
if pygame.mixer.music.get_busy():
    pygame.mixer.music.rewind   #Si la musique est déjà lancé, elle est relancé (evite les superpositions)
else:                           
    pygame.mixer.music.play()
    
fenetre.geometry('1370x700')
fenetre.resizable(width=False, height=False)

can1= Canvas(fenetre,width = 340, height = 390) #Le canvas où y a le monument
can1.grid(row = 0, column = 0)
can1.create_rectangle(2,2,340,390)


cadre_fenetre1 = Frame(fenetre)                #Le cadre où il y a le nom du monument
cadre_fenetre1.grid(row = 1, column = 0)
warning = Label(cadre_fenetre1, text= '(Pour éviter toute erreur, merci de cliquer au centre du pays)')
warning.pack()

cadre_fenetre2 = Frame(fenetre)  #Pour afficher la réponse
cadre_fenetre2.grid(row = 2, column = 1)


can2 = Canvas(fenetre, width = 1150, height=575) #Le canvas où il y a la carte
can2.grid(row=0, column =1, rowspan = 2) 
chemin='Projet/Images/worldmap.gif'
background=PhotoImage(file=chemin)         
can2.create_image(508,290,image=background)
    
#Création d'une barre de menu en haut de la fenêtre graphique
menuBar=Menu(fenetre)
fenetre['menu'] = menuBar
#Création d'un menu simple avec commande
menu = Menu(menuBar)
menuBar.add_cascade(label='Classique', menu=menu)
menu.add_command(label='Facile', command=ElementFacile)
menu.add_command(label='Normal', command=ElementNormal)
menu.add_command(label='Hunter', command=ElementHunter)
fenetre.mainloop()
