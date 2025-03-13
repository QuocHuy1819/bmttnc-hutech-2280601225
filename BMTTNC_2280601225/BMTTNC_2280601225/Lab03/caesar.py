from cipher.caesar import ALPHABET

class CaesarCipher:
    def _init_(selt):
        selt.alphanbet = ALPHABET

    def encrypt_text(selt, text: str, key: int) -> str:
        alphanbet_len = len(selt.alphanbet)
        text = text.upper()
        encrypt_text = []
        for letter in text:
            letter_index = selt.alphanbet.index(letter)
            output_index = (letter_index + key) % alphanbet_len
            output_index = selt.alphanbet[output_index]
            encrypt_text.append(output_index)
        return "".join(encrypt_text)
    def decrypt_text(selt, text: str, key: int) -> str:
        alphanbet_len = len(selt.alphanbet)
        text = text.upper()
        decrypt_text = []
        for letter in text:
            letter_index = selt.alphanbet.index(letter)
            output_index = (letter_index - key) % alphanbet_len
            output_index = selt.alphanbet[output_index]
            decrypt_text.append(output_letter)
            return "".join(decrypt_text)   
