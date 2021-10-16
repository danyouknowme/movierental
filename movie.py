from enum import Enum


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

    def price(self, days: int):
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def frequent_renter_points(self, days: int):
        """Return the rental price for a given number of days."""
        frp = self.value["frp"]
        return frp(days)


class Movie:
    """A movie available for rent."""

    # The types of movies (price_code).
    REGULAR = PriceCode.regular
    NEW_RELEASE = PriceCode.new_release
    CHILDRENS = PriceCode.children

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
