class MovieService:
    def __init__(self):
        self.movies = []
        self.counter = 1

    def get_all_movies(self):
        return self.movies

    def add_movie(self, title, genre, year, classification):
        movie = {"id": self.counter, "title": title, "genre": genre, "year": year, "classification": classification}
        self.movies.append(movie)
        self.counter += 1

    def delete_movie(self, movie_id):
        self.movies = [m for m in self.movies if m["id"] != movie_id]

    def update_movie(self, movie_id, title, genre, year, classification):
        # Buscar la película por ID
        for movie in self.movies:
            if movie["id"] == movie_id:
                movie["title"] = title
                movie["genre"] = genre
                movie["year"] = year
                movie["classification"] = classification
                return movie
        return None  # Retorna None si no encuentra la película
