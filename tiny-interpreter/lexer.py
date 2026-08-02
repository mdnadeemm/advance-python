from token import Token
class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[0]

    def advance(self):
        self.pos +=1
        if self.pos >= len(self.text):
            self.current_char = None
        else:self.current_char = self.text[self.pos]

    def integer(self):
        result = ""

        while self.current_char is not None and self.current_char.isdigit() :
            result += self.current_char
            self.advance()

        return int(result)


    def get_next_token(self):
        if self.current_char is not None and self.current_char.isdigit():
            return Token("NUMBER", self.integer())
        if self.current_char == '+':
            self.advance()

            return Token("PLUS", "+")
        if self.current_char is None:
            return "EOF"




lexer = Lexer("10+20")

print(lexer.get_next_token())
print(lexer.get_next_token())
print(lexer.get_next_token())
print(lexer.get_next_token())

#print(lexer.current_char)  # 1

#lexer.advance()
#print(lexer.current_char)  # 0

#lexer.advance()
#print(lexer.current_char)  # ?
