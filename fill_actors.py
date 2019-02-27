from Scrapping import *
from pymongo import MongoClient
from MongoDB import Actor
import re

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo
#je fais mon filtre sous forme de regex
def clean_actors(n):
    #n = n.replace("\n","").replace(".","").strip()
    n1 = re.sub('^\s+','',n)
    f = re.sub("\n","",n1)
    g = re.sub("\.","",f)
    return g
def clean_films(f):
    f = re.sub('\xa0',' ',f)
    return f

#je fais ma boucle pour mettre les acteur en keys et les films en values
dico = {}
for film in list(db.films.find()):
    if film.get('actors') is not None :
        for act in film.get('actors'):
            act1 = clean_actors(act)
            if act1 not in dico :
                dico[act1]=[]
                film1 = film.get('title')
                film2 = clean_films(film1)
            dico[act1].append(film2)

print(len(dico))
#je fais ma boucle pour tout mettre dans ma base données
for act,fil in dico.items() :
    acteur = Actor(act)
    for scene in fil :
        acteur.add_film(scene)
    acteur.load(db)

client.close()

    


