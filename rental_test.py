import unittest
from rental import Rental, PriceCode
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", str(datetime.now().year), ["Children"])
        self.regular_movie = Movie("CitizenFour", "2014", [
            "Documentary", "Historical Documentary"])
        self.childrens_movie = Movie("Frozen", "2013", [
            "Adventure", "Children", "Cartoon",
            "Musical", "Comedy", "Fantasy"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", "2014", [
            "Documentary", "Historical Documentary"])
        self.assertEqual("CitizenFour", m.get_title())
        self.assertEqual(PriceCode.regular, PriceCode.for_movie(m))

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_charge(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_charge(), 15.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_charge(), 2)
        rental = Rental(self.regular_movie, 10)
        self.assertEqual(rental.get_charge(), 14.0)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 7)
        self.assertEqual(rental.get_charge(), 7.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.new_movie, 4)
        self.assertEqual(rental.get_frequent_renter_points(), 4)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.regular_movie, 8)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.childrens_movie, 16)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
