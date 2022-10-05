

books_file = 'books.json'

# funkcia prida knihy do file


def add_books(name, author):
    with open('books.txt', 'a') as file:
        file.write(f"{name} by {author}, 0")

# funkcia nacita vsetky knihy z file


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.split(',').strip() for line in file.readlines()]
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines]


def mark_as_read():
    books = get_all_books(name)
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
            _save_all_books()


def _save_all_books(book):
    with open(books_file, 'w') as file:
        file.write(f"{book['name']}, {book['author']}, {book['read']} \n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
