# Exercise 19: Clean the shelf

A scraper visited one page of an online bookstore and saved what it found in `src/shelf.py` as a list called
`books`: one dictionary per book, every value still the **raw text** from the page.

```python
{"title": "A Light in the Attic", "price": "£51.77", "stock": "In stock (22 available)", "rating": "star-rating Three"}
```

Turn the text into numbers, then answer three questions. Write these functions in `src/shelf.py`.

**Cleaning**

1. `first_number(text)` — the first number in the text as a **float**, or `None` if there isn't one.
2. `stock_count(text)` — the number of copies in stock as an **int**. `0` when the text shows no count.
3. `stars(text)` — the rating as an **int**, from text like `"star-rating Three"`. The `WORDS` dictionary in the file turns the word into a number.
4. `clean(books)` — row in, row out: a **new** list of dictionaries with keys `"title"`, `"price"` (float), `"stock"` (int), `"stars"` (int). Single `return`.

**Questions** (each takes the output of `clean`)

5. `total_value(rows)` — price times stock, summed over every book, rounded to 2 decimal places.
6. `deals(rows, max_price)` — titles of books rated **4 or more** stars that cost **at most** `max_price`, in the order they appear.
7. `mentions(rows, word)` — titles that mention `word`, in any capitalization.

```
rows = clean(books)
rows[0]                ->  {'title': 'A Light in the Attic', 'price': 51.77, 'stock': 22, 'stars': 3}
total_value(rows)      ->  7319.57
deals(rows, 25.00)     ->  ['The Boys in the Boat', "Shakespeare's Sonnets"]
mentions(rows, "the")  ->  7 titles, starting with 'A Light in the Attic'
```

## Tools you'll need

- `re.findall` to get the numbers out of a piece of text (Step 3 of the notebook).
- The `x if condition else None` guard from Practice 7, for text with no number in it.
- `re.search(word, text, re.IGNORECASE)` as the condition in a filter. It gives back a Match (counts as `True`) or `None` (counts as `False`). This is the "Bonus" at the end of Step 5.

## Watch for

- In `price_to_float` you deleted everything that wasn't a digit or a period. That works on a price, but try it on `"Rated 4.5 by 1,234 users"`: every digit gets glued together into one wrong number, with no error. `first_number` has to **find** the number, not delete around it. One test checks exactly this.
- One price starts with `Â£` instead of `£`. That's what a site sends when the page's encoding is read wrong. A pattern that looks for digits doesn't care.
- Two books show `In stock` with no count. `first_number` gives `None` there; `stock_count` turns that into `0`.
- One book costs exactly `22.60`. Read *at most* carefully.
- `stars` needs no regex at all. Not everything does.

## Running the tests

From the top folder of this repo:

```
python -m unittest discover
```

Run `python src/shelf.py` from the top folder after each function you write. It runs the examples from
each docstring, so you can compare what prints to what the docstring says before running the tests.

**Where this list came from:** on a real bookstore page, the price, stock, and rating come back from the
scraper looking exactly like this. Next unit you'll write the scraper. These functions are the half that
comes after it.
