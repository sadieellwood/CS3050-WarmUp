"""

"""

class Movie:
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
        if num < 0 or num > 10:
            raise ValueError("Rating cannot be less than zero or more than ten!")
        self._rating = num
        
    def from_dict():
        pass
    
    def to_dict():
        pass
    
    def validate_query():
        pass
    
    def perform_firebase_query():
        pass
    
    def do_query():
        validate_query()
        perform_firebase_query()
    