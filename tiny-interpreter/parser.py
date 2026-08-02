from number_node import *
from binopnode import *
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def eat(self, token_type):

        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.token_type}")



    def expr(self):
        left = NumberNode(self.current_token.value)
        self.eat("NUMBER")
        op = self.current_token
        self.eat("PLUS")
        right = NumberNode(self.current_token.value)
        self.eat("NUMBER")

        return BinOpNode(left, op, right)
