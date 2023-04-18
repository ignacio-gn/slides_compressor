MATCH_PERCENT = 0.97


def get_input(msg: str) -> str:
    while not (inp := input(msg)):
        print("Please enter a valid string")
    return inp


def is_contained(str1: str, str2: str) -> bool:
    n_matches = len(list(filter(lambda word: word in str2.split(" "), str1.split(" "))))
    if n_matches / len(str1.split(" ")) > MATCH_PERCENT:
        return True

    return False
