from django.utils.crypto import get_random_string

TOKEN_LENGTH = 128


def generate_token() -> str:
    return get_random_string(length=TOKEN_LENGTH)
