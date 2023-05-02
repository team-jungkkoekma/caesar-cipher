import string


def caesar(shift: int) -> str:
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return shifted_alphabet


if __name__ == '__main__':
    user_shift = int(input("Enter a shift: "))
    print(caesar(user_shift))
