from firebase_connection import Firebase
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
    def validate_query(query):
        
        # convert date into actual date object with try except
        
        try:
            # convert rating into float
            for key in result.keys():
                if key == "logical_op":
                    pass

                elif "rating" in result[key].values():
                    result[key]["value"] = float(result[key]["value"])

            return True, result

        except pp.ParseException as e:
            message = "Invalid query! Check help window for correct syntax."
            return False, message
        
        # query validation (make sure logically sound)

        # expression 1
        if query[expr1["field"]] == "Series":
            if isinstance(query[expr1["value"]], str) == False:
                return print("This is not a string!")
        if query[expr1["field"]] == "Date":
            if isinstance(query[expr1["value"]], str) == False:
                return print("This is not a string!")
        if query[expr1["field"]] == "Title":
            if isinstance(query[expr1["value"]], str) == False:
                return print("This is not a string!")
        if query[expr1["field"]] == "Rating":
            if isinstance(query[expr1["value"]], float) == False:
                return print("This is not a float!")

        # logical operator
        if isinstance(query[logical_op]):
            # expression 2
            if query[expr2["field"]] == "Series":
                if isinstance(query[expr1["value"]], str) == False:
                    return print("This is not a string!")
            if query[expr2["field"]] == "Date":
                if isinstance(query[expr1["value"]], str) == False:
                    return print("This is not a string!")
            if query[expr2["field"]] == "Title":
                if isinstance(query[expr1["value"]], str) == False:
                    return print("This is not a string!")
            if query[expr2["field"]] == "Rating":
                if isinstance(query[expr1["value"]], float) == False:
                    return print("This is not a float!")

    def do_query(user_query):
        #declare firebase
        fire = Firebase()
        valid_query = validate_query(user_query)
        return fire.perform_firebase_query(self, valid_query)

    # takes firebase thing and converts into list of movie objects
    # (does not take into consideration doc yet)
    def from_dict(query):
        movie_list = []
        db = do_query(query)
        for i in db:
            mov_obj = Movie(db[i][0], db[i][1], db[i][2], db[i][3])
            movie_list.append(mov_obj)
        return movie_list
