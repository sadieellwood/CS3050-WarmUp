import firebase_connection
import movie_gui
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
        
    
    # convert dictionary to dataframe
    def from_dict(dt):
        movie_db = pd.DataFrame.from_dict(dt)
        return movie_db
    
    # convert dataframe to dictionary
    def to_dict(db):
        movie_dt = pd.DataFrame.to_dict(db)
        return movie_dt
    
    # running query functions
    def validate_query():
        user_query = movie_gui.user_parsed(_)
        # query validation (reference example query)
    
    def perform_firebase_query():
        pass
    
    def do_query():
        validate_query()
        perform_firebase_query()
    