import re

class Tokenizer:
    def split_word(self, text):
        tokens = []
        current_token = ''
        for char in text:
            if char.isalpha():
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                current_token = ''
        if current_token:
            tokens.append(current_token)
        return tokens

txt = 'Сосны обступали тропу плотно, и, хотя истыканное их верхушками небо светилось голубым, в лесу было сумрачно.'
tokenizer = Tokenizer()
tokens = tokenizer.split_word(txt)
print(tokens)