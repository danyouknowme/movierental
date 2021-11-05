from rental import PriceCode

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
