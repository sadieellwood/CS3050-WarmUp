from firebase_connection import Firebase
from datetime import datetime, timezone


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

    def __str__(self):
        string = f"{self.title} ({self.release_date.year})"

        if self.series != None:
            string + f" from the {self.series}"

        return string

# running query functions
@staticmethod
def validate_query(query_spec):

    # convert date into actual date object with try except
    try:
        # checking that rating is a number
        current_test = ("Rating", "a number")
        for key in query_spec.keys():
            if key == "logical_op":
                pass
            elif "rating" in query_spec[key].values():
                query_spec[key]["value"] = float(query_spec[key]["value"])

                #rating should not be negative or greater than 10
                if query_spec[key]["value"] > 10 or query_spec[key]["value"] < 0:
                    current_test = ("Rating", "between 0 and 10")
                    raise ValueError

        # checking that date is actually a date
        current_test = ("Date", "a date in the form YYYY-MM-DD")
        for key in query_spec.keys():
            if key == "logical_op":
                pass

            elif "date" in query_spec[key].values():
                query_spec[key]["value"] = datetime.fromisoformat(
                    query_spec[key]["value"] + " 00:00:00"
                ).replace(tzinfo=timezone.utc)

        # checking that series and title are only using == operators 
        for key in query_spec.keys():
            if key == "logical_op":
                pass

            elif "title" in query_spec[key].values():
                current_test = ("title", "used with ==")
                if query_spec[key]["comparison_op"] != "==":
                    raise ValueError

            elif "series" in query_spec[key].values():
                current_test = ("series", "used with ==")
                if query_spec[key]["comparison_op"] != "==":
                    raise ValueError
                # converting "None" string to type None
                if query_spec[key]["value"] == "None":
                    query_spec[key]["value"] = None
                
                
    except ValueError as e:
        message = f"Invalid query! {current_test[0]} must be {current_test[1]}"
        return False, message

    return True, query_spec

# takes firebase thing and converts into list of movie objects
# (does not take into consideration doc yet)
@staticmethod
def from_dict(dictionary):
    try:
        movie = Movie(
            dictionary["series"],
            dictionary["date"],
            dictionary["title"],
            dictionary["rating"],
        )
        return movie
    except KeyError:
        return "dictionary missing key"


def do_query(user_query):

    # declare firebase
    fire = Firebase()

    valid_query = validate_query(user_query)

    if valid_query[0]:
        #returns a list of dictionaries
        query_results = fire.perform_firebase_query(valid_query[1])

        # make each dictionary an instance of movie
        query_results =[from_dict(result) for result in query_results]

        return (True, query_results)
    # this will return (False, errorMessage) if query is not valid
    return valid_query