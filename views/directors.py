# Импорт необходимых библиотек
from flask_restx import Namespace, Resource

# Импорт экземпляра класса GenreService
from container import director_service

# Импорт экземпляра класса GenreService
from dao.model.director import DirectorSchema

# Формирование нэймспейса
directors_ns = Namespace('directors')

# Формирование сереилизаторов для модели Director для одного элемента и для списка
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """
        try:
            directors = director_service.get_directors()
            return directors_schema.dump(directors), 200
        except Exception as e:
            return e, 404


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """
            Формирование представления для получения жанра по режиссеру
            В случае отсутствия режиссера возвращается 'No such movie'
        """
        try:
            director = director_service.get_director(did)
            if director_schema.dump(director) == {}:
                return 'No such movie', 200
            return genre_schema.dump(director), 200
        except Exception as e:
            return e, 404
