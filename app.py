import utils.storage_database as database

MENU_PROMPT = """
Enter a choice:

a - add book
l - list all books
r - to mark a book as read
d - delete book
q - quit
s - save to file 

"""


def menu():
    database.create_book_table()
    user_choice = input(MENU_PROMPT)
    while user_choice != 'q':
        if user_choice == 'a':
            prompt_add_book()
        elif user_choice == 'l':
            list_books()
        elif user_choice == 'r':
            mark_as_read()
        elif user_choice == 'd':
            prompt_delete_book()
        elif user_choice == 's':
            save_to_file()
        else:
            print('Unknown command, TRY again')
        user_choice = input(MENU_PROMPT)


def prompt_add_book():
    book_name = input('Enter book name:\n')
    author = input('Enter book author:\n')
    database.add_books(book_name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read:{read}")


def mark_as_read():
    user_input = input('Please enter a book name\n')
    for book in database.books:
        if user_input == book['name']:
            book['read'] = True
        else:
            print('Unknown book, try again later')


def prompt_delete_book():
    book_name = input('Enter a book name you want delete\n')
    books = database.get_all_books()
    new_books = [book for book in books if book['name'] != book_name]
    database.books = new_books


def save_to_file():
    with open('books.txt', 'w') as file:
        for book in database.books:
            file.write(f"{book['name']} by {book['author']}")


menu()
