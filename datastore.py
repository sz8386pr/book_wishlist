''' json related code reference from http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/ '''
import json
import os
from book import Book
from datetime import datetime
import wishlistIO

'''moved to io.py
DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')'''

#separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    data, counter = wishlistIO.read_files()

    if data != None:
        make_book_list(data)

    if counter == 0:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''
    global counter

    output_data = make_output_data()
    wishlistIO.save_files(output_data, counter)


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books

    elif 'id' in kwargs:
        search_book = [ book for book in book_list if book.id == kwargs['id'] ]
        return search_book

    elif 'title' in kwargs:
        search_book = [ book for book in book_list if book.title == kwargs['title'] ]
        return search_book

    elif 'author' in kwargs:
        search_book = [ book for book in book_list if book.author == kwargs['author'] ]
        return search_book

    elif 'rating' in kwargs:
        search_book = [ book for book in book_list if book.rating == kwargs['rating'] ]
        return search_book


def add_book(book):
    ''' Check for duplicates, Add to db, set id value, return True/False '''

    global book_list

    for books in book_list:
        if book.title == books.title and book.author == books.author and books.read == False:
            print("Book already located and is still unread")
            return False
        elif book.title == books.title and book.author == books.author and books.read == True:
            print("Book has been read, would you still like to add")
            answer = ""
            while not answer == "Y" or answer == "N":
                answer = input("Enter Y or N: ")
                if answer.upper() == "Y":
                    book.id = generate_id()
                    book_list.append(book)
                    return True
                elif answer.upper() == "N":
                    return False
    book.id = generate_id()
    book_list.append(book)
    return True



def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read and save the date finished by month-day-year.
    Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            while True:
                try:
                    rating = int(input("Enter the book rating from 0 to 5: "))
                    if rating >= 0 or rating <= 5:
                        book.rating = rating
                        break
                except ValueError:
                    print("Enter numbers only")

            book.read = read

            finished = datetime.now().date().strftime('%m-%d-20%y')
            book.finished = finished

            return True

    return False # return False if book id is not found



def make_book_list(data):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    # books_str = string_from_file.split('\n')
    #
    # for book_str in books_str:
    #     data = book_str.split(separator)
    #     book = Book(data[0], data[1], data[2] == 'True', int(data[3]))
    #     book_list.append(book)

    for info in data["book"]:
        book = Book(info["title"], info["author"], info["book"], info["id"], info["rating"], info["finished"])
        book_list.append(book)



def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    #     output_data = []
    #
    #     for book in book_list:
    #         output = [ book.title, book.author, str(book.read), str(book.id) ]
    #         output_str = separator.join(output)
    #         output_data.append(output_str)
    #
    #     all_books_string = '\n'.join(output_data)
    #
    #     return all_books_string

    output_data = {}
    output_data["book"] = []

    for book in book_list:
        output_data["book"].append({"title": book.title, "author": book.author,
        "book": book.read, "id": book.id, "rating": book.rating, "finished": book.finished})

    return output_data

def edit_book(book_id):
    ''' edit book author and/or title by book_id '''

    global book_list

    for book in book_list:

        if book.id == book_id:
            print("Current book - Author: {} Title: {}\n".format(book.author, book.title))

            edit_author = ""
            while not (edit_author.upper() == "Y" or edit_author.upper() == "N"):
                edit_author = input("Would you like to edit the author? (Y or N)")
                if edit_author.upper() == 'Y':
                    new_author = input("Enter new author: ")
                    book.author = new_author
                    break
                elif edit_author.upper() != 'N':
                    edit_author = input("Enter (Y or N)")


            edit_title = ""
            while not (edit_title.upper() == "Y" or edit_title.upper() == "N"):
                edit_title = input("Would you like to edit the title? (Y or N)")
                if edit_title.upper() == 'Y':
                    new_title = input("Enter new title: ")
                    book.title = new_title
                    break
                elif edit_title.upper() != 'N':
                    edit_title = input("Enter (Y or N)")



def delete_book(book_id):
    ''' delete book by book_id '''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book_list.remove(book)
            return True

    return False # return False if book id is not found
