import string


def caesar(plaintext: str, shift: int) -> str:
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


if __name__ == '__main__':
    user_input = input("Enter a string: ")
    user_shift = int(input("Enter a shift: "))
    print(caesar(user_input, user_shift))
