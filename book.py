class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1
    NO_RATING = -1
    NO_FINISHED = ''

    def __init__(self, title, author, read=False, id=NO_ID, rating=NO_RATING, finished=NO_FINISHED):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.id = id
        self.rating = rating
        self.finished = finished


    def set_id(self, id):
        self.id = id

    def set_rating(self, rating):
        self.rating = rating

    def set_finished(self, finished):
        self.finished = finished

    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        ''' prints/draws rating in stars out of 5'''
        rating = self.rating
        if rating == -1:
            rating_str = '(not rated)'
        else:
            rating_str = ""
            for x in range(rating):
                rating_str += "★"
            for i in range(5-rating):
                rating_str += "☆"

        finished_str = self.finished
        if finished_str == '':
            finished_str = ('(n/a)')

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {} Finished On: {}'
        return template.format(id_str, self.title, self.author, read_str, rating_str, finished_str)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.rating == other.rating and self.finished == other.finished
