from tkinter import messagebox
import mysql.connector
from tkinter import *

screen = Tk()
screen.title("Gestion de stock Boutique")
screen.geometry("400x310")

ma_bdd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mouf",
    database="boutique",
)

if ma_bdd.is_connected():
    print("Connexion à la BDD réussie.")
else:
    print("Connexion à la BDD échoué.")

result_listbox = Listbox(screen)
result_listbox.place(x=10, y=40)
result_listbox.config(width=63)

title = Label(screen, text="GESTION DE STOCK :", font=("arial", 15, "bold"), fg="black")
title.place(x=90, y=5)

boutique = ma_bdd.cursor()

boutique.execute("select * from produit")

resultat_stock = boutique.fetchall()

for resultat in resultat_stock:
    produit = resultat[0]  
    stock = resultat[1]  
    result_listbox.insert(END, f"{produit}: {stock}")  



def ajouter_produit():
    fenetre = Toplevel(screen)
    fenetre.title("Ajouter un produit")
    fenetre.geometry("300x140")

    label_nom = Label(fenetre, text="Nom du produit :")
    label_nom.grid(row=0, column=0)
    champ_nom = Entry(fenetre)
    champ_nom.grid(row=0, column=1)

    label_description = Label(fenetre, text="Description :")
    label_description.grid(row=1, column=0)
    champ_description = Entry(fenetre)
    champ_description.grid(row=1, column=1)

    label_prix = Label(fenetre, text="Prix :")
    label_prix.grid(row=2, column=0)
    champ_prix = Entry(fenetre)
    champ_prix.grid(row=2, column=1)

    label_quantite = Label(fenetre, text="Quantité :")
    label_quantite.grid(row=3, column=0)
    champ_quantite = Entry(fenetre)
    champ_quantite.grid(row=3, column=1)

    label_categorie = Label(fenetre, text="ID catégorie :")
    label_categorie.grid(row=4, column=0)
    champ_categorie = Entry(fenetre)
    champ_categorie.grid(row=4, column=1)

    bouton_valider = Button(fenetre, text="Valider", command=lambda:
    enregistrer_produit(champ_nom.get(),
                        champ_description.get(),
                        champ_prix.get(),
                        champ_quantite.get(),
                        champ_categorie.get()))
    bouton_valider.grid(row=5, column=1)


def enregistrer_produit(nom, description, prix, quantite, id_categorie):
    curseur = ma_bdd.cursor()

    requete = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
    valeurs = (nom, description, prix, quantite, id_categorie)
    curseur.execute(requete, valeurs)

    ma_bdd.commit()

    messagebox.showinfo("Le produit a été ajouté avec succès")


boutton_add = Button(screen, text="Ajouter un produit", command=ajouter_produit)
boutton_add.place(x=50, y=220, height=30, width=140)


def supp_produit():
    fenetre = Toplevel(screen)
    fenetre.title("Supprimer un produit")
    fenetre.geometry("300x50")

    label_nom = Label(fenetre, text="N°ID du produit à supprimer :")
    label_nom.grid(row=0, column=0)
    champ_nom = Entry(fenetre)
    champ_nom.grid(row=0, column=1)

    bouton_suppri = Button(fenetre, text="Supprimer", command=lambda: suppression(champ_nom.get()))
    bouton_suppri.grid(row=5, column=1)


def suppression(id):
    curseur = ma_bdd.cursor()

    requete = 'delete from produit where id = %s'
    valeur = (id,)
    curseur.execute(requete, valeur)

    ma_bdd.commit()

    messagebox.showinfo("Le produit a été supprimé avec succès")


boutton_del = Button(screen, text="Supprimer un produit", command=supp_produit)
boutton_del.place(x=130, y=255, height=30, width=140)


def modifier_produit():
    fenetre = Toplevel(screen)
    fenetre.title("Modifier un produit")
    fenetre.geometry("300x160")

    label_id = Label(fenetre, text="ID du produit :")
    label_id.grid(row=0, column=0)
    champ_id = Entry(fenetre)
    champ_id.grid(row=0, column=1)

    label_nom = Label(fenetre, text="Nom du produit :")
    label_nom.grid(row=1, column=0)
    champ_nom = Entry(fenetre)
    champ_nom.grid(row=1, column=1)

    label_description = Label(fenetre, text="Description :")
    label_description.grid(row=2, column=0)
    champ_description = Entry(fenetre)
    champ_description.grid(row=2, column=1)

    label_prix = Label(fenetre, text="Prix :")
    label_prix.grid(row=3, column=0)
    champ_prix = Entry(fenetre)
    champ_prix.grid(row=3, column=1)

    label_quantite = Label(fenetre, text="Quantité :")
    label_quantite.grid(row=4, column=0)
    champ_quantite = Entry(fenetre)
    champ_quantite.grid(row=4, column=1)

    label_categorie = Label(fenetre, text="ID catégorie :")
    label_categorie.grid(row=5, column=0)
    champ_categorie = Entry(fenetre)
    champ_categorie.grid(row=5, column=1)

    bouton_valider = Button(fenetre, text="Valider", command=lambda: enregistrer_modifications(champ_id.get(), champ_nom.get(), champ_description.get(), champ_prix.get(), champ_quantite.get(), champ_categorie.get()))
    bouton_valider.grid(row=6, column=1)


def enregistrer_modifications(id, nom, description, prix, quantite, id_categorie):
    curseur = ma_bdd.cursor()

    requete = "UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id_produit = %s"
    valeurs = (nom, description, prix, quantite, id_categorie, id)
    curseur.execute(requete, valeurs)

    ma_bdd.commit()

    messagebox.showinfo("Le produit a été modifié avec succès")




boutton_change = Button(screen, text="Modifier un produit", command=modifier_produit)
boutton_change.place(x=210, y=220, height=30, width=140)


screen.mainloop()
