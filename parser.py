import pyparsing as pp

class Parser:
    # define keywords
    SERIES = pp.CaselessKeyword("series")
    DATE = pp.CaselessKeyword("date")
    TITLE = pp.CaselessKeyword("title")
    RATING = pp.CaselessKeyword("rating")

    # define operators + set results name for dict
    logical_op = (pp.Keyword("AND") | pp.Keyword("OR"))("logical_op")
    comparison_op = pp.one_of("== < <= > >=")("comparison_op")

    # define fields + set results name for dict
    field = (SERIES | DATE | TITLE | RATING)("field")

    # handle multi-word value strings
    unquoted_word = ~logical_op + pp.Word(pp.alphanums + ".:-()")
    unquoted_val = pp.Combine(unquoted_word + pp.ZeroOrMore(pp.White(" ") + unquoted_word))

    # define value + set results name for dict
    value = (pp.QuotedString("'") | unquoted_val)("value")

    # define expression format
    expr = pp.Forward()
    base_expr = pp.Group(field + comparison_op + value)
    expr << base_expr("expr1") + (logical_op + base_expr("expr2"))[..., 1] + ~(logical_op + base_expr)


    def parse(self, query):
        """Parses user query into a dictionary of matched tokens.

        Args:
            query (str): The user query string to be parsed.

        Returns:
            tuple[bool, dict | str]: If the query was valid, returns True and the parsed dictionary.
                If the query was invalid, returns False and the error message.
        """
        try:
            # parse query using defined query language
            result = self.expr.parse_string(query, parse_all=True)
            return True, result.as_dict()
        
        except pp.ParseException as e:
            return False, str(e)

if __name__ == "__main__":

    parser = Parser()

    user_query_str = "Date < 1995-10-30" # change this line to test valid/invalid queries
    is_valid, details = parser.parse(user_query_str)
    if is_valid:
        print(f"Valid Query: {is_valid}\nDict: {details}")
    else:
        print(f"Valid Query: {is_valid}\nError Message: {details}")

    # for testing
    valid_queries = [
        "Date < 1995-10-30",
        "Title == 'Night at the Museum: Secret of the Tomb'",
        "rating < 5.0 AND rating > 3.0",
        "Title == Loose Change: 2nd Edition",
        "Title == Pokemon Ranger and the Temple of the Sea AND Rating > 4.0"
        ]

    invalid_queries = [
        "age = 21.0" # incorrect field keyword
        "rating = 2.0", # incorrect comparison_op (must be ==)
        "rating < 5.0 and rating > 3.0" # incorrect logical_op (must be AND)
        "series == None OR rating == 0.0 OR date < 1995-10-30" # conjoined query w/ more than two conditions 
    ]

    # for GUI help window
    help_ex_queries = [
        "series == 'Divergent Collection'", # handles quoted + unquoted strings
        "Date > 2010-01-01", 
        "TITLE == The Hills Have Eyes",
        "rating <= 6.0",
        "rating > 3 AND rating < 7", # conjoined statement ex.
        "series == None OR rating == 0.0" # NULL series ex. (optional field)
    ]