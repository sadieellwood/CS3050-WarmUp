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
    unquoted_word = ~logical_op + pp.Word(pp.alphanums + ".-()")
    unquoted_val = pp.Combine(
        unquoted_word + pp.ZeroOrMore(pp.White(" ") + unquoted_word)
    )

    # define value + set results name for dict
    value = (pp.QuotedString("'") | unquoted_val)("value")

    # define expression format
    expr = pp.Forward()
    base_expr = pp.Group(field + comparison_op + value)
    expr << base_expr("expr1") + (logical_op + base_expr("expr2"))[..., 1] + ~(
        logical_op + base_expr
    )

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
            result = self.expr.parse_string(query, parse_all=True).as_dict()
            
            return True, result

        except pp.ParseException as e:
            message = "Invalid query! Check help window for correct syntax."
            return False, message

