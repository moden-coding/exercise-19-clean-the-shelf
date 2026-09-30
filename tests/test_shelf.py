import unittest

from src.shelf import (books, first_number, stock_count, stars, clean,
                       total_value, deals, mentions)


class TestFirstNumber(unittest.TestCase):
    def test_price(self):
        self.assertEqual(first_number("£51.77"), 51.77)

    def test_bad_encoding_is_ignored(self):
        self.assertEqual(first_number("Â£47.82"), 47.82)

    def test_number_inside_text_with_whitespace(self):
        self.assertEqual(first_number("\n    In stock (22 available)\n"), 22.0)

    def test_comma_thousands(self):
        self.assertEqual(first_number("1,234 reviews"), 1234.0)

    def test_first_of_several(self):
        self.assertEqual(first_number("Rated 4.5 by 1,234 users"), 4.5,
                         "deleting every non-digit glues these into one number")

    def test_none_when_no_number(self):
        self.assertIsNone(first_number("In stock"))


class TestStockCount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(stock_count("In stock (19 available)"), 19)

    def test_returns_int(self):
        self.assertIsInstance(stock_count("In stock (19 available)"), int)

    def test_no_count_is_zero(self):
        self.assertEqual(stock_count("In stock"), 0)
        self.assertEqual(stock_count("\n    In stock\n"), 0)


class TestStars(unittest.TestCase):
    def test_words(self):
        self.assertEqual(stars("star-rating One"), 1)
        self.assertEqual(stars("star-rating Five"), 5)


class TestClean(unittest.TestCase):
    def test_first_row(self):
        self.assertEqual(clean(books)[0], {"title": "A Light in the Attic", "price": 51.77, "stock": 22, "stars": 3})

    def test_row_with_no_count(self):
        self.assertEqual(clean(books)[8], {"title": "The Boys in the Boat", "price": 22.6, "stock": 0, "stars": 4})

    def test_length_and_originals_untouched(self):
        rows = clean(books)
        self.assertEqual(len(rows), 12)
        self.assertEqual(books[0]["price"], "£51.77", "the original list should be untouched")


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.rows = clean(books)

    def test_total_value(self):
        self.assertEqual(total_value(self.rows), 7319.57)

    def test_deals(self):
        self.assertEqual(deals(self.rows, 25.00), ["The Boys in the Boat", "Shakespeare's Sonnets"])

    def test_deals_boundary(self):
        self.assertEqual(deals(self.rows, 22.60), ["The Boys in the Boat", "Shakespeare's Sonnets"],
                         "a book costing exactly max_price counts")
        self.assertEqual(deals(self.rows, 22.59), ["Shakespeare's Sonnets"])

    def test_deals_none(self):
        self.assertEqual(deals(self.rows, 5), [])

    def test_mentions_any_case(self):
        self.assertEqual(mentions(self.rows, "LIFE"),
                         ["The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull"])

    def test_mentions_count(self):
        self.assertEqual(len(mentions(self.rows, "the")), 7)

    def test_mentions_none(self):
        self.assertEqual(mentions(self.rows, "dragon"), [])


if __name__ == "__main__":
    unittest.main()
