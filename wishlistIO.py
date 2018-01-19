import json
import os

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

def read_files():
    try :
        with open(BOOKS_FILE_NAME) as f:
            # data = f.read()
            data = json.load(f)

    except FileNotFoundError:
        # First time program has run. Assume no books.
        data = None

    # If the program cannot read the counter file, return 0 and let the datastore calculate the new counter from the book_list
    try:
        with open(COUNTER_FILE_NAME) as f:
            counter = int(f.read())
    except:
        counter = 0

    return data, counter


def save_files(output_data, counter):
    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        # f.write(output_data)
        json.dump(output_data, f)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))
