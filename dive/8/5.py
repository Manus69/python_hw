import csv
import json

def csv_json(ifile, ofile, fnames : list):
    books = {}

    with open(ifile, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            author = row[fnames[0]]
            book = {fnames[1] : row[fnames[1]], fnames[2] : row[fnames[2]]}

            if author in books: books[author].append(book)
            else : books[author] = [book]

    with open(ofile, "r") as f:
        json.dump(books, f)