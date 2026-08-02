from binopnode import *
from number_node import *
from token import *

ast = BinOpNode(
    NumberNode(10),
    Token("PLUS", "+"),
    NumberNode(20)
)

print(ast)
