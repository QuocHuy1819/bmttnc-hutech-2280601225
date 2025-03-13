class VigenereCipher:
     def _init_(selt):
        pass

     def vigenere_encrypt(selt, plain_text, key):
        encrypt_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord ('A')
                if char.isupper():
                    encrypt_text +=chr((ord(char) - ord('A') + 
                    key_shift) % 26 + ord('A'))
                    else:
                        encrypt_text +=chr((ord(char) - ord('A') + 
                        key_shift) % 26 + ord('A'))
                    key_index +=1
            else:
                encrypt_text += char
        return encrypt_text

    def vigenere_encrypt(selt, plain_text, key):
        decrypt_text = ""
        key_index = 0
        for char in encrypt_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord ('A')
                if char.isupper():
                    decrypt_text += chr((ord(char) - ord('A') - key_shift) %26 + ord('A'))
                    else:
                        decrypt_text += chr((ord(char) - ord('A') - key_shift) %26 + ord('a'))
                        key_index += 1
                        else:
                            decrypt_text += char
                            return decrypt_text


        