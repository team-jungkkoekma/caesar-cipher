import string


def caesar(plaintext: str, shift: int, decode=False) -> str:
    if decode:
        shift = 26 - shift
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.lower().translate(table)


if __name__ == '__main__':
    is_decode = input("Decode? (y/n): ")
    user_input = input("Enter a string: ")
    user_shift = int(input("Enter a shift: "))
    if is_decode == 'y':
        print(caesar(user_input, user_shift, decode=True))
    else:
        print(caesar(user_input, user_shift))
