import re

# What a scraper collected from one page of books.toscrape.com: one dictionary per book,
# every value still the raw text from the page. Nothing here has been cleaned yet.
books = [
    {"title": "A Light in the Attic",                  "price": "£51.77",  "stock": "In stock (22 available)",          "rating": "star-rating Three"},
    {"title": "Tipping the Velvet",                    "price": "£53.74",  "stock": "In stock (20 available)",          "rating": "star-rating One"},
    {"title": "Soumission",                            "price": "£50.10",  "stock": "\n    In stock (20 available)\n",  "rating": "star-rating One"},
    {"title": "Sharp Objects",                         "price": "Â£47.82", "stock": "In stock (20 available)",          "rating": "star-rating Four"},
    {"title": "Sapiens: A Brief History of Humankind", "price": "£54.23",  "stock": "In stock (20 available)",          "rating": "star-rating Five"},
    {"title": "The Requiem Red",                       "price": "£22.65",  "stock": "In stock (19 available)",          "rating": "star-rating One"},
    {"title": "The Dirty Little Secrets of Getting Your Dream Job", "price": "£33.34", "stock": "In stock (19 available)", "rating": "star-rating Four"},
    {"title": "The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull", "price": "£17.93", "stock": "In stock (19 available)", "rating": "star-rating Three"},
    {"title": "The Boys in the Boat",                  "price": "£22.60",  "stock": "In stock",                         "rating": "star-rating Four"},
    {"title": "The Black Maria",                       "price": "£52.15",  "stock": "\n    In stock\n",                 "rating": "star-rating One"},
    {"title": "Starving Hearts (Triangular Trade Trilogy, #1)", "price": "£13.99", "stock": "In stock (19 available)", "rating": "star-rating Two"},
    {"title": "Shakespeare's Sonnets",                 "price": "£20.66",  "stock": "In stock (19 available)",          "rating": "star-rating Four"},
]

WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

# Three made-up rows that are already clean. The examples below use them, so you can
# try total_value, deals, and mentions before clean() works.
sample = [
    {"title": "The Cat in the Hat", "price": 10.00, "stock": 3, "stars": 5},
    {"title": "Hat Tricks",         "price": 20.50, "stock": 2, "stars": 4},
    {"title": "Another Book",       "price": 5.25,  "stock": 0, "stars": 2},
]


def first_number(text):
    """The first number in the text as a float, or None if there isn't one.

    first_number("£51.77")                    ->  51.77
    first_number("Â£47.82")                   ->  47.82
    first_number("In stock (22 available)")   ->  22.0
    first_number("1,234 reviews")             ->  1234.0
    first_number("Rated 4.5 by 1,234 users")  ->  4.5
    first_number("In stock")                  ->  None
    """
    pass


def stock_count(text):
    """The number of copies in stock, as an int. 0 when the text shows no count.

    stock_count("In stock (19 available)")  ->  19
    stock_count("In stock")                 ->  0
    """
    pass


def stars(text):
    """The star rating as an int, from text like "star-rating Three". Use the WORDS dictionary.

    stars("star-rating Three")  ->  3
    stars("star-rating Five")   ->  5
    """
    pass


def clean(books):
    """Row in, row out: a new list of dictionaries with the same titles and numeric price, stock, and stars.

    clean(books)[0]  ->  {'title': 'A Light in the Attic', 'price': 51.77, 'stock': 22, 'stars': 3}
    clean(books)[8]  ->  {'title': 'The Boys in the Boat', 'price': 22.6, 'stock': 0, 'stars': 4}
    """
    pass


def total_value(rows):
    """Price times stock, summed over every book, rounded to 2 decimal places.

    total_value(sample)  ->  71.0        (10.00*3 + 20.50*2 + 5.25*0)
    """
    pass


def deals(rows, max_price):
    """Titles of books rated 4 or more stars that cost at most max_price, in page order.

    deals(sample, 25.00)  ->  ['The Cat in the Hat', 'Hat Tricks']
    deals(sample, 20.50)  ->  ['The Cat in the Hat', 'Hat Tricks']    (exactly 20.50 counts)
    deals(sample, 15.00)  ->  ['The Cat in the Hat']
    deals(sample, 5.00)   ->  []
    """
    pass


def mentions(rows, word):
    """Titles that mention the word, in any capitalization.

    mentions(sample, "HAT")     ->  ['The Cat in the Hat', 'Hat Tricks']
    mentions(sample, "the")     ->  ['The Cat in the Hat', 'Another Book']    ("Another" has "the" in it)
    mentions(sample, "dragon")  ->  []
    """
    pass


def main():
    # Run `python src/shelf.py` and compare each line to the examples in the docstrings.
    print('first_number("£51.77")                    -> ', first_number("£51.77"))
    print('first_number("Â£47.82")                   -> ', first_number("Â£47.82"))
    print('first_number("In stock (22 available)")   -> ', first_number("In stock (22 available)"))
    print('first_number("1,234 reviews")             -> ', first_number("1,234 reviews"))
    print('first_number("Rated 4.5 by 1,234 users")  -> ', first_number("Rated 4.5 by 1,234 users"))
    print('first_number("In stock")                  -> ', first_number("In stock"))
    print('stock_count("In stock (19 available)")    -> ', stock_count("In stock (19 available)"))
    print('stock_count("In stock")                   -> ', stock_count("In stock"))
    print('stars("star-rating Three")                -> ', stars("star-rating Three"))
    print('stars("star-rating Five")                 -> ', stars("star-rating Five"))
    print('total_value(sample)                       -> ', total_value(sample))
    print('deals(sample, 25.00)                      -> ', deals(sample, 25.00))
    print('deals(sample, 20.50)                      -> ', deals(sample, 20.50))
    print('deals(sample, 15.00)                      -> ', deals(sample, 15.00))
    print('deals(sample, 5.00)                       -> ', deals(sample, 5.00))
    print('mentions(sample, "HAT")                   -> ', mentions(sample, "HAT"))
    print('mentions(sample, "the")                   -> ', mentions(sample, "the"))
    print('mentions(sample, "dragon")                -> ', mentions(sample, "dragon"))

    rows = clean(books)
    if rows is None:
        print("Finish clean() to see the answers for the real shelf.")
    else:
        print()
        print("The real shelf")
        print(rows[0])
        print(rows[8])
        print(total_value(rows))
        print(deals(rows, 25.00))
        print(mentions(rows, "the"))


if __name__ == "__main__":
    main()
