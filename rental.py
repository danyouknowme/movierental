from __future__ import annotations
from enum import Enum
from datetime import datetime
from movie import Movie


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior."""
    new_release = {"price": lambda days: 3 * days,
                   "frp": lambda days: days,
                   }
    regular = {"price": lambda days: 2.0 if days <= 2 else 2.0 + (1.5 * (days - 2)),
               "frp": lambda days: 1,
               }
    children = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
                "frp": lambda days: 1,
                }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def frequent_renter_points(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        frp = self.value["frp"]
        return frp(days)

    @classmethod
    def for_movie(cls, movie: Movie) -> PriceCode:
        current_year = str(datetime.now().year)
        children_genre = "Children"
        if movie.get_year() == current_year:
            return cls.new_release
        elif children_genre in movie.get_genre():
            return cls.children
        else:
            return cls.regular


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code: float = PriceCode.for_movie(movie)

    def get_movie(self) -> str:
        return self.movie

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_charge(self) -> float:
        return self.price_code.price(self.days_rented)

    def get_frequent_renter_points(self, frequent_renter_points: float = 0) -> float:
        frequent_renter_points += self.price_code.frequent_renter_points(
            self.days_rented)
        return frequent_renter_points
