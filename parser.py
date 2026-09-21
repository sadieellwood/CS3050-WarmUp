import pyparsing as pp

class Parser:
    # define keywords
    SERIES = pp.CaselessKeyword("Series")
    DATE = pp.CaselessKeyword("Date")
    TITLE = pp.CaselessKeyword("Title")
    RATING = pp.CaselessKeyword("Rating")

    # define operators
    AND, OR = pp.Keyword.using_each(["AND", "OR"])
    comparison_op = pp.one_of("== < <= > >=")("operator")

    # define fields + set results name for dict
    field = (SERIES | DATE | TITLE | RATING)("field")

    # define value + set results name for dict
    # value = (pp.Word(pp.alphanums + ".-") | pp.QuotedString("'"))("value")

    value = (pp.QuotedString("'") | pp.rest_of_line())("value")

    # TODO: Add functionality for conjoined expressions
    # define expression format
    expr = field + comparison_op + value


    def parse(self, query):
        # parse query using defined query language
        result = self.expr.parse_string(query)
        # return dict of matched tokens
        return result.as_dict()

if __name__ == "__main__":
    # create a Parser object
    parser = Parser()

    # TODO: Handle NULL values for optional field (series)
    test_queries = [
        "Date < 1995-10-30",
        "Title == 'Night at the Museum: Secret of the Tomb'",
        "Rating >= 3.2",
        "rating == 5.0",
        "Title == Pirates Passage",
        "Title == Loose Change: 2nd Edition"]

    for query in test_queries:
        print(parser.parse(query))