import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 451)

    def test_get_actors(self):
        film = Film("tt7215444")
        self.assertEqual(film.get_actors(db), db.films.find_one({"imdb_id" : "tt7215444"}).get('actors'))

    def TestFilmMethods(self):
        self.assertEqual(Actor.get_nb_actors(db), db.actors.find().count())

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()
