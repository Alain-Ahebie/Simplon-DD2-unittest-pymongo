class Film:

  def __init__(self, id):
    self.id = id

  def get_nb_films(db):
    
    self = len(list(db.films.find()))
      # retourne le nombre de films présents dans la base

    return self
    
  def get_actors(self,db):
  # retourne la liste des acteurs d'un film
    c = db.films.find_one({"imdb_id" : self.id}).get('actors')
    return c

class Actor:

  def __init__(self, name):
    self.name = name
    self.films = []

  def add_film(self, film):
    self.films.append(film)

  def load(self, db):
    film_dict = {self.name : self.films}

    film_coll = db.actors
    film_coll.insert_one(film_dict)
    # ajoute l'acteur dans la base de données

  def get_nb_actors(db):
    # retourne le nombre d'acteurs présents dans la base

    return db.actors.find().count()
    

