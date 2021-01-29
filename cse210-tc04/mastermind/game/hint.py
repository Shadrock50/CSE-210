class Hint:
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.

    Returns:
        string: A hint in the form [xxxx]
    """ 
    hint = ""
    for index, letter in enumerate(guess):
        if code[index] == letter:
            hint += "x"
        elif letter in code:
            hint += "o"
        else:
            hint += "*"
    return hint