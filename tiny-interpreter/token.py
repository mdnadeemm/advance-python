class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.token_type}({self.value})"




#t1 = Token("NUMBER", 10)

#t2 = Token("PLUS", "+")
#print(t1)
#print(t2)
