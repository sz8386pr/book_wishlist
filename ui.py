from book import Book
import operator


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Delete book from wishlist
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice

def sort_by():
    ''' book display sorting option '''

    while True:
        print('''
            Sort by...
            1. Book ID
            2. Book title
            3. Book author
        ''')

        choice = input('Enter your selection: ')

        if choice == "1":
            return "id"
        elif choice == "2":
            return "title"
        elif choice == "3":
            return "author"
        else:
            message('Please enter a valid selection')


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print ('* No books *')
        return

    sorted_list(books) # Display sorted book list

    print('* {} book(s) *'.format(len(books)))


def sorted_list(books):
    ''' sort the book list by user order
    reference from https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python for sort a list of class instances'''

    sort = sort_by() # Get the sort option
    ordered_books = sorted(books, key=operator.attrgetter(sort)) # Sort by id/title/author. Original list is unaltered by using sorted() method

    for book in ordered_books:
        print(book)


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)
