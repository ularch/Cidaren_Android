from api.basic_api import use_api_get_prototype


def word_revert(word: str) -> str:
    return use_api_get_prototype(word)


if __name__ == '__main__':
    print(word_revert('installed'))
