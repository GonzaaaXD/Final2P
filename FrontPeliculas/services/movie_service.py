class MovieService:
    def __init__(self):
        self.movies = []
        self.counter = 1

    def get_all_movies(self):
        return self.movies

    def add_movie(self, title, genre, year, rating):
        movie = {"id": self.counter, "title": title, "genre": genre, "year": year, "rating": rating}
        self.movies.append(movie)
        self.counter += 1

    def delete_movie(self, movie_id):
        self.movies = [m for m in self.movies if m["id"] != movie_id]
