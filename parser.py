import pyparsing as pp

class Parser:
    # define keywords
    SERIES = pp.Keyword("Series")
    DATE = pp.Keyword("Date")
    TITLE = pp.Keyword("Title")
    RATING = pp.Keyword("Rating")

    # define operators
    AND, OR = pp.Keyword.using_each(["AND", "OR"])
    comparison_op = pp.one_of("== < <= > >=")("operator")

    # define fields + set results name for dict
    field = (SERIES | DATE | TITLE | RATING)("field")

    # define value + set results name for dict
    value = (pp.Word(pp.alphanums + ".-") | pp.QuotedString("'"))("value")

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

    # TODO: Handle parsing multi-word values w/out needing quotes
    # TODO: Figure out what to do about punctuation inside of value strings
    # TODO: Handle NULL values for optional field (series)
    test_queries = [
        "Date < 1995-10-30",
        "Title == 'Night at the Museum: Secret of the Tomb'",
        "Rating >= 3.2",
        "Title == 'Pirate's Passage'"]

    for query in test_queries:
        print(parser.parse(query))

    