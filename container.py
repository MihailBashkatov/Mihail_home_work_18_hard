# Импорт DAO и ServiceDAO трех классов: Director, Genre, Movie
from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService

# Импорт базы данных
from setup_db import db

# формирование экземляров DAO и ServiceDAO трех классов: Director, Genre, Movie
movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
