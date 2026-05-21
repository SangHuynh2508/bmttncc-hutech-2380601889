class TraspositionCipher:
    def __init__(self):
        pass

    def transposition_encrypt(self, plain_text, key):
        cipher_text = [''] * key
        for column in range(key):
            pointer = column
            while pointer < len(plain_text):
                cipher_text[column] += plain_text[pointer]
                pointer += key
        return ''.join(cipher_text)