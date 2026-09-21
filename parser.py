import pyparsing as pp

class Parser:
    # define keywords
    SERIES = pp.CaselessKeyword("Series")
    DATE = pp.CaselessKeyword("Date")
    TITLE = pp.CaselessKeyword("Title")
    RATING = pp.CaselessKeyword("Rating")

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
    expr << base_expr("expr1") + pp.ZeroOrMore(logical_op + base_expr("expr2"))

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
        "rating > 5.0 AND rating < 3.0",
        "Title == Magic & Bird: A Courtship of Rivals",
        "Title == Loose Change: 2nd Edition",
        "Title == Pokemon Ranger and the Temple of the Sea"]

    for query in test_queries:
        print(parser.parse(query))