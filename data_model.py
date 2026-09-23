import firebase_connection as fire
import movie_gui as gui
import pandas as pd

class Movie:
    # constructor
    def __init__(self, series, release_date, title, rating):
        self._series = series
        self._release_date = release_date
        self._title = title
        self._rating = rating
    
    # getters
    @property
    def series(self):
        return self._series
    
    @property
    def release_date(self):
        return self._release_date
    
    @property
    def title(self):
        return self._title
    
    @property
    def rating(self):
        return self._rating
    
    # setters
    @series.setter
    def series(self, name):
        self._series = name
    
    @release_date.setter
    def release_date(self, date):
        self._release_date = date
        
    @title.setter
    def title(self, name):
        self._title = name
        
    @rating.setter
    def rating(self, num):
        if num < 0 or num > 6.7:
            raise ValueError("Rating cannot be less than 0 or more than 6.7!")
        self._rating = num
    
    # running query functions
    def validate_query(user_query):
        # query validation (make sure logically sound)
        
        # expression 1
        if user_query[expr1['field']] == 'Series':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr1['field']] == 'Date':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr1['field']] == 'Title':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr1['field']] == 'Rating':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
            
        # logical operator
        if user_query['comparison_op'] != '<' or\
        user_query['comparison_op'] != '==' or\
        user_query['comparison_op'] != '>' or\
        user_query['comparison_op'] != '>=' or\
        user_query['comparison_op'] != '=<':
            return print('Type a logical operator')
            
        # expression 2
        if user_query[expr2['field']] == 'Series':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr2['field']] == 'Date':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr2['field']] == 'Title':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
        if user_query[expr2['field']] == 'Rating':
            if isInstance(user_query[expr1['value']], str) == false:
                return print('This is not a string!')
    
    # take user input and send to firebase (same as select statement frm databases)
    def perform_firebase_query(user_query):
        pass
    
    def do_query(user_query):
        validate_query(user_query)
        perform_firebase_query(user_query)
    
    # takes firebase thing and converts into list of movie objects
    # (does not take into consideration doc yet)
    def from_dict(user_query):
        movie_list = []
        db = do_query(user_query)
        for i in db:
            mov_obj = Movie(db[i][0], db[i][1], db[i][2], db[i][3])
            movie_list.append(mov_obj)
        return movie_list
    