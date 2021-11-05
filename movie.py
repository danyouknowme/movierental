from typing import List

class Movie:
    """A movie available for rent."""

    # The types of movies (price_code).

    def __init__(self, title, genre):
        # Initialize a new movie.
        self.title = title
        self.genre: List[str] = genre

    def get_title(self):
        return self.title

    def get_genre(self) -> List[str]:
        return self.genre

    def is_genre(self, movie: str) -> bool:
        """Returns true if the string parameter matches one of the movie’s genre."""
        return movie in self.genre

    def __str__(self):
        return self.title
