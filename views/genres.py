# Импорт необходимых библиотек
from flask_restx import Namespace, Resource

# Импорт экземпляра класса GenreService
from container import genre_service

# Импорт экземпляра класса GenreService
from dao.model.genre import GenreSchema

# Формирование нэймспейса
genres_ns = Namespace('genres')

# Формирование сереилизаторов для модели Genre для одного элемента и для списка
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """
        try:
            genres = genre_service.get_genres()
            return genres_schema.dump(genres), 200
        except Exception as e:
            return e, 404


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """
            Формирование представления для получения жанра по id
            В случае отсутствия фильма возвращается 'No such movie'
        """
        try:
            genre = genre_service.get_genre(gid)
            if genre_schema.dump(genre) == {}:
                return 'No such movie', 200
            return genre_schema.dump(genre), 200
        except Exception as e:
            return e, 404
